# MCP Routing

Lógica de seleção de MCP servers baseada no tipo de integração necessária.

> **Fonte**: `Automation/mcps/MCP-CATALOG.md`
> **Configuração**: `.claude/mcp.json`
> **Total**: 14 MCPs disponíveis

---

## 1. Mapa de MCPs por Categoria

### 1.1 Cloud APIs (6 MCPs)

| MCP | Tipo | Quando Usar | Operações |
|-----|------|-------------|-----------|
| `notion` | Cloud API | Workspace Notion, databases, pages | read, write, query, create |
| `supabase` | Cloud API | Backend, auth, real-time, storage | query, insert, update, rpc |
| `figma-desktop` | Local | Design assets, prototypes | read, export |
| `shadcn` | NPX | Componentes React/Tailwind | add, list |
| `context7` | NPX | Contexto expandido, documentação | fetch, search |
| `vercel` | Cloud API | Deploy, infraestrutura, domains | deploy, list, logs |

**Seleção automática**:
```yaml
if task.involves_integration:
  match task.service:
    "notion": return "notion"
    "supabase" | "database" | "backend": return "supabase"
    "figma" | "design": return "figma-desktop"
    "react" | "tailwind" | "component": return "shadcn"
    "documentation" | "library docs": return "context7"
    "deploy" | "vercel" | "hosting": return "vercel"
```

### 1.2 Built-in (6 MCPs)

| MCP | Quando Usar | Operações |
|-----|-------------|-----------|
| `markitdown` | Converter documentos para markdown | convert |
| `memory` | Memória persistente entre sessões | store, recall |
| `filesystem` | Acesso a arquivos do sistema | read, write, list |
| `github` | Integração GitHub | repos, issues, prs |
| `fetch` | Web fetching | fetch, parse |
| `context7` | Documentação de bibliotecas | fetch_docs |

**Seleção automática**:
```yaml
if task.needs_builtin:
  match task.type:
    "convert_document": return "markitdown"
    "remember" | "recall": return "memory"
    "file_access": return "filesystem"
    "github" | "repo" | "pr" | "issue": return "github"
    "web_fetch" | "url": return "fetch"
    "library_docs": return "context7"
```

### 1.3 Custom (1 MCP)

| MCP | Quando Usar | Operações |
|-----|-------------|-----------|
| `obsidian-docs` | Documentação Obsidian | search, read |

### 1.4 Development (1 MCP)

| MCP | Quando Usar | Operações |
|-----|-------------|-----------|
| `genkit` | Google AI Framework | generate, embed |

---

## 2. Matriz de Decisão

### 2.1 Por Serviço Externo

| Serviço | MCP Primário | Fallback |
|---------|--------------|----------|
| Notion | notion | fetch + parse manual |
| Supabase | supabase | (sem fallback) |
| GitHub | github | fetch GitHub API |
| Figma | figma-desktop | (sem fallback) |
| Vercel | vercel | (sem fallback) |
| Documentação | context7 | fetch + parse |

### 2.2 Por Tipo de Operação

| Operação | MCPs Aplicáveis |
|----------|-----------------|
| Ler dados externos | notion, supabase, github, fetch |
| Escrever dados | notion, supabase, memory |
| Deploy | vercel |
| Converter formato | markitdown |
| Lembrar contexto | memory |
| Buscar docs | context7, obsidian-docs |
| Adicionar componente | shadcn |

### 2.3 Por Autenticação

| MCP | Requer Auth | Tipo |
|-----|-------------|------|
| notion | Sim | OAuth / Token |
| supabase | Sim | API Key |
| vercel | Sim | Token |
| github | Sim | Token |
| figma-desktop | Sim | Local auth |
| shadcn | Não | Public |
| context7 | Não | Public |
| Built-ins | Não | Local |

---

## 3. Regras de Seleção

### 3.1 Regra: Service Match

```yaml
rule: match_service_to_mcp
description: "Se tarefa menciona serviço específico, usar MCP correspondente"
priority: HIGH
condition: task.mentions_known_service
action: select_matching_mcp
```

### 3.2 Regra: Operation Type

```yaml
rule: operation_determines_mcp
description: "Tipo de operação ajuda a selecionar MCP"
examples:
  - "criar página no Notion" → notion (write)
  - "buscar dados do banco" → supabase (query)
  - "fazer deploy" → vercel (deploy)
  - "lembrar para próxima sessão" → memory (store)
```

### 3.3 Regra: Fallback para Fetch

```yaml
rule: fetch_as_fallback
description: "Se MCP específico não disponível, tentar fetch"
condition: specific_mcp_unavailable AND task.is_read_only
action: use_fetch_mcp
warning: "Funcionalidade reduzida, apenas leitura"
```

---

## 4. Combinação de MCPs

Algumas tarefas requerem múltiplos MCPs:

| Tarefa | MCPs | Ordem |
|--------|------|-------|
| Sync Notion → Supabase | notion, supabase | notion read → supabase write |
| Deploy com dados | supabase, vercel | supabase query → vercel deploy |
| Documentar projeto | github, notion | github read → notion write |
| Buscar e lembrar | fetch, memory | fetch → memory store |

### 4.1 Pipeline de MCPs

```yaml
mcp_pipeline:
  name: "notion_to_supabase_sync"
  steps:
    - mcp: notion
      action: query_database
      output: $data
    - mcp: supabase
      action: upsert
      input: $data
```

---

## 5. Detecção de Disponibilidade

### 5.1 Health Check

```yaml
health_check:
  notion:
    test: "list_databases"
    timeout: 5s
  supabase:
    test: "select 1"
    timeout: 3s
  vercel:
    test: "list_projects"
    timeout: 5s
  github:
    test: "get_authenticated_user"
    timeout: 5s
```

### 5.2 Fallback Strategy

```yaml
on_mcp_unavailable:
  notion:
    fallback: "Use WebFetch com Notion API diretamente"
    degraded: true
  supabase:
    fallback: "Nenhum - requer conexão"
    critical: true
  github:
    fallback: "Use WebFetch com GitHub API"
    degraded: true
  memory:
    fallback: "Use arquivos locais como cache"
    degraded: true
```

---

## 6. Segurança e Permissões

### 6.1 Operações Sensíveis

| MCP | Operação | Risco | Aprovação |
|-----|----------|-------|-----------|
| supabase | DELETE | Alto | Requer confirmação |
| supabase | DROP | Crítico | Bloqueado por padrão |
| notion | delete_page | Médio | Requer confirmação |
| vercel | delete_deployment | Alto | Requer confirmação |
| github | delete_repo | Crítico | Bloqueado por padrão |

### 6.2 Rate Limits

```yaml
rate_limits:
  notion:
    requests_per_second: 3
    daily_limit: 10000
  supabase:
    requests_per_second: 100
    daily_limit: unlimited (tier dependent)
  github:
    requests_per_hour: 5000
  vercel:
    deployments_per_day: 100
```

---

## 7. Métricas de Uso

### 7.1 Por MCP

```yaml
track_per_mcp:
  - invocation_count
  - success_rate
  - avg_latency_ms
  - error_types
  - rate_limit_hits
```

### 7.2 Otimização

Usar métricas para:
- Identificar MCPs com alta latência
- Detectar rate limits frequentes
- Ajustar fallback strategies
- Planejar upgrades de tier

---

## 8. Integração com LimitlessAgent

### 8.1 MCPs como Integrações

```yaml
limitless_mcp_integration:
  description: "LimitlessAgent usa MCPs para integrações externas"
  example:
    goal: "Atualizar dashboard com dados do banco"
    mcp_usage:
      - supabase: query data
      - notion: update page
      - vercel: trigger rebuild
```

### 8.2 State Persistence

```yaml
state_via_mcp:
  primary: supabase
  description: "Supabase armazena estado do LimitlessAgent"
  tables:
    - limitless_executions
    - limitless_tasks
    - limitless_memory
    - limitless_documents
```

---

## 9. Extensibilidade

### 9.1 Adicionando Novo MCP

1. Adicionar configuração em `.claude/mcp.json`
2. Atualizar `Automation/mcps/MCP-CATALOG.md`
3. Adicionar entrada neste arquivo
4. Definir operações e triggers
5. Testar conexão e operações

### 9.2 Template de Entrada

```yaml
new_mcp:
  name: "mcp-name"
  type: "cloud | local | builtin"
  connection: "url ou comando"
  auth_required: true | false
  operations:
    - name: "operation1"
      risk: "low | medium | high | critical"
    - name: "operation2"
      risk: "low"
  when_to_use: "Descrição"
  fallback: "Estratégia de fallback"
```

---

## 10. Changelog

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0.0 | 2026-01-18 | Criação com 14 MCPs mapeados |

---

**Fonte de Verdade**: `Automation/mcps/MCP-CATALOG.md`
**Última atualização**: 2026-01-18
