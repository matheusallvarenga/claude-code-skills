#!/usr/bin/env python3
"""
ITM Audit System - Hasher Module
Cálculo de hashes SHA-256 para detecção de duplicatas.
"""

import hashlib
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('itm_audit.hasher')

# Constantes
CHUNK_SIZE = 65536  # 64KB


class Hasher:
    """Calculador de hashes com estratégia chunk+size."""
    
    def __init__(self,
                 checkpoint_dir: str = "data",
                 checkpoint_interval: int = 500,
                 max_workers: int = 4):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_interval = checkpoint_interval
        self.max_workers = max_workers
        self.hash_index: Dict[str, str] = {}  # path -> hash
        self.processed_count = 0
        self.errors: List[Dict] = []
        self.start_time: Optional[datetime] = None
    
    def calculate_hash(self, file_path: str) -> Tuple[str, Optional[str]]:
        """
        Calcula hash composto (SHA-256 do chunk + tamanho).
        
        Returns:
            Tuple[path, hash ou None se erro]
        """
        try:
            path = Path(file_path)
            
            if not path.exists():
                return file_path, None
            
            if not path.is_file():
                return file_path, None
            
            file_size = path.stat().st_size
            
            # Ler chunk inicial (ou arquivo completo se menor)
            with open(path, 'rb') as f:
                chunk = f.read(CHUNK_SIZE)
            
            # Calcular SHA-256 do chunk
            chunk_hash = hashlib.sha256(chunk).hexdigest()
            
            # Hash composto: chunk_hash + tamanho
            composite_hash = f"{chunk_hash}_{file_size}"
            
            return file_path, composite_hash
            
        except PermissionError:
            self.errors.append({
                'path': file_path,
                'error': 'Permission denied'
            })
            return file_path, None
        except Exception as e:
            self.errors.append({
                'path': file_path,
                'error': str(e)
            })
            return file_path, None
    
    def hash_files(self, file_paths: List[str]) -> Dict[str, str]:
        """
        Calcula hashes para lista de arquivos.
        
        Args:
            file_paths: Lista de caminhos de arquivos
            
        Returns:
            Dict mapeando path -> hash
        """
        self.start_time = datetime.now()
        total_files = len(file_paths)
        logger.info(f"Iniciando hash de {total_files} arquivos")
        
        # Processamento paralelo
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self.calculate_hash, fp): fp 
                for fp in file_paths
            }
            
            for future in as_completed(futures):
                file_path, file_hash = future.result()
                
                if file_hash:
                    self.hash_index[file_path] = file_hash
                
                self.processed_count += 1
                
                # Checkpoint
                if self.processed_count % self.checkpoint_interval == 0:
                    self.save_checkpoint()
                    progress = (self.processed_count / total_files) * 100
                    logger.info(f"Progresso: {self.processed_count}/{total_files} ({progress:.1f}%)")
        
        logger.info(f"Hash completo: {len(self.hash_index)} arquivos hasheados")
        return self.hash_index
    
    def hash_from_scan_results(self, scan_results_path: str) -> Dict[str, str]:
        """
        Calcula hashes a partir de resultados de scan.
        
        Args:
            scan_results_path: Caminho para scan_results.json
            
        Returns:
            Dict mapeando path -> hash
        """
        with open(scan_results_path, 'r', encoding='utf-8') as f:
            scan_data = json.load(f)
        
        # Extrair paths de arquivos sem erro
        file_paths = [
            f['path'] for f in scan_data.get('files', [])
            if not f.get('error')
        ]
        
        return self.hash_files(file_paths)
    
    def save_checkpoint(self, filename: Optional[str] = None):
        """Salva checkpoint do estado atual."""
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"checkpoint_hash_{timestamp}.json"
        
        checkpoint_path = self.checkpoint_dir / filename
        
        checkpoint_data = {
            'phase': 'HASH',
            'processed_count': self.processed_count,
            'timestamp': datetime.now().isoformat(),
            'hashed_count': len(self.hash_index),
            'errors_count': len(self.errors)
        }
        
        with open(checkpoint_path, 'w', encoding='utf-8') as f:
            json.dump(checkpoint_data, f, indent=2)
        
        logger.debug(f"Checkpoint salvo: {checkpoint_path}")
    
    def save_results(self, output_path: str):
        """Salva índice de hashes em JSON."""
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'hash_info': {
                'total_hashed': len(self.hash_index),
                'total_errors': len(self.errors),
                'hash_algorithm': 'SHA-256 (64KB chunk + size)',
                'generated_at': datetime.now().isoformat()
            },
            'hash_index': self.hash_index,
            'errors': self.errors
        }
        
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Hash index salvo: {output_path}")
    
    def load_cache(self, cache_path: str) -> int:
        """
        Carrega cache de hashes anteriores.
        
        Returns:
            Número de hashes carregados do cache
        """
        cache_file = Path(cache_path)
        
        if not cache_file.exists():
            return 0
        
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
            
            self.hash_index = cache_data.get('hash_index', {})
            loaded = len(self.hash_index)
            logger.info(f"Cache carregado: {loaded} hashes")
            return loaded
        except Exception as e:
            logger.warning(f"Erro ao carregar cache: {e}")
            return 0


def main():
    """Exemplo de uso."""
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python hasher.py <scan_results.json>")
        sys.exit(1)
    
    scan_results_path = sys.argv[1]
    hasher = Hasher()
    
    # Calcular hashes
    hasher.hash_from_scan_results(scan_results_path)
    
    # Salvar resultados
    hasher.save_results("data/hash_index.json")
    
    print(f"Hashes calculados: {len(hasher.hash_index)}")
    print(f"Erros: {len(hasher.errors)}")


if __name__ == "__main__":
    main()
