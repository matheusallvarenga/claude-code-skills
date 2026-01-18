# Agent Routing

Lógica de seleção de agentes especializados baseada no tipo de tarefa.

> **Fonte**: `Automation/agents/AGENTS-CATALOG.md`
> **Total**: 27 agentes disponíveis

---

## 1. Mapa de Agentes por Categoria

### 1.1 Development (6 agentes)

| Agente | Modelo | Quando Usar | Triggers |
|--------|--------|-------------|----------|
| `fullstack-developer` | Opus | Projetos completos, APIs + frontend | "criar app", "full stack", "end-to-end" |
| `frontend-developer` | Sonnet | UI/UX, React, Next.js, Tailwind | "frontend", "react", "componente", "UI" |
| `backend-architect` | Opus | Arquitetura, microservices, databases | "arquitetura", "microservice", "escalar" |
| `code-reviewer` | Sonnet | Code review, best practices, security | "revisar código", "code review", "melhorar" |
| `task-decomposition-expert` | Sonnet | Quebrar tarefas complexas | "decompor", "dividir tarefa", "planejar" |
| `prompt-engineer` | Opus | Otimização de prompts LLM | "prompt", "otimizar prompt", "LLM" |

**Seleção automática**:
```yaml
if task.involves_coding AND task.complexity > 0.7:
  if task.is_full_project:
    return "fullstack-developer"
  elif task.is_frontend_only:
    return "frontend-developer"
  elif task.is_architecture:
    return "backend-architect"
  elif task.is_review:
    return "code-reviewer"
```

### 1.2 Research (4 agentes)

| Agente | Modelo | Quando Usar | Triggers |
|--------|--------|-------------|----------|
| `competitive-intelligence-analyst` | Sonnet | Análise de concorrência, SWOT | "concorrente", "competidor", "mercado", "SWOT" |
| `market-research-analyst` | Sonnet | Pesquisa de mercado, tendências | "pesquisa de mercado", "tendência", "indústria" |
| `seo-analyzer` | Sonnet | Auditoria SEO, otimização | "SEO", "ranking", "otimização busca" |
| `sales-automator` | Sonnet | Automação de vendas, emails | "vendas", "cold email", "outreach", "lead" |

**Seleção automática**:
```yaml
if task.category == "research":
  if "competitor" in task.keywords:
    return "competitive-intelligence-analyst"
  elif "market" in task.keywords:
    return "market-research-analyst"
  elif "seo" in task.keywords:
    return "seo-analyzer"
  elif "sales" in task.keywords:
    return "sales-automator"
```

### 1.3 Content (6 agentes)

| Agente | Modelo | Quando Usar | Triggers |
|--------|--------|-------------|----------|
| `podcast-content-analyzer` | Opus | Análise de episódios, momentos virais | "podcast", "episódio", "transcrição" |
| `podcast-metadata-specialist` | Sonnet | Metadados, show notes, SEO | "show notes", "metadados podcast" |
| `podcast-trend-scout` | Sonnet | Tendências, tópicos emergentes | "tendência podcast", "tópico quente" |
| `social-media-copywriter` | Sonnet | Conteúdo para redes sociais | "twitter", "linkedin", "instagram", "post" |
| `content-curator` | Sonnet | Curadoria, qualidade de conteúdo | "curar", "organizar conteúdo", "qualidade" |
| `video-editor` | Opus | Edição de vídeo, FFmpeg | "vídeo", "cortar", "editar vídeo", "ffmpeg" |

**Seleção automática**:
```yaml
if task.category == "content":
  if "podcast" in task.keywords:
    if task.is_analysis:
      return "podcast-content-analyzer"
    elif task.is_metadata:
      return "podcast-metadata-specialist"
    else:
      return "podcast-trend-scout"
  elif "social" in task.keywords:
    return "social-media-copywriter"
  elif "video" in task.keywords:
    return "video-editor"
  else:
    return "content-curator"
```

### 1.4 PKM/Obsidian (5 agentes)

| Agente | Modelo | Quando Usar | Triggers |
|--------|--------|-------------|----------|
| `connection-agent` | Sonnet | Links entre notas, knowledge graph | "conectar notas", "links", "relacionar" |
| `moc-agent` | Sonnet | Maps of Content, navegação | "MOC", "mapa de conteúdo", "índice" |
| `metadata-agent` | Sonnet | Frontmatter, metadados | "metadata", "frontmatter", "propriedades" |
| `tag-agent` | Sonnet | Taxonomia de tags | "tags", "taxonomia", "categorizar" |
| `review-agent` | Sonnet | Quality assurance do vault | "revisar vault", "qualidade notas" |

**Seleção automática**:
```yaml
if task.involves_obsidian OR task.involves_pkm:
  if "link" in task.keywords OR "connect" in task.keywords:
    return "connection-agent"
  elif "moc" in task.keywords OR "index" in task.keywords:
    return "moc-agent"
  elif "metadata" in task.keywords OR "frontmatter" in task.keywords:
    return "metadata-agent"
  elif "tag" in task.keywords:
    return "tag-agent"
  elif "review" in task.keywords OR "quality" in task.keywords:
    return "review-agent"
```

### 1.5 Design (4 agentes)

| Agente | Modelo | Quando Usar | Triggers |
|--------|--------|-------------|----------|
| `cli-ui-designer` | Sonnet | Interfaces de terminal | "CLI", "terminal UI", "TUI" |
| `ui-ux-designer` | Sonnet | Design de interfaces web/mobile | "UI", "UX", "design interface", "wireframe" |
| `visual-analysis-ocr` | Sonnet | Extração de texto de imagens | "OCR", "extrair texto", "imagem para texto" |
| `timestamp-precision-specialist` | Sonnet | Timestamps precisos para edição | "timestamp", "cut point", "precisão" |

**Seleção automática**:
```yaml
if task.category == "design":
  if "cli" in task.keywords OR "terminal" in task.keywords:
    return "cli-ui-designer"
  elif "ocr" in task.keywords OR "image text" in task.keywords:
    return "visual-analysis-ocr"
  elif "timestamp" in task.keywords:
    return "timestamp-precision-specialist"
  else:
    return "ui-ux-designer"
```

### 1.6 Utility (2 agentes)

| Agente | Modelo | Quando Usar | Triggers |
|--------|--------|-------------|----------|
| `context-manager` | Opus | Gestão de contexto multi-agente | "contexto", "sessão longa", "preservar estado" |
| `seo-podcast-optimizer` | Sonnet | SEO específico para podcasts | "SEO podcast", "otimizar podcast" |

---

## 2. Matriz de Decisão

### 2.1 Por Complexidade

| Complexity Score | Agentes Recomendados | Modelo |
|------------------|---------------------|--------|
| 0.0 - 0.3 | Não usar agente (executar direto) | Haiku |
| 0.3 - 0.5 | Agentes Sonnet (tarefas focadas) | Sonnet |
| 0.5 - 0.7 | Agentes Sonnet (tarefas complexas) | Sonnet |
| 0.7 - 1.0 | Agentes Opus (análise profunda) | Opus |

### 2.2 Por Tipo de Output

| Output Esperado | Agente Categoria | Exemplo |
|-----------------|------------------|---------|
| Código | Development | fullstack-developer, frontend-developer |
| Documento | Content/Research | content-curator, market-research-analyst |
| Análise | Research | competitive-intelligence-analyst |
| Design | Design | ui-ux-designer, cli-ui-designer |
| Organização | PKM | connection-agent, tag-agent |

### 2.3 Por Urgência

| Urgência | Estratégia |
|----------|------------|
| Alta | Usar agente Sonnet mais próximo, evitar Opus |
| Normal | Seguir routing padrão |
| Baixa | Pode usar Opus para melhor qualidade |

---

## 3. Regras de Seleção

### 3.1 Regra: Especialista > Generalista

```yaml
rule: prefer_specialist
description: "Sempre preferir agente especializado ao invés de execução direta"
condition: task.has_specialized_agent
action: invoke_specialist
example:
  task: "Criar componente React"
  wrong: executar diretamente
  right: invocar frontend-developer
```

### 3.2 Regra: Modelo Apropriado

```yaml
rule: match_model_to_complexity
description: "Usar modelo do agente apropriado à complexidade"
conditions:
  - if complexity < 0.5: prefer Sonnet agents
  - if complexity >= 0.7: prefer Opus agents
  - if cost_sensitive: prefer Sonnet even for complex
```

### 3.3 Regra: Combinação de Agentes

```yaml
rule: agent_combination
description: "Tarefas complexas podem requerer múltiplos agentes"
example:
  task: "Criar landing page com copy otimizado"
  agents:
    - frontend-developer (implementação)
    - social-media-copywriter (copy)
    - seo-analyzer (otimização)
  execution: sequential ou parallel conforme dependências
```

---

## 4. Fallback Logic

### 4.1 Agente Indisponível

```yaml
fallback_chain:
  fullstack-developer:
    - frontend-developer + backend-architect (split)
    - general execution with Opus

  frontend-developer:
    - fullstack-developer
    - general execution with Sonnet

  code-reviewer:
    - fullstack-developer (review mode)
    - general execution with review prompt
```

### 4.2 Modelo Indisponível

```yaml
model_fallback:
  opus_unavailable:
    - downgrade to sonnet
    - warn user about quality tradeoff

  sonnet_unavailable:
    - upgrade to opus (if allowed)
    - downgrade to haiku (for simple tasks)
```

---

## 5. Métricas de Performance

### 5.1 Por Agente

```yaml
track_per_agent:
  - invocation_count
  - success_rate
  - avg_completion_time
  - avg_tokens_used
  - user_satisfaction (se disponível)
```

### 5.2 Otimização Contínua

Usar métricas para:
- Ajustar triggers de seleção
- Identificar agentes subutilizados
- Detectar padrões de fallback frequente
- Recomendar novos agentes para gaps identificados

---

## 6. Integração com LimitlessAgent

### 6.1 Quando Escalar para LimitlessAgent

```yaml
escalate_to_limitless:
  conditions:
    - complexity > 0.7 AND task.is_multi_step
    - task.requires_persistence
    - task.estimated_duration > 30min
    - task.requires_multiple_agents_coordinated
```

### 6.2 Handoff Protocol

```yaml
handoff:
  from: request-optimizer
  to: limitless-agent
  payload:
    - original_request
    - analysis_result (5-point)
    - recommended_agents[]
    - complexity_score
    - estimated_subtasks[]
```

---

## 7. Changelog

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0.0 | 2026-01-18 | Criação com 27 agentes mapeados |

---

**Fonte de Verdade**: `Automation/agents/AGENTS-CATALOG.md`
**Última atualização**: 2026-01-18
