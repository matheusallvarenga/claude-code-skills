# ITM-AUDIT Skill

## Descrição
Sistema de Auditoria de Dados v5 para análise forense de arquivos distribuídos em múltiplas fontes (Google Drive, HD Externo, Notion).

## Capacidades
- Varredura recursiva de diretórios com metadados completos
- Deduplicação via SHA-256 (hash dos primeiros 64KB + tamanho)
- Classificação por tipo, idade e padrões de uso
- Geração de relatórios Markdown estruturados
- Modo READ-ONLY garantido (nunca modifica arquivos fonte)

## Arquitetura

### Fases de Execução
1. **SCAN** - Varredura e coleta de metadados
2. **TREE** - Análise hierárquica de diretórios (opcional)
3. **HASH** - Cálculo de hashes para deduplicação
4. **ANALYZE** - Classificação e identificação de padrões
5. **REPORT** - Geração de relatórios e planos de ação

### Scripts Disponíveis
| Script | Função |
|--------|--------|
| `scanner.py` | Varredura recursiva com metadados |
| `tree_analyzer.py` | Análise hierárquica de diretórios |
| `hasher.py` | Cálculo SHA-256 otimizado |
| `dedup_engine.py` | Motor de identificação de duplicatas |
| `classifier.py` | Classificação por tipo/idade/padrão |
| `reporter.py` | Geração de relatórios Markdown |

## Uso

### Comando Rápido
```
/audit [fonte] [opções]
```

### Fluxo Completo
1. Definir fonte(s) de dados
2. Executar SCAN inicial
3. Processar HASH para deduplicação
4. Gerar ANALYZE com classificações
5. Produzir REPORT final

## Constraints
- **READ-ONLY**: Nunca modificar, mover ou deletar arquivos fonte
- **Checkpoints**: Salvar estado a cada 1000 arquivos processados
- **Output**: Apenas em `Projects/itm-audit/audit-reports/`

## Documentação
- [Fases Detalhadas](./docs/phases.md)
- [Algoritmos](./docs/algorithms.md)
- [Troubleshooting](./docs/troubleshooting.md)
- [Exemplos](./docs/examples.md)

## Integração
- **MCPs**: Obsidian, Notion (para relatórios)
- **Agents**: task-decomposition-expert, backend-architect
- **Output**: Markdown compatível com Obsidian
