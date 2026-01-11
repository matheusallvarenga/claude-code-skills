# Fases do Sistema de Auditoria

## Fase 1: SCAN (Varredura)

### Objetivo
Coletar metadados completos de todos os arquivos nas fontes definidas.

### Processo
1. Receber lista de diretórios raiz
2. Varredura recursiva respeitando symlinks
3. Captura de metadados por arquivo:
   - Path completo
   - Nome e extensão
   - Tamanho em bytes
   - Data de criação
   - Data de modificação
   - Data de último acesso
   - Permissões

### Output
- `scan_results.json` - Dados estruturados
- `scan_summary.md` - Resumo executivo

### Checkpoints
- A cada 1000 arquivos processados
- Arquivo: `data/checkpoint_scan_{timestamp}.json`

---

## Fase 1.5: TREE (Estrutura Hierárquica) — Opcional

### Objetivo
Gerar mapa visual da estrutura de diretórios com estatísticas de tamanho.

### Processo
1. Percorrer árvore de diretórios até profundidade configurável
2. Calcular tamanho agregado por pasta
3. Identificar Top 10 maiores diretórios
4. Gerar visualização em formato árvore

### Parâmetros
- `max_depth`: Profundidade máxima (default: 4)
- `output_format`: 'json', 'markdown', ou 'both'
- `report_session_dir`: Diretório específico para o relatório MD (opcional, para integrar com sessão do reporter)

### Output
- `tree_structure.json` - Estrutura completa em JSON
- `tree_structure_{timestamp}.md` - Visualização Markdown

### Uso
Recomendado antes do HASH para:
- Entender distribuição de espaço
- Identificar diretórios prioritários
- Planejar exclusões (node_modules, .git, etc.)

---

## Fase 2: HASH (Fingerprinting)

### Objetivo
Calcular identificadores únicos para detecção de duplicatas.

### Algoritmo
1. Ler primeiros 64KB do arquivo
2. Calcular SHA-256 do chunk
3. Combinar com tamanho total para hash composto
4. Arquivos < 64KB: hash do conteúdo completo

### Otimizações
- Skip de arquivos já hasheados (cache)
- Processamento em batches de 100
- Priorização por tamanho (maiores primeiro)

### Output
- `hash_index.json` - Mapeamento path → hash
- Atualização do `scan_results.json`

---

## Fase 3: ANALYZE (Análise)

### Objetivo
Classificar arquivos e identificar padrões.

### Classificações

#### Por Tipo
| Categoria | Extensões |
|-----------|-----------|
| Documentos | .pdf, .doc, .docx, .txt, .md |
| Planilhas | .xls, .xlsx, .csv |
| Imagens | .jpg, .png, .gif, .webp, .svg |
| Vídeos | .mp4, .mov, .avi, .mkv |
| Áudio | .mp3, .wav, .m4a, .flac |
| Código | .py, .js, .ts, .json, .yaml |
| Arquivos | .zip, .rar, .7z, .tar |
| Outros | Demais extensões |

#### Por Idade
| Categoria | Critério |
|-----------|----------|
| Recente | < 30 dias |
| Ativo | 30-180 dias |
| Arquivado | 180-365 dias |
| Legacy | > 365 dias |

#### Por Duplicação
- Únicos
- Duplicados (2 cópias)
- Multi-duplicados (3+ cópias)

### Output
- `analysis_results.json`
- Grupos de duplicatas identificados

---

## Fase 4: REPORT (Relatórios)

### Objetivo
Gerar documentação acionável em Markdown.

### Relatórios Gerados

#### 1. Audit Report Principal
- Sumário executivo
- Estatísticas gerais
- Distribuição por tipo/idade
- Top 10 maiores arquivos
- Top 10 diretórios mais pesados

#### 2. Deduplication Report
- Total de espaço recuperável
- Grupos de duplicatas ordenados por impacto
- Recomendações de qual cópia manter

#### 3. Action Plan
- Ações prioritárias (Pareto)
- Estimativa de impacto
- Checklist de execução

### Destino
`Projects/itm-audit/audit-reports/{timestamp}/`
