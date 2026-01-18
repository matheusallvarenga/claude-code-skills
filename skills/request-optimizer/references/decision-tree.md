# Decision Tree: Integrated Resource Routing

Árvore de decisão expandida integrando todos os recursos disponíveis.

> **Versão**: 2.0.0
> **Integra**: agent-routing.md, skill-routing.md, mcp-routing.md, complexity-scoring.md

---

## 1. Fluxo Principal

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         USER REQUEST                                     │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHASE 1: ANALYSIS (5 Points)                          │
├─────────────────────────────────────────────────────────────────────────┤
│ 1. Specificity Assessment                                                │
│ 2. Exploration Detection                                                 │
│ 3. Subtask Identification                                               │
│ 4. Tool Coordination                                                    │
│ 5. Model Recommendation                                                 │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHASE 2: COMPLEXITY SCORING                           │
├─────────────────────────────────────────────────────────────────────────┤
│ Calculate: scope + depth + ambiguity + tooling + duration               │
│ Result: 0.0 (trivial) → 1.0 (máxima complexidade)                       │
│ See: references/complexity-scoring.md                                   │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHASE 3: RESOURCE SELECTION                           │
├─────────────────────────────────────────────────────────────────────────┤
│ ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│ │   SKILL?    │  │    MCP?     │  │   AGENT?    │  │   MODEL?    │    │
│ │ skill-      │  │ mcp-        │  │ agent-      │  │ complexity- │    │
│ │ routing.md  │  │ routing.md  │  │ routing.md  │  │ scoring.md  │    │
│ └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘    │
│        └─────────────────┴─────────────────┴─────────────────┘          │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHASE 4: EXECUTION ROUTING                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   Complexity < 0.3?  ─────────────────────────→  DIRECT EXECUTION       │
│         │                                         (Haiku, no agent)      │
│         │                                                                │
│   Complexity 0.3-0.7? ─────────────────────────→  AGENT EXECUTION       │
│         │                                         (Sonnet, specialized)  │
│         │                                                                │
│   Complexity > 0.7? ───────────────────────────→  LIMITLESS/OPUS        │
│                                                   (NZT Protocol)         │
│                                                                          │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ↓
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHASE 5: APPROVAL & EXECUTE                           │
├─────────────────────────────────────────────────────────────────────────┤
│ Present recommendation → Get approval → Execute → Report results        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Decision Rules (Expandidas)

### Rule 1: Specificity Gate

```yaml
rule: specificity_gate
priority: 1
condition: request.specificity_score < 0.5
actions:
  - if request.allows_exploration:
      recommend: "Explore Agent"
      approval: REQUIRED
  - else:
      recommend: "Ask clarification"
      questions:
        - "Qual arquivo/função específica?"
        - "Qual o resultado esperado?"
```

### Rule 2: Skill Detection

```yaml
rule: skill_detection
priority: 2
condition: request.matches_skill_trigger
reference: skill-routing.md
actions:
  - match request.file_type:
      ".pdf": invoke skill "pdf"
      ".docx": invoke skill "docx"
      ".xlsx": invoke skill "xlsx"
      ".pptx": invoke skill "pptx"
  - match request.keywords:
      ["notion", "page", "database"]: invoke skill "notion-*"
      ["teste", "playwright"]: invoke skill "webapp-testing"
      ["arte", "generativo"]: invoke skill "algorithmic-art"
```

### Rule 3: MCP Detection

```yaml
rule: mcp_detection
priority: 3
condition: request.needs_external_integration
reference: mcp-routing.md
actions:
  - match request.service:
      "notion": activate MCP "notion"
      "supabase" | "database": activate MCP "supabase"
      "github" | "repo": activate MCP "github"
      "deploy" | "vercel": activate MCP "vercel"
      "figma" | "design": activate MCP "figma-desktop"
  - if request.needs_docs:
      activate MCP "context7"
```

### Rule 4: Agent Selection

```yaml
rule: agent_selection
priority: 4
condition: request.complexity >= 0.3
reference: agent-routing.md
actions:
  - match request.category:
      "development":
        - if request.is_full_project: "fullstack-developer"
        - if request.is_frontend: "frontend-developer"
        - if request.is_architecture: "backend-architect"
        - if request.is_review: "code-reviewer"
      "research":
        - if "competitor" in keywords: "competitive-intelligence-analyst"
        - if "market" in keywords: "market-research-analyst"
        - if "seo" in keywords: "seo-analyzer"
      "content":
        - if "podcast" in keywords: "podcast-content-analyzer"
        - if "social" in keywords: "social-media-copywriter"
        - if "video" in keywords: "video-editor"
      "pkm":
        - if "link" in keywords: "connection-agent"
        - if "moc" in keywords: "moc-agent"
        - if "tag" in keywords: "tag-agent"
      "design":
        - if "cli" in keywords: "cli-ui-designer"
        - if "ui" in keywords: "ui-ux-designer"
```

### Rule 5: Model Selection

```yaml
rule: model_selection
priority: 5
reference: complexity-scoring.md
actions:
  - if complexity < 0.3:
      model: "haiku"
      reason: "Tarefa simples, otimizar custo"
  - if complexity >= 0.3 AND complexity < 0.7:
      model: "sonnet"
      reason: "Equilíbrio custo/qualidade"
  - if complexity >= 0.7:
      model: "opus"
      reason: "Tarefa complexa requer raciocínio profundo"
      approval: REQUIRED (custo elevado)
```

### Rule 6: Subtask Decomposition

```yaml
rule: subtask_decomposition
priority: 6
condition: request.has_multiple_outcomes OR complexity > 0.5
actions:
  - identify subtasks
  - create TodoWrite list
  - sequence by dependencies
  - approval: REQUIRED for 5+ subtasks
```

### Rule 7: LimitlessAgent Escalation

```yaml
rule: limitless_escalation
priority: 7
condition:
  - complexity > 0.7 AND request.is_multi_step
  - OR complexity > 0.5 AND request.requires_persistence
  - OR complexity > 0.8
  - OR request.estimated_duration > 30min
actions:
  - recommend: "Invocar LimitlessAgent (NZT Protocol)"
  - approval: REQUIRED
  - handoff: IExecutionPlan
```

---

## 3. Approval Gates

### Always Require Approval

| Ação | Razão | Risco |
|------|-------|-------|
| Invocar Explore Agent | Token cost | Médio |
| Invocar qualquer Agent (Task tool) | Token cost | Médio |
| Usar modelo Opus | Custo elevado | Alto |
| Executar LimitlessAgent | Autonomia, custo | Alto |
| MCP write operations | Modificação de dados | Médio |
| Multi-step workflows (5+ tasks) | Complexidade | Médio |
| Operações de delete | Irreversível | Alto |

### Safe Without Approval

| Ação | Razão |
|------|-------|
| Analisar request | Apenas raciocínio |
| Recomendar estratégia | Não executa nada |
| Ler arquivos | Read-only |
| Sugerir /clear, /compact | Otimização |
| Edições simples (1 arquivo, escopo claro) | Baixo risco |
| MCP read operations | Read-only |

---

## 4. Resource Combination Matrix

### Skill + Agent

| Tarefa | Skill | Agent | Ordem |
|--------|-------|-------|-------|
| Criar doc de arquitetura | docx | backend-architect | agent → skill |
| Landing page responsiva | frontend-design | frontend-developer | skill → agent |
| Relatório de mercado | xlsx + docx | market-research-analyst | agent → skills |
| Apresentação de produto | pptx | sales-automator | agent → skill |

### Skill + MCP

| Tarefa | Skill | MCP | Ordem |
|--------|-------|-----|-------|
| Sync Notion → Word | docx | notion | mcp read → skill write |
| Dashboard de dados | xlsx | supabase | mcp query → skill format |
| Doc de API | docx | github | mcp read → skill format |

### Agent + MCP

| Tarefa | Agent | MCP | Ordem |
|--------|-------|-----|-------|
| Análise de repo | code-reviewer | github | mcp read → agent analyze |
| Pesquisa com dados | market-research-analyst | supabase | mcp query → agent analyze |
| Deploy de projeto | fullstack-developer | vercel | agent build → mcp deploy |

---

## 5. Execution Paths

### Path A: Direct Execution (Complexity < 0.3)

```
Request → Analyze → Score: 0.2 → No agent needed
    ↓
Select Haiku → Execute directly → Report
```

### Path B: Agent Execution (Complexity 0.3 - 0.7)

```
Request → Analyze → Score: 0.5 → Select agent
    ↓
Match category → frontend-developer (Sonnet)
    ↓
Ask approval → Invoke Task tool → Report
```

### Path C: LimitlessAgent (Complexity > 0.7)

```
Request → Analyze → Score: 0.85 → Escalate
    ↓
Create IExecutionPlan → Ask approval
    ↓
Handoff to LimitlessAgent (NZT Protocol)
    ↓
Monitor → Report when complete
```

---

## 6. Error Handling

### Resource Unavailable

```yaml
fallback_strategy:
  skill_unavailable:
    - try equivalent agent
    - if no agent: execute directly with appropriate model

  agent_unavailable:
    - try related agent from same category
    - if no alternative: execute directly with Opus

  mcp_unavailable:
    - try fetch MCP if read-only
    - if write needed: report error, suggest manual action

  model_unavailable:
    - follow fallback chain: Claude → Ollama → Gemini → ChatGPT
```

### Execution Failed

```yaml
on_failure:
  - log error with context
  - if recoverable:
      - attempt recovery action
      - retry with different resource
  - if not recoverable:
      - report to user with diagnostics
      - suggest alternatives
```

---

## 7. Metrics Collection

```yaml
collect_per_decision:
  - complexity_score
  - resources_selected (skills, agents, mcps, model)
  - approval_required
  - execution_path (direct | agent | limitless)
  - outcome (success | partial | failed)
  - actual_cost
  - actual_duration
```

---

## 8. Execution Checklist

Before presenting recommendation:

- [ ] Analysis complete (5 points)
- [ ] Complexity score calculated
- [ ] Skill routing checked (skill-routing.md)
- [ ] MCP routing checked (mcp-routing.md)
- [ ] Agent routing checked (agent-routing.md)
- [ ] Model selected (complexity-scoring.md)
- [ ] Approval gates identified
- [ ] Fallbacks defined
- [ ] Estimated cost/duration (if applicable)

---

## 9. Post-Execution

After approval and execution:

1. Execute recommended strategy
2. Track metrics
3. Report results concisely
4. If multi-step: update progress via TodoWrite
5. If LimitlessAgent: monitor and report iterations
6. Ask: "Tarefa completa. Algo mais?"

---

## 10. Changelog

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0.0 | 2025-11-07 | Criação original (POC) |
| 2.0.0 | 2026-01-18 | Integração completa com routing files |

---

**Referências**:
- `references/agent-routing.md`
- `references/skill-routing.md`
- `references/mcp-routing.md`
- `references/complexity-scoring.md`
- `references/resource-registry.md`
- `references/integration-interfaces.md`
