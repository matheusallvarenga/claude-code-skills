# Request Optimizer

> Intelligent request analysis and routing system for Claude Code CLI

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](./CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](https://claude.ai/claude-code)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

---

## Overview

**Request Optimizer** is an intelligent gateway that intercepts and analyzes every user request before execution. It calculates task complexity, selects appropriate resources (agents, skills, MCPs), and recommends the optimal execution strategy.

### Key Features

- **Complexity Scoring** - Algorithm that scores tasks from 0.0 (trivial) to 1.0 (maximum complexity)
- **Resource Routing** - Intelligent selection from 27 agents, 27 skills, and 14 MCPs
- **Model Selection** - Automatic routing to Haiku, Sonnet, or Opus based on complexity
- **Approval Gates** - Safety controls for sensitive operations
- **LimitlessAgent Ready** - Interfaces prepared for future autonomous agent integration

---

## Quick Start

### Installation

This skill is designed for [Claude Code CLI](https://claude.ai/claude-code). Copy the entire `request-optimizer` folder to your skills directory:

```bash
cp -r request-optimizer ~/.claude/skills/
# or for project-specific
cp -r request-optimizer .claude/skills/
```

### Usage

The skill is invoked automatically when configured, or manually via:

```
/request-optimizer
```

Or reference in conversation:

```
Analyze this request before executing: [your task here]
```

---

## Architecture

```
USER REQUEST
     │
     ↓
┌─────────────────────────────────────────────────────────────┐
│                  request-optimizer v2.0                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   PHASE 1: Analysis (5 Points)                              │
│   └─ references/analysis-framework.md                       │
│                                                              │
│   PHASE 2: Complexity Scoring                               │
│   └─ references/complexity-scoring.md                       │
│                                                              │
│   PHASE 3: Resource Selection                               │
│   ├─ references/agent-routing.md (27 agents)                │
│   ├─ references/skill-routing.md (27 skills)                │
│   └─ references/mcp-routing.md (14 MCPs)                    │
│                                                              │
│   PHASE 4: Execution Routing                                │
│   └─ references/decision-tree.md                            │
│                                                              │
│   PHASE 5: Integration (Future)                             │
│   └─ references/integration-interfaces.md                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
     │
     ↓
┌─────────────────────────────────────────────────────────────┐
│                   EXECUTION PATH                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Complexity < 0.3   →   Direct Execution (Haiku)           │
│   Complexity 0.3-0.7 →   Agent Execution (Sonnet)           │
│   Complexity > 0.7   →   LimitlessAgent (Opus/NZT)          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## How It Works

### Phase 1: 5-Point Analysis

When a request is received, the skill analyzes it across 5 dimensions:

| Point | Question | Example |
|-------|----------|---------|
| **Specificity** | How specific is the request? | "Fix bug" vs "Fix null pointer in auth.ts:42" |
| **Exploration** | Does it need codebase exploration? | Unknown file locations, architecture questions |
| **Subtasks** | Can it be decomposed? | Multi-step features, migrations |
| **Tools** | What resources are needed? | Agents, Skills, MCPs |
| **Model** | Which model is optimal? | Haiku, Sonnet, Opus |

### Phase 2: Complexity Scoring

Complexity is calculated using 5 weighted factors:

```
complexity_score = (
    scope_factor * 0.25 +
    depth_factor * 0.25 +
    ambiguity_factor * 0.20 +
    tooling_factor * 0.15 +
    duration_factor * 0.15
)
```

| Factor | Weight | Range |
|--------|--------|-------|
| Scope | 25% | Single file → Full project |
| Depth | 25% | Surface → Research-grade |
| Ambiguity | 20% | Crystal clear → Highly ambiguous |
| Tooling | 15% | No tools → Complex orchestration |
| Duration | 15% | Instant → Long (60+ min) |

### Phase 3: Resource Selection

Based on analysis, the skill selects from:

| Resource | Count | Examples |
|----------|-------|----------|
| **Agents** | 27 | fullstack-developer, code-reviewer, market-research-analyst |
| **Skills** | 27 | pdf, docx, webapp-testing, notion-* |
| **MCPs** | 14 | notion, supabase, github, vercel |

### Phase 4: Recommendation

The skill presents a structured recommendation:

```markdown
## Analysis Results

| Factor | Assessment |
|--------|------------|
| **Specificity** | HIGH |
| **Complexity Score** | 0.52 |
| **Exploration Needed** | No |
| **Subtasks Identified** | 3 |

## Resource Recommendation

| Type | Resource | Reason |
|------|----------|--------|
| Model | Sonnet | Balanced cost/quality |
| Agent | frontend-developer | React expertise needed |
| Skills | webapp-testing | UI verification |
| MCPs | shadcn | Component library |

## Execution Path

Agent Execution (Sonnet)

Ready to execute? (Yes / No / Adjust)
```

---

## File Structure

```
request-optimizer/
├── SKILL.md                              # Main skill definition
├── README.md                             # This file
├── CHANGELOG.md                          # Version history
├── POC-SUMMARY.md                        # Original POC documentation
└── references/
    ├── resource-registry.md              # Central resource index
    ├── agent-routing.md                  # 27 agent selection logic
    ├── skill-routing.md                  # 27 skill selection logic
    ├── mcp-routing.md                    # 14 MCP selection logic
    ├── complexity-scoring.md             # Scoring algorithm
    ├── decision-tree.md                  # Routing decision tree
    ├── integration-interfaces.md         # TypeScript interfaces
    ├── analysis-framework.md             # 5-point analysis rules
    ├── execution-example.md              # Real-world example
    └── configuration-guide.md            # Configuration options
```

---

## Model Selection

| Complexity | Model | Cost | Use Case |
|------------|-------|------|----------|
| 0.0 - 0.3 | **Haiku** | $0.25/M | Simple tasks, high speed |
| 0.3 - 0.7 | **Sonnet** | $3/M | Balanced tasks |
| 0.7 - 1.0 | **Opus** | $15/M | Complex tasks, max quality |

### Fallback Chain

When primary model is unavailable:

```
Claude (Haiku/Sonnet/Opus)
    ↓
Ollama (local)
    ↓
Gemini Pro
    ↓
ChatGPT
```

---

## Approval Gates

### Requires Approval

| Action | Risk | Reason |
|--------|------|--------|
| Invoke Explore Agent | Medium | Token cost |
| Invoke any Agent (Task tool) | Medium | Token cost |
| Use Opus model | High | Elevated cost |
| Execute LimitlessAgent | High | Autonomy, cost |
| MCP write operations | Medium | Data modification |
| Multi-step workflows (5+ tasks) | Medium | Complexity |

### Safe Without Approval

| Action | Reason |
|--------|--------|
| Analyze request | Reasoning only |
| Recommend strategy | No execution |
| Read files | Read-only |
| Simple edits (1 file, clear scope) | Low risk |
| MCP read operations | Read-only |

---

## Configuration

### CLAUDE.md Integration

Add to your project's CLAUDE.md for automatic activation:

```markdown
## Request Analysis

Before executing any non-trivial request, invoke the request-optimizer skill to:
1. Analyze complexity (0.0-1.0)
2. Select appropriate resources (agents, skills, MCPs)
3. Recommend execution strategy
4. Get approval for sensitive operations

Reference: `.claude/skills/request-optimizer/SKILL.md`
```

### Environment Variables (Future)

```bash
# Cost sensitivity (low, medium, high)
REQUEST_OPTIMIZER_COST_SENSITIVITY=medium

# Default model override
REQUEST_OPTIMIZER_MODEL_OVERRIDE=

# Max complexity for auto-execution
REQUEST_OPTIMIZER_AUTO_EXECUTE_THRESHOLD=0.3
```

---

## Integration with LimitlessAgent

This skill is designed to integrate with [LimitlessAgent](../../Projects/LimitlessAgent/) for autonomous multi-step execution.

### Current Status

- **Phase 1** (Current): Standalone analysis and recommendation
- **Phase 2** (Planned): State persistence via Supabase
- **Phase 3** (Planned): Full LimitlessAgent integration

### Interfaces

TypeScript interfaces are defined in `references/integration-interfaces.md`:

```typescript
interface IExecutionPlan {
  plan_id: string;
  goal: IGoal;
  tasks: IExecutionTask[];
  resources: IResources;
  config: IConfig;
  guardrails: IGuardrails;
}
```

---

## Examples

### Example 1: Simple Task

```
User: "Fix typo in README"

Analysis:
  Specificity: HIGH
  Complexity: 0.12
  Model: Haiku
  Agent: None
  Path: Direct Execution
```

### Example 2: Medium Task

```
User: "Create responsive landing page"

Analysis:
  Specificity: MEDIUM
  Complexity: 0.52
  Model: Sonnet
  Agent: frontend-developer
  Skills: frontend-design
  MCPs: shadcn
  Path: Agent Execution
```

### Example 3: Complex Task

```
User: "Architect microservices system"

Analysis:
  Specificity: LOW
  Complexity: 0.86
  Model: Opus
  Agent: backend-architect
  Path: LimitlessAgent (recommended)
  Approval: REQUIRED
```

---

## Token Budget Impact

This skill is designed to **reduce** overall token usage by:
- Avoiding unnecessary exploration
- Recommending Haiku for simple tasks
- Suggesting context clearing/compacting
- Preventing redundant tool invocations
- Structuring work before execution

**Estimated overhead**: <5% additional context for analysis recommendations

---

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Follow existing file structure and naming conventions
4. Update CHANGELOG.md
5. Submit Pull Request

### Adding New Resources

**New Agent**: Update `references/agent-routing.md` and link to `Automation/agents/AGENTS-CATALOG.md`

**New Skill**: Update `references/skill-routing.md`

**New MCP**: Update `references/mcp-routing.md` and link to `Automation/mcps/MCP-CATALOG.md`

---

## Related Projects

| Project | Description | Link |
|---------|-------------|------|
| LimitlessAgent | Autonomous agent with NZT Protocol | `Projects/LimitlessAgent/` |
| Claude Code Skills | Skill repository | [GitHub](https://github.com/matheusallvarenga/claude-code-skills) |
| Agents Catalog | 27 specialized agents | `Automation/agents/AGENTS-CATALOG.md` |
| MCPs Catalog | 14 MCP servers | `Automation/mcps/MCP-CATALOG.md` |

---

## Troubleshooting

### Skill Not Triggering
- Ensure skill is in `~/.claude/skills/request-optimizer/` or `.claude/skills/request-optimizer/`
- Check SKILL.md has proper YAML frontmatter
- Verify skill name matches reference

### Analysis Seems Wrong
- Check `references/analysis-framework.md` for rules
- Review `references/execution-example.md` for examples
- Consider providing more specific request details

### Approval Gates Too Strict
- This is intentional to prevent token waste
- Can be adjusted via configuration (future)
- Check `references/decision-tree.md` for rules

---

## License

MIT License - See [LICENSE](./LICENSE) file for details.

---

## Author

**Matheus Allvarenga**
- GitHub: [@matheusallvarenga](https://github.com/matheusallvarenga)

---

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history.

---

**Version**: 2.0.0
**Last Updated**: 2026-01-18
