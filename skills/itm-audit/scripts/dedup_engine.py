#!/usr/bin/env python3
"""
ITM Audit System - Deduplication Engine
Motor de identificação e análise de duplicatas.
"""

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('itm_audit.dedup')


@dataclass
class DuplicateFile:
    """Informações de um arquivo em grupo de duplicatas."""
    path: str
    size_bytes: int
    modified_at: str
    source: str  # Fonte/diretório raiz


@dataclass
class DuplicateGroup:
    """Grupo de arquivos duplicados."""
    hash: str
    file_count: int
    individual_size: int
    total_size: int
    recoverable_space: int
    files: List[DuplicateFile]
    recommended_keep: Optional[str] = None


class DeduplicationEngine:
    """Motor de identificação de duplicatas."""
    
    def __init__(self):
        self.groups: List[DuplicateGroup] = []
        self.unique_files: List[str] = []
        self.total_recoverable: int = 0
    
    def analyze(self, 
                hash_index: Dict[str, str],
                file_metadata: Dict[str, Dict]) -> List[DuplicateGroup]:
        """
        Analisa índice de hashes para identificar duplicatas.
        
        Args:
            hash_index: Dict[path -> hash]
            file_metadata: Dict[path -> metadata]
            
        Returns:
            Lista de grupos de duplicatas ordenados por impacto
        """
        logger.info("Iniciando análise de duplicatas...")
        
        # Agrupar por hash
        hash_groups: Dict[str, List[str]] = defaultdict(list)
        for path, file_hash in hash_index.items():
            hash_groups[file_hash].append(path)
        
        # Processar grupos
        for file_hash, paths in hash_groups.items():
            if len(paths) == 1:
                self.unique_files.append(paths[0])
                continue
            
            # Criar grupo de duplicatas
            files = []
            for path in paths:
                meta = file_metadata.get(path, {})
                files.append(DuplicateFile(
                    path=path,
                    size_bytes=meta.get('size_bytes', 0),
                    modified_at=meta.get('modified_at', ''),
                    source=self._get_source(path)
                ))
            
            # Ordenar por data de modificação (mais antigo primeiro)
            files.sort(key=lambda x: x.modified_at)
            
            individual_size = files[0].size_bytes if files else 0
            total_size = individual_size * len(files)
            recoverable = individual_size * (len(files) - 1)
            
            group = DuplicateGroup(
                hash=file_hash,
                file_count=len(files),
                individual_size=individual_size,
                total_size=total_size,
                recoverable_space=recoverable,
                files=files,
                recommended_keep=files[0].path if files else None
            )
            
            self.groups.append(group)
            self.total_recoverable += recoverable
        
        # Ordenar por espaço recuperável (maior primeiro)
        self.groups.sort(key=lambda x: x.recoverable_space, reverse=True)
        
        logger.info(f"Análise completa: {len(self.groups)} grupos de duplicatas")
        logger.info(f"Espaço recuperável total: {self._human_size(self.total_recoverable)}")
        
        return self.groups
    
    def analyze_from_files(self,
                           hash_index_path: str,
                           scan_results_path: str) -> List[DuplicateGroup]:
        """
        Analisa a partir de arquivos JSON.
        
        Args:
            hash_index_path: Caminho para hash_index.json
            scan_results_path: Caminho para scan_results.json
            
        Returns:
            Lista de grupos de duplicatas
        """
        # Carregar hash index
        with open(hash_index_path, 'r', encoding='utf-8') as f:
            hash_data = json.load(f)
        hash_index = hash_data.get('hash_index', {})
        
        # Carregar metadados
        with open(scan_results_path, 'r', encoding='utf-8') as f:
            scan_data = json.load(f)
        
        # Converter lista para dict por path
        file_metadata = {
            f['path']: f for f in scan_data.get('files', [])
        }
        
        return self.analyze(hash_index, file_metadata)
    
    def get_summary(self) -> Dict:
        """Retorna resumo da análise."""
        return {
            'total_duplicate_groups': len(self.groups),
            'total_duplicate_files': sum(g.file_count for g in self.groups),
            'total_unique_files': len(self.unique_files),
            'total_recoverable_bytes': self.total_recoverable,
            'total_recoverable_human': self._human_size(self.total_recoverable),
            'top_10_by_impact': [
                {
                    'hash': g.hash[:16] + '...',
                    'files': g.file_count,
                    'recoverable': self._human_size(g.recoverable_space)
                }
                for g in self.groups[:10]
            ]
        }
    
    def get_pareto_groups(self, threshold: float = 0.8) -> List[DuplicateGroup]:
        """
        Retorna grupos que representam X% do espaço recuperável.
        
        Args:
            threshold: Percentual do espaço total (0.8 = 80%)
            
        Returns:
            Lista de grupos prioritários
        """
        if not self.groups:
            return []
        
        target = self.total_recoverable * threshold
        accumulated = 0
        pareto_groups = []
        
        for group in self.groups:
            pareto_groups.append(group)
            accumulated += group.recoverable_space
            if accumulated >= target:
                break
        
        return pareto_groups
    
    def save_results(self, output_path: str):
        """Salva resultados da análise em JSON."""
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'dedup_info': {
                'total_groups': len(self.groups),
                'total_duplicates': sum(g.file_count for g in self.groups),
                'total_unique': len(self.unique_files),
                'recoverable_bytes': self.total_recoverable,
                'recoverable_human': self._human_size(self.total_recoverable),
                'generated_at': datetime.now().isoformat()
            },
            'groups': [asdict(g) for g in self.groups],
            'summary': self.get_summary()
        }
        
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Resultados salvos: {output_path}")
    
    def _get_source(self, path: str) -> str:
        """Extrai fonte/raiz do path."""
        parts = Path(path).parts
        # Retorna os primeiros 3 níveis como identificador da fonte
        if len(parts) >= 3:
            return str(Path(*parts[:3]))
        return str(Path(*parts))
    
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
    
    if len(sys.argv) < 3:
        print("Uso: python dedup_engine.py <hash_index.json> <scan_results.json>")
        sys.exit(1)
    
    hash_path = sys.argv[1]
    scan_path = sys.argv[2]
    
    engine = DeduplicationEngine()
    engine.analyze_from_files(hash_path, scan_path)
    
    # Salvar resultados
    engine.save_results("data/dedup_results.json")
    
    # Mostrar resumo
    summary = engine.get_summary()
    print(json.dumps(summary, indent=2))
    
    # Mostrar grupos Pareto
    print("\n--- Top 20% que representam 80% do espaço ---")
    pareto = engine.get_pareto_groups(0.8)
    print(f"Grupos prioritários: {len(pareto)} de {len(engine.groups)}")


if __name__ == "__main__":
    main()
