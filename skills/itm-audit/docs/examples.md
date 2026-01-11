# Exemplos de Uso - ITM Audit System

## Exemplo 1: Auditoria Básica de Diretório

### Cenário
Auditar pasta de Downloads para identificar duplicatas e arquivos grandes.

### Execução
```
/audit /Users/matheusallvarenga/Downloads --quick
```

### Output Esperado
```markdown
# Audit Report - Downloads
Generated: 2025-12-29 10:30:00

## Summary
- Total Files: 1,247
- Total Size: 45.3 GB
- Duplicates Found: 89 groups
- Recoverable Space: 12.1 GB

## Top 10 Largest Files
| File | Size | Last Modified |
|------|------|---------------|
| video_project.mp4 | 4.2 GB | 2025-11-15 |
| backup_2024.zip | 2.8 GB | 2025-10-01 |
...
```

---

## Exemplo 2: Análise de Estrutura (TREE)

### Cenário
Entender distribuição de espaço antes de auditoria completa em HD Externo.

### Execução
```python
from scripts.tree_analyzer import analyze_tree

result = analyze_tree(
    target_path="/Volumes/INTENTUM/Work",
    output_dir="Projects/itm-audit/data",
    max_depth=4,
    output_format='both'
)
```

### Output Esperado
```markdown
# Estrutura de Diretórios - INTENTUM/Work
Gerado: 2025-12-29 10:00:00

## Visão Geral
- Diretórios: 1,247
- Profundidade máxima analisada: 4 níveis

## Top 10 Maiores Diretórios
| Diretório | Tamanho | Arquivos |
|-----------|---------|----------|
| /Projects/video-assets | 245.3 GB | 892 |
| /Backups/2024 | 156.7 GB | 2,341 |
| /Design/exports | 89.2 GB | 5,678 |
| /Documents/archives | 67.8 GB | 12,456 |
...

## Árvore Hierárquica
Work/ (1.1 TB)
├── Projects/ (456.2 GB)
│   ├── video-assets/ (245.3 GB)
│   ├── client-work/ (123.4 GB)
│   └── internal/ (87.5 GB)
├── Backups/ (312.8 GB)
│   ├── 2024/ (156.7 GB)
│   └── 2023/ (156.1 GB)
└── Documents/ (198.4 GB)
    ├── archives/ (67.8 GB)
    └── active/ (130.6 GB)
```

### Uso Recomendado
- Executar TREE antes de HASH para identificar diretórios prioritários
- Usar output para decidir exclusões (ex: Backups antigos)
- Visualizar concentração de espaço (Pareto visual)

---

## Exemplo 3: Auditoria Multi-Fonte

### Cenário
Comparar arquivos entre Google Drive e HD Externo para consolidação.

### Execução
```
/audit --sources
  - /Users/matheusallvarenga/Library/CloudStorage/GoogleDrive-matheusallvarenga@intentum.ai
  - /Volumes/HD_External/Backups
--compare-mode
```

### Output Esperado
```markdown
# Cross-Source Audit Report

## Source Comparison
| Metric | Google Drive | HD External |
|--------|--------------|-------------|
| Files | 23,456 | 31,892 |
| Size | 125 GB | 289 GB |
| Unique | 18,234 | 22,109 |

## Cross-Duplicates
Files existing in BOTH sources: 5,222
Recoverable if consolidated: 67.3 GB

## Recommendations
1. HD External has 8,783 files not in Google Drive
2. Google Drive has 3,125 files not in HD External
3. Consider: Sync missing files before cleanup
```

---

## Exemplo 4: Auditoria Focada em Tipo

### Cenário
Identificar todos os PDFs e documentos para organização.

### Execução
```
/audit /path/to/documents --filter-types documentos,planilhas
```

### Output Esperado
```markdown
# Document Audit Report

## By Type
| Type | Count | Size |
|------|-------|------|
| PDF | 1,892 | 8.3 GB |
| DOCX | 567 | 1.2 GB |
| XLSX | 234 | 890 MB |
| CSV | 89 | 120 MB |

## Age Distribution
| Age | Count | Percentage |
|-----|-------|------------|
| Recent (<30d) | 234 | 12% |
| Active (30-180d) | 567 | 29% |
| Archived (180-365d) | 891 | 46% |
| Legacy (>365d) | 256 | 13% |

## Duplicate Documents
- 45 PDF groups (312 files total)
- Most duplicated: "Contract_Template.pdf" (12 copies)
```

---

## Exemplo 5: Retomada de Checkpoint

### Cenário
Auditoria interrompida, retomar do ponto de parada.

### Execução
```
/audit --resume
```

### Diálogo Esperado
```
Found checkpoint: checkpoint_scan_20251229_143022.json
- Phase: SCAN
- Processed: 15,234 / ~45,000 files
- Last path: /path/to/some/directory

Resume from checkpoint? [Y/n]: Y

Resuming SCAN phase...
[████████████░░░░░░░░] 34% (15,234 → processing...)
```

---

## Exemplo 6: Relatório de Ação Prioritária

### Cenário
Gerar plano de ação focado no maior impacto (Pareto).

### Execução
```
/audit /path --action-plan --pareto
```

### Output Esperado
```markdown
# Action Plan - Pareto Priority

## Quick Wins (80% impact, 20% effort)

### 1. Delete Duplicate Videos (Impact: 34.5 GB)
| Action | Files | Space |
|--------|-------|-------|
| Remove duplicates of "project_final_v2.mp4" | 4 copies | 16.8 GB |
| Remove duplicates of "presentation_recording.mov" | 3 copies | 9.2 GB |
| Remove duplicates of "tutorial_backup.mp4" | 5 copies | 8.5 GB |

### 2. Archive Legacy Documents (Impact: 12.3 GB)
567 documents not accessed in >1 year
Recommendation: Move to cold storage

### 3. Clean Cache/Temp (Impact: 8.9 GB)
| Directory | Size |
|-----------|------|
| .cache/ | 4.2 GB |
| node_modules/ (orphaned) | 3.1 GB |
| __pycache__/ | 1.6 GB |

## Execution Checklist
- [ ] Review duplicate groups before deletion
- [ ] Backup unique files from duplicate groups
- [ ] Execute deletions in order of impact
- [ ] Verify space recovered
- [ ] Update baseline for next audit
```

---

## Exemplo 7: Modo Verbose/Debug

### Cenário
Troubleshooting de problema específico.

### Execução
```
/audit /path --verbose --log-level DEBUG
```

### Output Esperado
```
[DEBUG] 10:30:01 - Starting scan of /path
[DEBUG] 10:30:01 - Config: batch_size=1000, checkpoint_interval=1000
[INFO]  10:30:02 - Processing directory: /path/subdir1
[DEBUG] 10:30:02 - File: document.pdf (2.3 MB, modified 2024-11-15)
[DEBUG] 10:30:02 - File: image.png (450 KB, modified 2024-10-20)
[WARNING] 10:30:03 - Permission denied: /path/restricted/file.txt
[DEBUG] 10:30:03 - Skipped 1 file due to permissions
[INFO]  10:30:05 - Checkpoint saved: 1000 files processed
...
[INFO]  10:35:22 - Scan complete: 5,234 files in 5m21s
[DEBUG] 10:35:22 - Memory usage: 234 MB peak
[DEBUG] 10:35:22 - Errors: 3 permission, 0 encoding, 0 other
```

---

## Comandos Rápidos de Referência

| Comando | Descrição |
|---------|-----------|
| `/audit /path` | Auditoria completa padrão |
| `/audit /path --quick` | Apenas scan + resumo |
| `/audit /path --dedup-only` | Foco em duplicatas |
| `/audit --resume` | Retomar do checkpoint |
| `/audit --status` | Ver progresso atual |
| `/audit --report last` | Abrir último relatório |
