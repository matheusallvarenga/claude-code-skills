#!/usr/bin/env python3
"""
ITM Audit System - Scanner Module
Varredura recursiva de diretórios com coleta de metadados.
"""

import os
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Generator
from dataclasses import dataclass, asdict

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('itm_audit.scanner')

@dataclass
class FileMetadata:
    """Metadados de um arquivo."""
    path: str
    name: str
    extension: str
    size_bytes: int
    created_at: str
    modified_at: str
    accessed_at: str
    is_symlink: bool = False
    error: Optional[str] = None

class Scanner:
    """Scanner de diretórios com suporte a checkpoint."""
    
    def __init__(self, 
                 checkpoint_dir: str = "data",
                 checkpoint_interval: int = 1000,
                 exclude_patterns: Optional[List[str]] = None):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_interval = checkpoint_interval
        self.exclude_patterns = exclude_patterns or [
            '.git', '__pycache__', 'node_modules', '.DS_Store',
            '.Trash', '.cache', 'venv', '.venv'
        ]
        self.results: List[FileMetadata] = []
        self.errors: List[Dict] = []
        self.processed_count = 0
        self.start_time: Optional[datetime] = None
        
    def should_exclude(self, path: Path) -> bool:
        """Verifica se o path deve ser excluído."""
        for pattern in self.exclude_patterns:
            if pattern in path.parts:
                return True
        return False
    
    def get_file_metadata(self, file_path: Path) -> FileMetadata:
        """Extrai metadados de um arquivo."""
        try:
            stat = file_path.stat()
            return FileMetadata(
                path=str(file_path.absolute()),
                name=file_path.name,
                extension=file_path.suffix.lower(),
                size_bytes=stat.st_size,
                created_at=datetime.fromtimestamp(stat.st_ctime).isoformat(),
                modified_at=datetime.fromtimestamp(stat.st_mtime).isoformat(),
                accessed_at=datetime.fromtimestamp(stat.st_atime).isoformat(),
                is_symlink=file_path.is_symlink()
            )
        except PermissionError:
            return FileMetadata(
                path=str(file_path),
                name=file_path.name,
                extension=file_path.suffix.lower(),
                size_bytes=0,
                created_at="",
                modified_at="",
                accessed_at="",
                error="Permission denied"
            )
        except Exception as e:
            return FileMetadata(
                path=str(file_path),
                name=file_path.name,
                extension=file_path.suffix.lower(),
                size_bytes=0,
                created_at="",
                modified_at="",
                accessed_at="",
                error=str(e)
            )
    
    def scan_directory(self, root_path: str) -> Generator[FileMetadata, None, None]:
        """
        Varre diretório recursivamente.
        Yields metadados de cada arquivo encontrado.
        """
        root = Path(root_path)
        
        if not root.exists():
            raise ValueError(f"Path não existe: {root_path}")
        
        if not root.is_dir():
            raise ValueError(f"Path não é diretório: {root_path}")
        
        self.start_time = datetime.now()
        logger.info(f"Iniciando scan de: {root_path}")
        
        for dirpath, dirnames, filenames in os.walk(root, topdown=True):
            current_path = Path(dirpath)
            
            # Filtrar diretórios excluídos
            dirnames[:] = [d for d in dirnames 
                          if not self.should_exclude(current_path / d)]
            
            for filename in filenames:
                file_path = current_path / filename
                
                if self.should_exclude(file_path):
                    continue
                
                metadata = self.get_file_metadata(file_path)
                self.results.append(metadata)
                self.processed_count += 1
                
                if metadata.error:
                    self.errors.append({
                        'path': metadata.path,
                        'error': metadata.error
                    })
                
                # Checkpoint
                if self.processed_count % self.checkpoint_interval == 0:
                    self.save_checkpoint()
                    logger.info(f"Checkpoint: {self.processed_count} arquivos processados")
                
                yield metadata
        
        logger.info(f"Scan completo: {self.processed_count} arquivos")
    
    def save_checkpoint(self, filename: Optional[str] = None):
        """Salva checkpoint do estado atual."""
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"checkpoint_scan_{timestamp}.json"
        
        checkpoint_path = self.checkpoint_dir / filename
        
        checkpoint_data = {
            'phase': 'SCAN',
            'processed_count': self.processed_count,
            'timestamp': datetime.now().isoformat(),
            'results_count': len(self.results),
            'errors_count': len(self.errors),
            'last_path': self.results[-1].path if self.results else None
        }
        
        with open(checkpoint_path, 'w', encoding='utf-8') as f:
            json.dump(checkpoint_data, f, indent=2)
        
        logger.debug(f"Checkpoint salvo: {checkpoint_path}")
    
    def save_results(self, output_path: str):
        """Salva resultados completos em JSON."""
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'scan_info': {
                'total_files': len(self.results),
                'total_errors': len(self.errors),
                'scan_duration': str(datetime.now() - self.start_time) if self.start_time else None,
                'generated_at': datetime.now().isoformat()
            },
            'files': [asdict(f) for f in self.results],
            'errors': self.errors
        }
        
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Resultados salvos: {output_path}")
    
    def get_summary(self) -> Dict:
        """Retorna resumo estatístico."""
        total_size = sum(f.size_bytes for f in self.results if not f.error)
        extensions = {}
        
        for f in self.results:
            if f.error:
                continue
            ext = f.extension or '(sem extensão)'
            if ext not in extensions:
                extensions[ext] = {'count': 0, 'size': 0}
            extensions[ext]['count'] += 1
            extensions[ext]['size'] += f.size_bytes
        
        return {
            'total_files': len(self.results),
            'total_size_bytes': total_size,
            'total_size_human': self._human_size(total_size),
            'total_errors': len(self.errors),
            'by_extension': dict(sorted(
                extensions.items(), 
                key=lambda x: x[1]['size'], 
                reverse=True
            )[:20])
        }
    
    @staticmethod
    def _human_size(size_bytes: int) -> str:
        """Converte bytes para formato legível."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} PB"


def main():
    """Exemplo de uso."""
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python scanner.py <diretório>")
        sys.exit(1)
    
    target_dir = sys.argv[1]
    scanner = Scanner()
    
    # Executar scan
    for metadata in scanner.scan_directory(target_dir):
        pass  # Processamento acontece no generator
    
    # Salvar resultados
    scanner.save_results("data/scan_results.json")
    
    # Mostrar resumo
    summary = scanner.get_summary()
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
