# Integration Interfaces

Interfaces para integração futura com LimitlessAgent, Real Life OS e outros sistemas.

> **Propósito**: Definir contratos de integração para garantir compatibilidade futura
> **Status**: Especificação (não implementado ainda)

---

## 1. Visão Geral da Arquitetura de Integração

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         INTEGRATION LAYER                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌───────────────────────────────────────────────────────────────┐     │
│   │                    request-optimizer v2.0                      │     │
│   │                                                                │     │
│   │   Input: IUserRequest                                         │     │
│   │   Output: IRequestAnalysis                                    │     │
│   │                                                                │     │
│   └────────────────────────────┬──────────────────────────────────┘     │
│                                │                                         │
│                                ↓                                         │
│   ┌───────────────────────────────────────────────────────────────┐     │
│   │                    IExecutionRouter                            │     │
│   │                                                                │     │
│   │   Decide: Direct | Agent | LimitlessAgent                     │     │
│   │                                                                │     │
│   └────────────────────────────┬──────────────────────────────────┘     │
│                                │                                         │
│              ┌─────────────────┼─────────────────┐                      │
│              ↓                 ↓                 ↓                      │
│         Direct            Agent           LimitlessAgent                │
│         Execution         Invocation      (NZT Protocol)                │
│              │                 │                 │                      │
│              └─────────────────┼─────────────────┘                      │
│                                ↓                                         │
│   ┌───────────────────────────────────────────────────────────────┐     │
│   │                    IExecutionResult                            │     │
│   │                                                                │     │
│   │   Contains: result, metrics, state_changes                    │     │
│   │                                                                │     │
│   └────────────────────────────┬──────────────────────────────────┘     │
│                                │                                         │
│                                ↓                                         │
│   ┌───────────────────────────────────────────────────────────────┐     │
│   │                    IStateManager                               │     │
│   │                                                                │     │
│   │   Persist: Supabase | Memory MCP | Local Files                │     │
│   │                                                                │     │
│   └───────────────────────────────────────────────────────────────┘     │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Interface: IUserRequest

Input do usuário para o request-optimizer.

```typescript
interface IUserRequest {
  // Identificação
  id: string;                    // UUID único
  timestamp: string;             // ISO 8601
  session_id?: string;           // Para tracking cross-session

  // Conteúdo
  content: string;               // Texto do request
  context?: {
    files_mentioned: string[];   // Arquivos referenciados
    urls_mentioned: string[];    // URLs referenciadas
    previous_context?: string;   // Contexto de conversa anterior
  };

  // Preferências (opcionais)
  preferences?: {
    cost_sensitivity: 'low' | 'medium' | 'high';
    speed_preference: 'fast' | 'normal' | 'quality';
    model_override?: 'haiku' | 'sonnet' | 'opus';
    agent_override?: string;
  };

  // Metadata
  metadata?: {
    source: 'cli' | 'api' | 'webhook' | 'n8n';
    user_id?: string;
    project_id?: string;
  };
}
```

---

## 3. Interface: IRequestAnalysis

Output do request-optimizer após análise.

```typescript
interface IRequestAnalysis {
  // Identificação
  request_id: string;            // Referência ao IUserRequest
  analysis_id: string;           // UUID da análise
  timestamp: string;

  // 5-Point Analysis
  analysis: {
    specificity: {
      score: number;             // 0.0 - 1.0
      assessment: 'high' | 'medium' | 'low';
      missing_info?: string[];   // O que falta para ser específico
    };

    exploration_needed: {
      required: boolean;
      reason?: string;
      suggested_scope?: string;
    };

    subtasks: {
      identified: boolean;
      count: number;
      tasks: ISubtask[];
    };

    tool_coordination: {
      agents_needed: string[];
      skills_needed: string[];
      mcps_needed: string[];
    };

    model_recommendation: {
      recommended: 'haiku' | 'sonnet' | 'opus';
      reason: string;
      alternatives?: string[];
    };
  };

  // Complexity Score
  complexity: {
    score: number;               // 0.0 - 1.0
    factors: {
      scope: number;
      depth: number;
      ambiguity: number;
      tooling: number;
      duration: number;
    };
    category: 'simple' | 'medium' | 'complex';
  };

  // Recomendação Final
  recommendation: {
    execution_path: 'direct' | 'agent' | 'limitless';
    model: 'haiku' | 'sonnet' | 'opus';
    agent?: string;
    requires_approval: boolean;
    approval_reasons?: string[];
    estimated_cost?: string;
    estimated_duration?: string;
  };

  // Confiança
  confidence: number;            // 0.0 - 1.0
}

interface ISubtask {
  id: string;
  description: string;
  type: 'exploration' | 'implementation' | 'validation';
  dependencies: string[];        // IDs de outras subtasks
  estimated_complexity: number;
}
```

---

## 4. Interface: IExecutionPlan

Plano de execução para LimitlessAgent ou execução coordenada.

```typescript
interface IExecutionPlan {
  // Identificação
  plan_id: string;
  analysis_id: string;           // Referência à IRequestAnalysis
  timestamp: string;

  // Goal
  goal: {
    original: string;            // Request original
    refined?: string;            // Goal refinado após análise
    success_criteria: string[];  // Como saber que completou
  };

  // Subtasks
  tasks: IExecutionTask[];

  // Recursos
  resources: {
    agents: IAgentAssignment[];
    skills: ISkillAssignment[];
    mcps: IMCPAssignment[];
    models: IModelAssignment[];
  };

  // Configuração
  config: {
    max_iterations: number;
    max_cost_usd: number;
    timeout_minutes: number;
    parallel_allowed: boolean;
  };

  // Guardrails
  guardrails: {
    blocked_operations: string[];
    require_approval_for: string[];
    risk_level: 'low' | 'medium' | 'high';
  };
}

interface IExecutionTask {
  id: string;
  description: string;
  type: string;
  dependencies: string[];
  assigned_agent?: string;
  assigned_model: string;
  status: 'pending' | 'in_progress' | 'completed' | 'failed';
}

interface IAgentAssignment {
  agent_name: string;
  task_ids: string[];
  model: 'sonnet' | 'opus';
}

interface ISkillAssignment {
  skill_name: string;
  task_ids: string[];
  trigger?: string;
}

interface IMCPAssignment {
  mcp_name: string;
  operations: string[];
  task_ids: string[];
}

interface IModelAssignment {
  task_id: string;
  model: 'haiku' | 'sonnet' | 'opus';
  provider: 'claude' | 'ollama' | 'gemini' | 'chatgpt';
  fallback_chain: string[];
}
```

---

## 5. Interface: IExecutionResult

Resultado de uma execução (direta, agent, ou LimitlessAgent).

```typescript
interface IExecutionResult {
  // Identificação
  execution_id: string;
  plan_id?: string;              // Se veio de um plano
  analysis_id: string;
  timestamp_start: string;
  timestamp_end: string;

  // Status
  status: 'success' | 'partial' | 'failed' | 'cancelled';
  completion_percentage: number;

  // Resultado
  result: {
    summary: string;
    output?: any;                // Output específico da tarefa
    artifacts_created: string[]; // Arquivos criados
    artifacts_modified: string[];// Arquivos modificados
  };

  // Tasks (se multi-step)
  tasks?: {
    total: number;
    completed: number;
    failed: number;
    details: ITaskResult[];
  };

  // Métricas
  metrics: {
    total_tokens: number;
    total_cost_usd: number;
    iterations: number;
    agents_used: string[];
    skills_used: string[];
    mcps_used: string[];
    models_used: {
      model: string;
      tokens: number;
      cost: number;
    }[];
  };

  // Erros (se houver)
  errors?: {
    count: number;
    details: IError[];
  };

  // Learnings (para feedback loop)
  learnings?: {
    patterns_identified: string[];
    suggestions: string[];
  };
}

interface ITaskResult {
  task_id: string;
  status: 'success' | 'failed' | 'skipped';
  output?: any;
  error?: string;
  duration_ms: number;
  tokens_used: number;
}

interface IError {
  code: string;
  message: string;
  task_id?: string;
  recoverable: boolean;
  recovery_attempted: boolean;
}
```

---

## 6. Interface: IStateManager

Gerenciamento de estado persistente.

```typescript
interface IStateManager {
  // Operações de Estado
  saveState(key: string, value: any): Promise<void>;
  getState(key: string): Promise<any>;
  deleteState(key: string): Promise<void>;
  listStates(prefix?: string): Promise<string[]>;

  // Executions
  saveExecution(execution: IExecutionResult): Promise<void>;
  getExecution(execution_id: string): Promise<IExecutionResult>;
  listExecutions(filters?: ExecutionFilters): Promise<IExecutionResult[]>;

  // Memory
  saveMemory(key: string, value: any, embedding?: number[]): Promise<void>;
  searchMemory(query: string, limit?: number): Promise<MemoryResult[]>;

  // Metrics
  recordMetric(metric: IMetric): Promise<void>;
  getMetrics(filters?: MetricFilters): Promise<IMetric[]>;
}

interface ExecutionFilters {
  status?: string;
  date_from?: string;
  date_to?: string;
  agent?: string;
  limit?: number;
}

interface MemoryResult {
  key: string;
  value: any;
  similarity: number;
}

interface IMetric {
  name: string;
  value: number;
  timestamp: string;
  tags?: Record<string, string>;
}
```

---

## 7. Interface: ILimitlessAgent

Interface para invocar o LimitlessAgent.

```typescript
interface ILimitlessAgent {
  // Execução
  execute(plan: IExecutionPlan): Promise<IExecutionResult>;

  // Controle
  pause(execution_id: string): Promise<void>;
  resume(execution_id: string): Promise<void>;
  cancel(execution_id: string): Promise<void>;

  // Status
  getStatus(execution_id: string): Promise<ExecutionStatus>;

  // Iteração
  iterate(execution_id: string): Promise<IterationResult>;

  // Feedback
  provideFeedback(execution_id: string, feedback: Feedback): Promise<void>;
}

interface ExecutionStatus {
  execution_id: string;
  status: 'running' | 'paused' | 'completed' | 'failed';
  current_iteration: number;
  current_task?: string;
  progress_percentage: number;
  estimated_completion?: string;
}

interface IterationResult {
  iteration: number;
  task_completed?: string;
  next_task?: string;
  goal_complete: boolean;
  needs_input: boolean;
  input_question?: string;
}

interface Feedback {
  type: 'approval' | 'rejection' | 'modification' | 'input';
  content: string;
  applies_to?: string;  // task_id
}
```

---

## 8. Eventos e Callbacks

### 8.1 Eventos do Sistema

```typescript
type SystemEvent =
  | { type: 'analysis_complete'; data: IRequestAnalysis }
  | { type: 'execution_started'; data: { execution_id: string; plan: IExecutionPlan } }
  | { type: 'task_completed'; data: ITaskResult }
  | { type: 'iteration_complete'; data: IterationResult }
  | { type: 'execution_complete'; data: IExecutionResult }
  | { type: 'error'; data: IError }
  | { type: 'approval_needed'; data: ApprovalRequest }
  | { type: 'input_needed'; data: InputRequest };

interface ApprovalRequest {
  execution_id: string;
  action: string;
  reason: string;
  risk_level: 'low' | 'medium' | 'high';
  timeout_seconds?: number;
}

interface InputRequest {
  execution_id: string;
  question: string;
  options?: string[];
  required: boolean;
  timeout_seconds?: number;
}
```

### 8.2 Callbacks

```typescript
interface ICallbacks {
  onAnalysisComplete?: (analysis: IRequestAnalysis) => void;
  onExecutionStart?: (execution_id: string) => void;
  onTaskComplete?: (result: ITaskResult) => void;
  onIterationComplete?: (result: IterationResult) => void;
  onExecutionComplete?: (result: IExecutionResult) => void;
  onError?: (error: IError) => void;
  onApprovalNeeded?: (request: ApprovalRequest) => Promise<boolean>;
  onInputNeeded?: (request: InputRequest) => Promise<string>;
}
```

---

## 9. Implementação Futura

### 9.1 Fase 1: request-optimizer standalone

```yaml
phase: 1
status: current
implements:
  - IUserRequest (input)
  - IRequestAnalysis (output)
  - Basic execution routing
does_not_implement:
  - IStateManager (uses local files)
  - ILimitlessAgent (manual invocation)
```

### 9.2 Fase 2: State Management

```yaml
phase: 2
status: planned
implements:
  - IStateManager (Supabase)
  - Execution history
  - Metrics tracking
depends_on:
  - Supabase setup
  - LimitlessAgent schema
```

### 9.3 Fase 3: LimitlessAgent Integration

```yaml
phase: 3
status: planned
implements:
  - ILimitlessAgent
  - IExecutionPlan
  - Full event system
depends_on:
  - Phase 2 complete
  - LimitlessAgent implementation
```

---

## 10. Compatibilidade

### 10.1 Versioning

```yaml
interface_version: "1.0.0"
compatibility:
  request_optimizer: ">=2.0.0"
  limitless_agent: ">=1.0.0"  # quando disponível
breaking_changes:
  - Major version: incompatível
  - Minor version: backward compatible
  - Patch version: bug fixes only
```

### 10.2 Migration Path

```yaml
migration:
  v1_to_v2:
    - IRequestAnalysis.complexity agora é objeto (era number)
    - IExecutionResult.metrics expandido
    - Novos campos opcionais não quebram v1
```

---

## 11. Changelog

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0.0 | 2026-01-18 | Criação das interfaces de integração |

---

**Status**: Especificação para implementação futura
**Última atualização**: 2026-01-18
