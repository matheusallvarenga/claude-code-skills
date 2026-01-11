#!/usr/bin/env python3
"""
ITM Audit System - Classifier Module
Classificação de arquivos por tipo, idade e padrões.
"""

import json
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('itm_audit.classifier')

# Categorias de arquivos por extensão
FILE_CATEGORIES = {
    'documentos': ['.pdf', '.doc', '.docx', '.txt', '.md', '.rtf', '.odt', '.pages'],
    'planilhas': ['.xls', '.xlsx', '.csv', '.numbers', '.ods'],
    'apresentacoes': ['.ppt', '.pptx', '.key', '.odp'],
    'imagens': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp', '.tiff', '.ico', '.heic'],
    'videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.m4v'],
    'audio': ['.mp3', '.wav', '.m4a', '.flac', '.aac', '.ogg', '.wma'],
    'codigo': ['.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.c', '.cpp', '.h', '.cs', '.go', '.rs', '.rb', '.php', '.swift', '.kt'],
    'config': ['.json', '.yaml', '.yml', '.xml', '.toml', '.ini', '.env', '.conf'],
    'arquivos': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
    'executaveis': ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm'],
    'fontes': ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
    'dados': ['.sql', '.db', '.sqlite', '.mdb'],
}

# Categorias de idade
AGE_CATEGORIES = {
    'recente': 30,      # < 30 dias
    'ativo': 180,       # 30-180 dias
    'arquivado': 365,   # 180-365 dias
    'legacy': float('inf')  # > 365 dias
}


@dataclass
class ClassificationResult:
    """Resultado de classificação de um arquivo."""
    path: str
    type_category: str
    age_category: str
    size_category: str
    days_since_modified: int
    size_bytes: int


@dataclass
class CategoryStats:
    """Estatísticas de uma categoria."""
    count: int
    total_size: int
    percentage_count: float
    percentage_size: float
    files: List[str]


class Classifier:
    """Classificador de arquivos multi-dimensional."""
    
    def __init__(self):
        self.results: List[ClassificationResult] = []
        self.by_type: Dict[str, CategoryStats] = {}
        self.by_age: Dict[str, CategoryStats] = {}
        self.by_size: Dict[str, CategoryStats] = {}
        self.total_files = 0
        self.total_size = 0
    
    def classify_type(self, extension: str) -> str:
        """Classifica arquivo por extensão."""
        ext = extension.lower()
        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                return category
        return 'outros'
    
    def classify_age(self, modified_at: str) -> tuple:
        """
        Classifica arquivo por idade.
        
        Returns:
            Tuple[categoria, dias_desde_modificacao]
        """
        try:
            if not modified_at:
                return 'desconhecido', -1
            
            # Parse ISO format
            mod_date = datetime.fromisoformat(modified_at.replace('Z', '+00:00'))
            if mod_date.tzinfo:
                mod_date = mod_date.replace(tzinfo=None)
            
            days = (datetime.now() - mod_date).days
            
            if days < AGE_CATEGORIES['recente']:
                return 'recente', days
            elif days < AGE_CATEGORIES['ativo']:
                return 'ativo', days
            elif days < AGE_CATEGORIES['arquivado']:
                return 'arquivado', days
            else:
                return 'legacy', days
                
        except Exception:
            return 'desconhecido', -1
    
    def classify_size(self, size_bytes: int) -> str:
        """Classifica arquivo por tamanho."""
        if size_bytes < 1024:  # < 1KB
            return 'tiny'
        elif size_bytes < 1024 * 1024:  # < 1MB
            return 'small'
        elif size_bytes < 100 * 1024 * 1024:  # < 100MB
            return 'medium'
        elif size_bytes < 1024 * 1024 * 1024:  # < 1GB
            return 'large'
        else:
            return 'huge'
    
    def classify_files(self, files: List[Dict]) -> List[ClassificationResult]:
        """
        Classifica lista de arquivos.
        
        Args:
            files: Lista de dicts com metadados de arquivos
            
        Returns:
            Lista de resultados de classificação
        """
        logger.info(f"Classificando {len(files)} arquivos...")
        
        type_groups = defaultdict(lambda: {'count': 0, 'size': 0, 'files': []})
        age_groups = defaultdict(lambda: {'count': 0, 'size': 0, 'files': []})
        size_groups = defaultdict(lambda: {'count': 0, 'size': 0, 'files': []})
        
        for file_data in files:
            if file_data.get('error'):
                continue
            
            path = file_data.get('path', '')
            extension = file_data.get('extension', '')
            size = file_data.get('size_bytes', 0)
            modified = file_data.get('modified_at', '')
            
            # Classificar
            type_cat = self.classify_type(extension)
            age_cat, days = self.classify_age(modified)
            size_cat = self.classify_size(size)
            
            result = ClassificationResult(
                path=path,
                type_category=type_cat,
                age_category=age_cat,
                size_category=size_cat,
                days_since_modified=days,
                size_bytes=size
            )
            
            self.results.append(result)
            self.total_files += 1
            self.total_size += size
            
            # Agregar por categoria
            type_groups[type_cat]['count'] += 1
            type_groups[type_cat]['size'] += size
            type_groups[type_cat]['files'].append(path)
            
            age_groups[age_cat]['count'] += 1
            age_groups[age_cat]['size'] += size
            age_groups[age_cat]['files'].append(path)
            
            size_groups[size_cat]['count'] += 1
            size_groups[size_cat]['size'] += size
            size_groups[size_cat]['files'].append(path)
        
        # Converter para CategoryStats
        self.by_type = self._to_category_stats(type_groups)
        self.by_age = self._to_category_stats(age_groups)
        self.by_size = self._to_category_stats(size_groups)
        
        logger.info(f"Classificação completa: {self.total_files} arquivos")
        return self.results
    
    def classify_from_scan(self, scan_results_path: str) -> List[ClassificationResult]:
        """
        Classifica a partir de arquivo de scan.
        
        Args:
            scan_results_path: Caminho para scan_results.json
            
        Returns:
            Lista de resultados
        """
        with open(scan_results_path, 'r', encoding='utf-8') as f:
            scan_data = json.load(f)
        
        files = scan_data.get('files', [])
        return self.classify_files(files)
    
    def _to_category_stats(self, groups: Dict) -> Dict[str, CategoryStats]:
        """Converte grupos agregados para CategoryStats."""
        result = {}
        for name, data in groups.items():
            result[name] = CategoryStats(
                count=data['count'],
                total_size=data['size'],
                percentage_count=(data['count'] / self.total_files * 100) if self.total_files else 0,
                percentage_size=(data['size'] / self.total_size * 100) if self.total_size else 0,
                files=data['files'][:100]  # Limitar para não explodir o JSON
            )
        return result
    
    def get_summary(self) -> Dict:
        """Retorna resumo da classificação."""
        return {
            'total_files': self.total_files,
            'total_size_bytes': self.total_size,
            'total_size_human': self._human_size(self.total_size),
            'by_type': {
                k: {
                    'count': v.count,
                    'size_human': self._human_size(v.total_size),
                    'pct_count': f"{v.percentage_count:.1f}%",
                    'pct_size': f"{v.percentage_size:.1f}%"
                }
                for k, v in sorted(self.by_type.items(), key=lambda x: x[1].total_size, reverse=True)
            },
            'by_age': {
                k: {
                    'count': v.count,
                    'size_human': self._human_size(v.total_size),
                    'pct_count': f"{v.percentage_count:.1f}%",
                    'pct_size': f"{v.percentage_size:.1f}%"
                }
                for k, v in self.by_age.items()
            },
            'by_size': {
                k: {
                    'count': v.count,
                    'size_human': self._human_size(v.total_size),
                    'pct_count': f"{v.percentage_count:.1f}%"
                }
                for k, v in self.by_size.items()
            }
        }
    
    def get_legacy_candidates(self, min_days: int = 365) -> List[ClassificationResult]:
        """Retorna arquivos candidatos a arquivamento."""
        return [r for r in self.results if r.days_since_modified >= min_days]
    
    def get_large_files(self, min_size_mb: int = 100) -> List[ClassificationResult]:
        """Retorna arquivos grandes."""
        min_bytes = min_size_mb * 1024 * 1024
        return sorted(
            [r for r in self.results if r.size_bytes >= min_bytes],
            key=lambda x: x.size_bytes,
            reverse=True
        )
    
    def save_results(self, output_path: str):
        """Salva resultados em JSON."""
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'classification_info': {
                'total_files': self.total_files,
                'total_size': self.total_size,
                'generated_at': datetime.now().isoformat()
            },
            'summary': self.get_summary(),
            'by_type': {k: asdict(v) for k, v in self.by_type.items()},
            'by_age': {k: asdict(v) for k, v in self.by_age.items()},
            'by_size': {k: asdict(v) for k, v in self.by_size.items()}
        }
        
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Resultados salvos: {output_path}")
    
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
        print("Uso: python classifier.py <scan_results.json>")
        sys.exit(1)
    
    scan_path = sys.argv[1]
    classifier = Classifier()
    
    # Classificar
    classifier.classify_from_scan(scan_path)
    
    # Salvar
    classifier.save_results("data/classification_results.json")
    
    # Mostrar resumo
    summary = classifier.get_summary()
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
