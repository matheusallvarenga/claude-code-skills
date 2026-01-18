# Resource Registry

Central de referências para todos os recursos disponíveis no ecossistema.

> **Princípio**: Este arquivo NÃO duplica catálogos existentes. Apenas referencia e define interfaces de acesso.

---

## 1. Fontes de Recursos

### 1.1 Agentes Especializados (27)

| Atributo | Valor |
|----------|-------|
| **Catálogo Principal** | `Automation/agents/AGENTS-CATALOG.md` |
| **Definições** | `.claude/agents/*.md` |
| **Total** | 27 agentes |
| **Routing Logic** | `references/agent-routing.md` |

**Categorias**:
- Development (6): fullstack, frontend, backend, code-reviewer, task-decomp, prompt-engineer
- Research (4): competitive-intel, market-research, seo-analyzer, sales-auto
- Content (6): podcast-*, social-media, content-curator, video-editor
- PKM (5): connection, moc, metadata, tag, review
- Design (4): cli-ui, ui-ux, timestamp-prec, visual-ocr
- Utility (2): context-manager, seo-podcast-optimizer

### 1.2 Skills (27)

| Atributo | Valor |
|----------|-------|
| **Localização** | `.claude/skills/` |
| **Total** | 27 skills |
| **Routing Logic** | `references/skill-routing.md` |

**Categorias**:
- Documents (5): docx, pdf, pptx, xlsx, doc-coauthoring
- Notion (4): spec-to-impl, meeting-intel, research-doc, knowledge-capture
- Design (5): algorithmic-art, canvas-design, theme-factory, brand-guidelines, frontend-design
- Development (5): mcp-builder, webapp-testing, web-artifacts-builder, full-stack-finisher, skill-creator
- Research (4): content-research-writer, lead-research-assistant, request-optimizer, internal-comms
- Learning (3): github-for-beginners, vs-code-for-beginners, video-downloader
- Audit (1): itm-audit

### 1.3 MCP Servers (14)

| Atributo | Valor |
|----------|-------|
| **Catálogo Principal** | `Automation/mcps/MCP-CATALOG.md` |
| **Configuração** | `.claude/mcp.json` |
| **Total** | 14 MCPs |
| **Routing Logic** | `references/mcp-routing.md` |

**Categorias**:
- Cloud APIs (6): notion, supabase, figma-desktop, shadcn, context7, vercel
- Built-in (6): markitdown, memory, filesystem, github, fetch, context7
- Custom (1): obsidian-docs
- Development (1): genkit

### 1.4 LLM Providers

| Atributo | Valor |
|----------|-------|
| **Routing Diagram** | `Projects/LimitlessAgent/docs/diagrams/llm-routing.md` |
| **Architecture** | `Projects/LimitlessAgent/docs/ARCHITECTURE.md` |
| **Routing Logic** | `references/complexity-scoring.md` |

**Providers Disponíveis**:
- Claude (Haiku, Sonnet, Opus) - Primary
- Ollama (local) - Secondary fallback
- Gemini Pro - Tertiary fallback
- ChatGPT - Quaternary fallback

---

## 2. Interfaces de Acesso

### 2.1 Interface: Agent Selection

```yaml
interface: AgentSelection
input:
  task_type: string        # development, research, content, pkm, design, utility
  complexity: float        # 0.0 - 1.0
  specific_need: string    # opcional, para match mais preciso
output:
  recommended_agent: string
  model: string            # sonnet | opus
  confidence: float
  alternatives: list
```

### 2.2 Interface: Skill Selection

```yaml
interface: SkillSelection
input:
  task_category: string    # documents, notion, design, development, research, learning, audit
  file_type: string        # opcional (pdf, docx, xlsx, etc.)
  context: string          # descrição da tarefa
output:
  recommended_skill: string
  trigger_pattern: string
  confidence: float
```

### 2.3 Interface: MCP Selection

```yaml
interface: MCPSelection
input:
  integration_needed: string  # notion, supabase, github, etc.
  operation_type: string      # read, write, query, deploy
output:
  recommended_mcp: string
  connection_type: string     # cloud | local | built-in
  requires_auth: boolean
```

### 2.4 Interface: Model Selection

```yaml
interface: ModelSelection
input:
  complexity_score: float  # 0.0 - 1.0
  cost_sensitivity: string # low | medium | high
  latency_requirement: string # fast | normal | slow_ok
output:
  recommended_model: string
  provider: string
  estimated_cost: string
  fallback_chain: list
```

---

## 3. Regras de Resolução

### 3.1 Prioridade de Recursos

```
1. Verificar se tarefa requer SKILL específica (file type, pattern match)
2. Verificar se tarefa requer MCP (integração externa)
3. Verificar se tarefa requer AGENT especializado (complexidade, domínio)
4. Selecionar MODEL baseado em complexity score
5. Aplicar fallback se recurso primário indisponível
```

### 3.2 Conflito de Recursos

Quando múltiplos recursos são aplicáveis:

```yaml
resolution_rules:
  - rule: "skill_over_agent"
    condition: "Tarefa tem skill dedicada"
    action: "Usar skill, agente como backup"

  - rule: "agent_over_direct"
    condition: "Tarefa é complexa (>0.5) e tem agente especializado"
    action: "Invocar agente ao invés de executar diretamente"

  - rule: "mcp_required"
    condition: "Tarefa requer dados externos"
    action: "MCP é obrigatório, combinar com skill/agent"
```

### 3.3 Fallback Chain

```
Skill falhou → Tentar com Agent especializado
Agent falhou → Tentar execução direta com Model apropriado
Model primário falhou → Seguir fallback chain (Ollama → Gemini → ChatGPT)
Todos falharam → Reportar erro com diagnóstico
```

---

## 4. Extensibilidade

### 4.1 Adicionando Novo Agente

1. Criar arquivo em `.claude/agents/{nome}.md`
2. Atualizar `Automation/agents/AGENTS-CATALOG.md`
3. Adicionar entrada em `references/agent-routing.md`
4. Testar com request de exemplo

### 4.2 Adicionando Nova Skill

1. Criar diretório em `.claude/skills/{nome}/`
2. Criar `SKILL.md` com definição
3. Adicionar entrada em `references/skill-routing.md`
4. Testar invocação via `/nome`

### 4.3 Adicionando Novo MCP

1. Adicionar configuração em `.claude/mcp.json`
2. Atualizar `Automation/mcps/MCP-CATALOG.md`
3. Adicionar entrada em `references/mcp-routing.md`
4. Testar conexão e operações

### 4.4 Adicionando Novo LLM Provider

1. Atualizar `Projects/LimitlessAgent/docs/diagrams/llm-routing.md`
2. Adicionar na fallback chain em `references/complexity-scoring.md`
3. Configurar credenciais se necessário
4. Testar roteamento

---

## 5. Integração Futura: LimitlessAgent

### 5.1 Conexão Planejada

```
request-optimizer (análise)
        ↓
    complexity > 0.7?
        ↓
    YES → Invocar LimitlessAgent (NZT Protocol)
        ↓
    LimitlessAgent usa este Resource Registry para:
        - Agent routing
        - Model routing
        - MCP coordination
        - State persistence (Supabase)
```

### 5.2 Interfaces de Integração

Ver `references/integration-interfaces.md` para:
- `IRequestAnalysis` - Output do request-optimizer
- `IExecutionPlan` - Input para LimitlessAgent
- `IExecutionResult` - Output do LimitlessAgent
- `IStateManager` - Persistência cross-session

---

## 6. Métricas de Uso

### 6.1 Tracking Recomendado

```yaml
metrics:
  agent_usage:
    - agent_name
    - invocation_count
    - success_rate
    - avg_tokens

  skill_usage:
    - skill_name
    - trigger_pattern
    - invocation_count

  mcp_usage:
    - mcp_name
    - operation_type
    - latency_ms

  model_usage:
    - model_name
    - complexity_score
    - cost_usd
    - tokens_used
```

### 6.2 Otimização Baseada em Dados

Futuramente, usar métricas para:
- Ajustar thresholds de complexity scoring
- Identificar agentes subutilizados
- Otimizar fallback chain baseado em disponibilidade real
- Calcular ROI de cada recurso

---

## 7. Versionamento

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0.0 | 2026-01-18 | Criação inicial |

---

**Mantido por**: request-optimizer skill
**Última atualização**: 2026-01-18
