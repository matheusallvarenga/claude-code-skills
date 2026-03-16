# /audit Command

Execute o ITM Audit System para análise forense de arquivos.

## Uso

```
/audit [fonte] [opções]
```

## Parâmetros

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `fonte` | Diretório ou fonte de dados | `/path/to/folder`, `gdrive`, `external` |
| `--quick` | Apenas scan + resumo rápido | |
| `--dedup-only` | Foco apenas em duplicatas | |
| `--resume` | Retomar do último checkpoint | |
| `--status` | Ver progresso atual | |

## Fontes Pré-configuradas

| Alias | Path |
|-------|------|
| `gdrive` | Google Drive do usuário |
| `external` | HD Externo montado |
| `downloads` | ~/Downloads |

## Fluxo de Execução

1. **SCAN** — Varredura recursiva com metadados
2. **HASH** — Fingerprinting SHA-256 (64KB chunk + size)
3. **ANALYZE** — Classificação por tipo/idade/duplicatas
4. **REPORT** — Geração de relatórios Markdown

## Skill Associada

Este command utiliza a skill `itm-audit` localizada em:
```
.claude/skills/itm-audit/
```

## Constraints

- **READ-ONLY**: Nunca modifica arquivos fonte
- **Checkpoints**: Salvos a cada 1000 arquivos
- **Output**: `Projects/itm-audit/audit-reports/`

## Exemplos

```bash
# Auditoria completa de Downloads
/audit ~/Downloads

# Scan rápido do Google Drive
/audit gdrive --quick

# Retomar auditoria interrompida
/audit --resume

# Foco em duplicatas de HD externo
/audit /Volumes/External --dedup-only
```

## Referências

- [SKILL.md](../skills/itm-audit/SKILL.md)
- [Fases](../skills/itm-audit/docs/phases.md)
- [Algoritmos](../skills/itm-audit/docs/algorithms.md)
- [Troubleshooting](../skills/itm-audit/docs/troubleshooting.md)
