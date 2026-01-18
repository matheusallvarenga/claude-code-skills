# Changelog

Todas as mudanças notáveis nesta skill serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [Unreleased]

### Planejado
- Integração completa com LimitlessAgent (NZT Protocol)
- State persistence via Supabase
- Métricas e analytics dashboard
- Learning from outcomes (feedback loop)
- API endpoints para invocação externa

---

## [2.0.0] - 2026-01-18

### Adicionado
- **Arquitetura modular** com arquivos de referência separados
- **`references/resource-registry.md`** - Central de referências para todos os recursos
- **`references/agent-routing.md`** - Lógica de seleção para 27 agentes especializados
- **`references/skill-routing.md`** - Lógica de seleção para 27 skills
- **`references/mcp-routing.md`** - Lógica de seleção para 14 MCPs
- **`references/complexity-scoring.md`** - Algoritmo de scoring (0.0-1.0)
- **`references/decision-tree.md`** - Árvore de decisão expandida
- **`references/integration-interfaces.md`** - Interfaces TypeScript para futuras integrações
- **Análise em 5 pontos**: Specificity, Exploration, Subtasks, Tools, Model
- **Approval gates** documentados para operações sensíveis
- **Fallback chain**: Claude → Ollama → Gemini → ChatGPT
- **Resource Combination Matrix**: Como combinar skill + agent + MCP
- **Execution paths**: Direct | Agent | LimitlessAgent
- Este arquivo `CHANGELOG.md`
- `README.md` completo para repositório

### Alterado
- **SKILL.md** completamente reescrito para v2.0
- Fórmula de complexidade agora usa 5 fatores ponderados:
  ```
  complexity = (scope*0.25 + depth*0.25 + ambiguity*0.20 + tooling*0.15 + duration*0.15)
  ```
- Model selection baseado em thresholds:
  - < 0.3: Haiku
  - 0.3-0.7: Sonnet
  - > 0.7: Opus
- Agent selection agora considera 27 agentes categorizados

### Preparado para Futuro
- Interfaces definidas para LimitlessAgent (`IExecutionPlan`, `ILimitlessAgent`)
- Schema de eventos para callbacks (`SystemEvent`, `ICallbacks`)
- Estrutura de state management (`IStateManager`)

---

## [1.0.0] - 2025-11-07

### Adicionado
- Versão inicial (POC)
- Análise básica de requests
- Seleção simples de modelo (Haiku/Sonnet/Opus)
- Estrutura inicial de skill

### Limitações da v1.0
- Sem integração com catálogos de agentes
- Sem routing de skills ou MCPs
- Algoritmo de complexidade simplificado
- Sem interfaces de integração
- Sem documentação de fallbacks

---

## Comparativo de Versões

| Feature | v1.0.0 | v2.0.0 |
|---------|--------|--------|
| Agentes suportados | 0 | 27 |
| Skills suportadas | 0 | 27 |
| MCPs suportados | 0 | 14 |
| Algoritmo de scoring | Simples | 5 fatores ponderados |
| Arquivos de referência | 0 | 7 |
| Interfaces TypeScript | 0 | 8 |
| Approval gates | Não | Sim |
| Fallback chain | Não | Sim |
| LimitlessAgent ready | Não | Sim (interfaces) |

---

## Roadmap

### v2.1.0 (Planejado)
- [ ] Auto-invocação via hook no CLAUDE.md
- [ ] Métricas básicas de uso
- [ ] Cache de decisões similares

### v2.2.0 (Planejado)
- [ ] Integração inicial com Supabase para state
- [ ] Dashboard de métricas
- [ ] Learning from outcomes

### v3.0.0 (Planejado)
- [ ] Integração completa com LimitlessAgent
- [ ] NZT Protocol implementation
- [ ] Multi-session state persistence
- [ ] API externa para invocação

---

## Links

- [Documentação Principal](./README.md)
- [SKILL.md](./SKILL.md)
- [Catálogo de Agentes](../../Automation/agents/AGENTS-CATALOG.md)
- [Catálogo de MCPs](../../Automation/mcps/MCP-CATALOG.md)
- [LimitlessAgent Architecture](../../Projects/LimitlessAgent/docs/ARCHITECTURE.md)

---

**Mantido por**: Matheus Allvarenga
**Última atualização**: 2026-01-18
