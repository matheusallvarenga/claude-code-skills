# Complexity Scoring

Algoritmo para calcular a complexidade de uma tarefa e determinar o modelo/agente apropriado.

> **Fonte**: `Projects/LimitlessAgent/docs/diagrams/llm-routing.md`
> **Baseado em**: LimitlessAgent Architecture

---

## 1. Algoritmo de Scoring

### 1.1 Fórmula Principal

```
complexity_score = (
    scope_factor * 0.25 +
    depth_factor * 0.25 +
    ambiguity_factor * 0.20 +
    tooling_factor * 0.15 +
    duration_factor * 0.15
)
```

Resultado: `0.0` (trivial) a `1.0` (máxima complexidade)

### 1.2 Fatores de Complexidade

#### Scope Factor (0.0 - 1.0)

| Escopo | Valor | Exemplos |
|--------|-------|----------|
| Single file/item | 0.1 | "Corrigir typo", "Ler arquivo" |
| Few files (2-5) | 0.3 | "Refatorar função", "Criar componente" |
| Module/Feature | 0.5 | "Adicionar feature", "Criar API" |
| Multi-module | 0.7 | "Integrar sistemas", "Refatorar arquitetura" |
| Full project | 1.0 | "Criar app do zero", "Migração completa" |

#### Depth Factor (0.0 - 1.0)

| Profundidade | Valor | Exemplos |
|--------------|-------|----------|
| Surface level | 0.1 | "Listar arquivos", "Mostrar status" |
| Basic analysis | 0.3 | "Explicar código", "Resumir documento" |
| Moderate analysis | 0.5 | "Encontrar bugs", "Sugerir melhorias" |
| Deep analysis | 0.7 | "Arquitetar solução", "Análise de segurança" |
| Research-grade | 1.0 | "Pesquisa de mercado completa", "Auditoria profunda" |

#### Ambiguity Factor (0.0 - 1.0)

| Clareza | Valor | Exemplos |
|---------|-------|----------|
| Crystal clear | 0.1 | "Renomear variável X para Y" |
| Mostly clear | 0.3 | "Adicionar validação de email" |
| Some ambiguity | 0.5 | "Melhorar performance" |
| Significant ambiguity | 0.7 | "Fazer ficar melhor" |
| Highly ambiguous | 1.0 | "Consertar o código" (sem contexto) |

#### Tooling Factor (0.0 - 1.0)

| Ferramentas | Valor | Exemplos |
|-------------|-------|----------|
| No tools needed | 0.0 | "Explicar conceito" |
| Single tool | 0.2 | "Ler arquivo" |
| Few tools (2-3) | 0.4 | "Editar e testar" |
| Multiple tools | 0.6 | "Pesquisar, implementar, testar" |
| Complex orchestration | 1.0 | "Multi-agent workflow" |

#### Duration Factor (0.0 - 1.0)

| Duração Estimada | Valor | Exemplos |
|------------------|-------|----------|
| Instant (< 1min) | 0.1 | "Responder pergunta simples" |
| Quick (1-5min) | 0.3 | "Pequena edição" |
| Moderate (5-15min) | 0.5 | "Implementar feature pequena" |
| Extended (15-60min) | 0.7 | "Feature média, debugging" |
| Long (> 60min) | 1.0 | "Projeto completo, pesquisa extensa" |

---

## 2. Thresholds de Decisão

### 2.1 Model Selection

| Complexity Score | Modelo | Custo | Quando |
|------------------|--------|-------|--------|
| 0.0 - 0.3 | **Haiku** | $0.25/M input | Tarefas simples, alta velocidade |
| 0.3 - 0.7 | **Sonnet** | $3/M input | Tarefas moderadas, bom equilíbrio |
| 0.7 - 1.0 | **Opus** | $15/M input | Tarefas complexas, máxima qualidade |

### 2.2 Agent Selection

| Complexity Score | Estratégia |
|------------------|------------|
| 0.0 - 0.3 | Executar diretamente (sem agente) |
| 0.3 - 0.5 | Agente Sonnet (especializado) |
| 0.5 - 0.7 | Agente Sonnet (com mais contexto) |
| 0.7 - 1.0 | Agente Opus OU LimitlessAgent |

### 2.3 Escalation to LimitlessAgent

```yaml
escalate_to_limitless:
  conditions:
    - complexity > 0.7 AND task.is_multi_step
    - complexity > 0.5 AND task.requires_persistence
    - complexity > 0.8 (qualquer tarefa)
    - task.estimated_iterations > 10
```

---

## 3. Provider Selection Matrix

### 3.1 Quadrant Analysis

```
                    HIGH COST
                        │
         Q1             │            Q2
    ┌───────────────────┼───────────────────┐
    │                   │                   │
    │  Claude Opus      │   (AVOID)         │
    │  Complex tasks    │   High cost,      │
    │  High quality     │   low complexity  │
    │                   │                   │
HIGH├───────────────────┼───────────────────┤LOW
COMP│                   │                   │COMP
    │  Claude Sonnet    │   Claude Haiku    │
    │  Balanced         │   or Ollama       │
    │  Most tasks       │   Simple tasks    │
    │                   │                   │
    └───────────────────┼───────────────────┘
         Q3             │            Q4
                        │
                    LOW COST
```

### 3.2 Cost Sensitivity Override

```yaml
cost_sensitivity:
  low:
    description: "Qualidade máxima, custo não importa"
    model_preference: [opus, sonnet, haiku]

  medium:
    description: "Equilíbrio custo/qualidade"
    model_preference: [sonnet, haiku, opus]

  high:
    description: "Minimizar custo"
    model_preference: [haiku, ollama, sonnet]
```

---

## 4. Fallback Chain

### 4.1 Ordem de Fallback

```
1. Claude (Haiku/Sonnet/Opus) - Primary
      ↓ (if rate limited or unavailable)
2. Ollama (local) - Secondary
      ↓ (if unavailable)
3. Gemini Pro - Tertiary
      ↓ (if unavailable)
4. ChatGPT - Quaternary
```

### 4.2 Rate Limit Handling

```yaml
rate_limit_states:
  AVAILABLE:
    action: use_normally

  RATE_LIMITED:
    action: switch_to_fallback
    cooldown: 60s

  COOLDOWN:
    action: wait_or_fallback
    check_interval: 10s
```

### 4.3 Fallback Degradation

| Provider | Capabilities vs Claude |
|----------|----------------------|
| Ollama | 70-80% (local, free, limited context) |
| Gemini Pro | 85-90% (good alternative) |
| ChatGPT | 80-85% (different strengths) |

---

## 5. Heurísticas Rápidas

### 5.1 Keywords → Complexity

| Keywords | Complexity Boost |
|----------|-----------------|
| "simples", "rápido", "só" | -0.2 |
| "completo", "detalhado" | +0.2 |
| "pesquisar", "analisar" | +0.3 |
| "criar do zero", "arquitetar" | +0.4 |
| "migrar", "refatorar tudo" | +0.5 |

### 5.2 Task Type → Base Complexity

| Tipo de Tarefa | Base Complexity |
|----------------|-----------------|
| Pergunta simples | 0.1 |
| Leitura de arquivo | 0.2 |
| Edição pequena | 0.3 |
| Criação de função | 0.4 |
| Criação de componente | 0.5 |
| Criação de feature | 0.6 |
| Debugging complexo | 0.7 |
| Arquitetura/Design | 0.8 |
| Projeto completo | 0.9 |
| Pesquisa extensa | 1.0 |

---

## 6. Exemplos de Scoring

### 6.1 Exemplo: "Corrigir typo no README"

```yaml
analysis:
  scope: 0.1 (single file)
  depth: 0.1 (surface)
  ambiguity: 0.1 (crystal clear)
  tooling: 0.2 (single tool: Edit)
  duration: 0.1 (instant)

calculation:
  (0.1 * 0.25) + (0.1 * 0.25) + (0.1 * 0.20) + (0.2 * 0.15) + (0.1 * 0.15)
  = 0.025 + 0.025 + 0.02 + 0.03 + 0.015
  = 0.115

result:
  score: 0.12
  model: Haiku
  agent: None (execute directly)
```

### 6.2 Exemplo: "Criar landing page responsiva"

```yaml
analysis:
  scope: 0.5 (feature)
  depth: 0.5 (moderate)
  ambiguity: 0.5 (some ambiguity - "responsiva" é vago)
  tooling: 0.6 (multiple tools: Write, Edit, possibly test)
  duration: 0.5 (moderate)

calculation:
  (0.5 * 0.25) + (0.5 * 0.25) + (0.5 * 0.20) + (0.6 * 0.15) + (0.5 * 0.15)
  = 0.125 + 0.125 + 0.10 + 0.09 + 0.075
  = 0.515

result:
  score: 0.52
  model: Sonnet
  agent: frontend-developer
```

### 6.3 Exemplo: "Arquitetar sistema de microservices"

```yaml
analysis:
  scope: 1.0 (full project)
  depth: 0.8 (deep analysis)
  ambiguity: 0.7 (significant - many ways to do it)
  tooling: 0.8 (complex orchestration)
  duration: 1.0 (long)

calculation:
  (1.0 * 0.25) + (0.8 * 0.25) + (0.7 * 0.20) + (0.8 * 0.15) + (1.0 * 0.15)
  = 0.25 + 0.20 + 0.14 + 0.12 + 0.15
  = 0.86

result:
  score: 0.86
  model: Opus
  agent: backend-architect
  escalate: Consider LimitlessAgent
```

---

## 7. Ajustes Dinâmicos

### 7.1 Learning from Outcomes

```yaml
feedback_loop:
  if task_succeeded AND actual_time < estimated_time:
    adjust: lower_complexity_for_similar_tasks

  if task_failed OR required_escalation:
    adjust: raise_complexity_for_similar_tasks
```

### 7.2 User Preference Override

```yaml
user_overrides:
  always_use_opus: false
  prefer_local: false  # Ollama preference
  cost_limit_per_task: null  # USD

  manual_override:
    description: "User can always force model choice"
    example: "use opus for this"
```

---

## 8. Integração com Request-Optimizer

### 8.1 Fluxo de Scoring

```
User Request
     ↓
request-optimizer receives
     ↓
Extract factors (scope, depth, ambiguity, tooling, duration)
     ↓
Calculate complexity_score
     ↓
Determine model recommendation
     ↓
Determine agent recommendation
     ↓
Check escalation conditions
     ↓
Present recommendation to user
```

### 8.2 Output Format

```yaml
complexity_analysis:
  score: 0.52
  factors:
    scope: 0.5
    depth: 0.5
    ambiguity: 0.5
    tooling: 0.6
    duration: 0.5
  recommendation:
    model: sonnet
    agent: frontend-developer
    escalate: false
  confidence: 0.85
```

---

## 9. Métricas e Calibração

### 9.1 Métricas a Rastrear

```yaml
track:
  - predicted_complexity vs actual_effort
  - model_recommendation vs model_used
  - escalation_predictions vs actual_escalations
  - cost_predictions vs actual_cost
```

### 9.2 Calibração Periódica

- Revisar pesos dos fatores mensalmente
- Ajustar thresholds baseado em outcomes
- Adicionar novas heurísticas conforme padrões emergem

---

## 10. Changelog

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0.0 | 2026-01-18 | Criação baseada no LimitlessAgent llm-routing.md |

---

**Fonte de Verdade**: `Projects/LimitlessAgent/docs/diagrams/llm-routing.md`
**Última atualização**: 2026-01-18
