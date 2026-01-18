# Skill Routing

Lógica de seleção de skills baseada no tipo de tarefa e padrões de invocação.

> **Fonte**: `.claude/skills/`
> **Total**: 27 skills disponíveis

---

## 1. Mapa de Skills por Categoria

### 1.1 Documents (5 skills)

| Skill | Trigger | Quando Usar | File Types |
|-------|---------|-------------|------------|
| `docx` | `/docx` | Criar/editar documentos Word | .docx |
| `pdf` | `/pdf` | Manipular PDFs (extrair, merge, forms) | .pdf |
| `pptx` | `/pptx` | Criar/editar apresentações | .pptx |
| `xlsx` | `/xlsx` | Trabalhar com planilhas | .xlsx, .csv |
| `doc-coauthoring` | `/doc-coauthoring` | Edição colaborativa de documentos | qualquer |

**Seleção automática**:
```yaml
if task.involves_file:
  match task.file_extension:
    ".docx" | ".doc": return "docx"
    ".pdf": return "pdf"
    ".pptx" | ".ppt": return "pptx"
    ".xlsx" | ".xls" | ".csv": return "xlsx"

if task.is_collaborative_editing:
  return "doc-coauthoring"
```

### 1.2 Notion Integration (4 skills)

| Skill | Trigger | Quando Usar |
|-------|---------|-------------|
| `notion-spec-to-implementation` | - | Converter specs em tasks |
| `notion-meeting-intelligence` | - | Preparar materiais de reunião |
| `notion-research-documentation` | - | Documentar pesquisas |
| `notion-knowledge-capture` | - | Capturar conhecimento de conversas |

**Seleção automática**:
```yaml
if task.involves_notion:
  if task.is_spec_conversion:
    return "notion-spec-to-implementation"
  elif task.is_meeting_prep:
    return "notion-meeting-intelligence"
  elif task.is_research:
    return "notion-research-documentation"
  elif task.is_knowledge_capture:
    return "notion-knowledge-capture"
```

### 1.3 Design & Creative (5 skills)

| Skill | Trigger | Quando Usar |
|-------|---------|-------------|
| `algorithmic-art` | - | Arte generativa com p5.js |
| `canvas-design` | - | Design visual para PDF/PNG |
| `theme-factory` | - | Aplicar temas profissionais |
| `brand-guidelines` | - | Identidade de marca Anthropic |
| `frontend-design` | `/frontend-design` | Padrões UI/UX para web |

**Seleção automática**:
```yaml
if task.category == "design":
  if task.is_generative_art:
    return "algorithmic-art"
  elif task.is_visual_design:
    return "canvas-design"
  elif task.needs_theming:
    return "theme-factory"
  elif task.is_brand_related:
    return "brand-guidelines"
  elif task.is_web_ui:
    return "frontend-design"
```

### 1.4 Development & Testing (5 skills)

| Skill | Trigger | Quando Usar |
|-------|---------|-------------|
| `mcp-builder` | - | Criar MCP servers |
| `webapp-testing` | `/webapp-testing` | Testes com Playwright |
| `web-artifacts-builder` | - | Criar artefatos web interativos |
| `full-stack-project-finisher` | - | Finalizar projetos 70-100% |
| `skill-creator` | - | Criar novas skills |

**Seleção automática**:
```yaml
if task.category == "development":
  if task.is_mcp_creation:
    return "mcp-builder"
  elif task.is_testing:
    return "webapp-testing"
  elif task.is_artifact_creation:
    return "web-artifacts-builder"
  elif task.is_project_finishing:
    return "full-stack-project-finisher"
  elif task.is_skill_creation:
    return "skill-creator"
```

### 1.5 Research & Content (4 skills)

| Skill | Trigger | Quando Usar |
|-------|---------|-------------|
| `content-research-writer` | - | Pesquisa e escrita de conteúdo |
| `lead-research-assistant` | - | Pesquisa de leads |
| `request-optimizer` | - | Otimização de requests (meta) |
| `internal-comms` | - | Comunicações internas |

**Seleção automática**:
```yaml
if task.category == "research":
  if task.is_content_writing:
    return "content-research-writer"
  elif task.is_lead_research:
    return "lead-research-assistant"
  elif task.is_internal_comm:
    return "internal-comms"
```

### 1.6 Learning & Productivity (3 skills)

| Skill | Trigger | Quando Usar |
|-------|---------|-------------|
| `github-for-beginners` | - | Ensinar GitHub |
| `vs-code-for-beginners` | - | Ensinar VS Code |
| `video-downloader` | - | Download de vídeos |

**Seleção automática**:
```yaml
if task.is_learning:
  if "github" in task.topic:
    return "github-for-beginners"
  elif "vscode" in task.topic:
    return "vs-code-for-beginners"

if task.is_video_download:
  return "video-downloader"
```

### 1.7 Audit (1 skill)

| Skill | Trigger | Quando Usar |
|-------|---------|-------------|
| `itm-audit` | `/audit` | Auditoria de dados forense |

---

## 2. Matriz de Decisão

### 2.1 Por Padrão de Arquivo

| Padrão | Skill |
|--------|-------|
| `*.docx`, `*.doc` | docx |
| `*.pdf` | pdf |
| `*.pptx`, `*.ppt` | pptx |
| `*.xlsx`, `*.xls`, `*.csv` | xlsx |
| `*.ipynb` | (usar Read tool nativo) |

### 2.2 Por Keyword

| Keywords | Skill Provável |
|----------|---------------|
| "criar documento", "word" | docx |
| "pdf", "extrair pdf", "merge pdf" | pdf |
| "apresentação", "slides" | pptx |
| "planilha", "excel", "csv" | xlsx |
| "notion", "page", "database" | notion-* |
| "teste", "playwright", "e2e" | webapp-testing |
| "arte", "generativo", "p5" | algorithmic-art |
| "tema", "estilo" | theme-factory |

### 2.3 Por Contexto

| Contexto | Skills Aplicáveis |
|----------|-------------------|
| Trabalhando com Notion | notion-* skills |
| Criando conteúdo visual | canvas-design, algorithmic-art |
| Desenvolvendo MCP | mcp-builder |
| Finalizando projeto | full-stack-project-finisher |
| Ensinando iniciante | github-for-beginners, vs-code-for-beginners |

---

## 3. Regras de Seleção

### 3.1 Regra: File Type Priority

```yaml
rule: file_type_determines_skill
description: "Se tarefa envolve arquivo, usar skill correspondente"
priority: HIGH
condition: task.has_file_reference
action: select_by_file_extension
```

### 3.2 Regra: Explicit Trigger

```yaml
rule: explicit_trigger_wins
description: "Se usuário usou /skill, respeitar escolha"
priority: HIGHEST
condition: task.starts_with_slash_command
action: invoke_requested_skill
```

### 3.3 Regra: Context Inference

```yaml
rule: infer_from_context
description: "Se não há trigger explícito, inferir do contexto"
priority: MEDIUM
condition: NOT task.has_explicit_trigger
action: analyze_keywords_and_context
```

---

## 4. Combinação Skill + Agent

Algumas tarefas beneficiam de skill + agent:

| Tarefa | Skill | Agent |
|--------|-------|-------|
| Criar apresentação de mercado | pptx | market-research-analyst |
| Documentar arquitetura | docx | backend-architect |
| Criar landing page | frontend-design | frontend-developer |
| Gerar arte para podcast | algorithmic-art | podcast-metadata-specialist |

### 4.1 Ordem de Execução

```yaml
combination_execution:
  - if skill.provides_template AND agent.provides_content:
      order: [agent, skill]  # Agent gera conteúdo, skill formata

  - if skill.provides_tool AND agent.provides_expertise:
      order: [skill, agent]  # Skill prepara, agent executa
```

---

## 5. Fallback Logic

### 5.1 Skill Não Disponível

```yaml
fallback:
  docx_unavailable:
    - usar Write tool com markdown
    - converter depois se necessário

  pdf_unavailable:
    - usar WebFetch se URL
    - usar Read se arquivo local

  notion_skills_unavailable:
    - usar Notion MCP diretamente
    - exportar para markdown
```

### 5.2 Skill Falhou

```yaml
on_skill_failure:
  - log error
  - attempt with agent equivalent
  - if no agent: execute directly
  - notify user of degraded experience
```

---

## 6. Métricas de Performance

### 6.1 Por Skill

```yaml
track_per_skill:
  - invocation_count
  - success_rate
  - avg_execution_time
  - user_satisfaction
  - fallback_frequency
```

### 6.2 Padrões de Uso

Identificar:
- Skills mais usadas (otimizar)
- Skills nunca usadas (remover ou promover)
- Combinações frequentes (criar shortcuts)
- Falhas recorrentes (investigar)

---

## 7. Integração com LimitlessAgent

### 7.1 Skills como Tools

```yaml
limitless_integration:
  skills_as_tools: true
  description: "LimitlessAgent pode invocar skills como tools"
  example:
    goal: "Criar relatório trimestral"
    steps:
      - use xlsx skill para dados
      - use market-research-analyst para análise
      - use docx skill para documento final
      - use pdf skill para exportar
```

### 7.2 Skill Chaining

```yaml
skill_chain:
  name: "report_generation"
  steps:
    - skill: xlsx
      action: extract_data
    - skill: content-research-writer
      action: analyze
    - skill: docx
      action: format
    - skill: pdf
      action: export
```

---

## 8. Extensibilidade

### 8.1 Adicionando Nova Skill

1. Criar diretório em `.claude/skills/{nome}/`
2. Criar `SKILL.md` com definição
3. Adicionar entrada neste arquivo
4. Definir triggers e keywords
5. Testar invocação

### 8.2 Template de Entrada

```yaml
new_skill:
  name: "skill-name"
  trigger: "/skill-name"
  category: "categoria"
  keywords: ["keyword1", "keyword2"]
  file_types: [".ext1", ".ext2"]  # se aplicável
  when_to_use: "Descrição de quando usar"
  combination_with: ["agent1", "skill2"]  # se aplicável
```

---

## 9. Changelog

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0.0 | 2026-01-18 | Criação com 27 skills mapeadas |

---

**Fonte de Verdade**: `.claude/skills/`
**Última atualização**: 2026-01-18
