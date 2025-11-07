# Decision Tree: Tool Coordination

## Entry Point: Analysis Complete

You have completed analysis. Now decide what to do:

```
START: User Request Analyzed
│
├─ Is request specific enough to act?
│  ├─ YES → Can task be completed with current context?
│  │       ├─ YES → Create strategy, ask approval
│  │       └─ NO → Need exploration?
│  │              ├─ YES → Recommend Explore Agent (ask approval)
│  │              └─ NO → Need external data/queries?
│  │                     ├─ YES → Recommend MCP (ask approval)
│  │                     └─ NO → Recommend context optimization
│  │
│  └─ NO → Request too vague
│         └─ Recommend clarification or approve exploration-based approach

```

---

## Decision Rules

### Rule 1: Specificity Gate
**IF** request lacks specific file/function/area references
**THEN** flag as LOW specificity
**ACTION**: Either ask for clarification OR suggest Explore agent (with approval gate)

### Rule 2: Context Adequacy
**IF** you have file paths/sufficient context
**AND** task is straightforward
**THEN** proceed with direct strategy
**ACTION**: Create execution plan, request approval

### Rule 3: Exploration Trigger
**IF** request requires understanding codebase structure/relationships
**THEN** recommend Explore agent
**ACTION**: Present exploration plan, get approval, execute if approved

### Rule 4: MCP Activation
**IF** task needs external data/APIs
  - Database queries → Supabase MCPs
  - GitHub operations → GitHub MCPs
  - Library documentation → Context7 MCP
**THEN** recommend MCP invocation
**ACTION**: Present what will be fetched, get approval, execute if approved

### Rule 5: Subtask Decomposition
**IF** request has 3+ distinct outcomes/phases
**THEN** recommend TodoWrite decomposition
**ACTION**: Structure as todo list, suggest sequencing, get approval

### Rule 6: Model Escalation
**IF** task complexity HIGH and specificity HIGH
**AND** reasoning/architecture-heavy
**THEN** recommend Opus
**ACTION**: Note extra token cost, present reasoning, get approval

**ELSE IF** task complexity LOW
**THEN** recommend Haiku
**ACTION**: Default choice for efficiency

**ELSE**
**THEN** recommend Sonnet
**ACTION**: Balanced choice

---

## Approval Gates

### Always Ask Approval Before:
1. Invoking Explore Agent (token cost)
2. Invoking other Agents (Task tool invocation)
3. Creating MCPs queries that fetch large data
4. Switching to Opus model
5. Starting multi-step workflows (TodoWrite)

### Safe to Execute Without Approval:
1. Analyzing/thinking about the request
2. Recommending strategies
3. Suggesting `/clear`, `/compact`, or model changes
4. Answering questions from current context
5. Simple code edits (single file, clear scope)

---

## Execution Checklist

Before asking approval, verify:

- [ ] Analysis complete (all 5 framework items addressed)
- [ ] Strategy clear and actionable
- [ ] Tool recommendations justified
- [ ] Model recommendation with reasoning
- [ ] Approval gate identified (what needs user OK)
- [ ] Context optimization suggestions included (if applicable)

---

## Post-Execution

After user approves and execution starts:

1. Execute recommended strategy step-by-step
2. If intermediate approval needed (heavy tool invocation), pause and ask
3. Report results concisely
4. Ask: "Should we continue optimizing or are you ready to implement?"
5. If continuing, re-run analysis on next request
