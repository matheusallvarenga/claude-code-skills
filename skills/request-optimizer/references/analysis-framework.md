# Analysis Framework for Request Optimization

## 1. Specificity Analysis

Assess how well-defined the request is:

| Level | Characteristics | Example | Model Hint |
|-------|-----------------|---------|-----------|
| **High** | Target file/function named, clear action | "Fix the logout bug in auth.ts:42" | Haiku |
| **Medium** | General area known, but some exploration needed | "Improve authentication flow" | Sonnet |
| **Low** | Vague area, requires significant exploration | "Analyze the project and suggest improvements" | Sonnet |

**Action**: If specificity is LOW, recommend being more specific or approve exploration-based strategy.

---

## 2. Exploration Detection

Determine if codebase exploration is necessary:

### Triggers for "Exploration Needed"
- Request lacks specific file/directory references
- Requires understanding relationships between components
- Needs to discover what patterns/tech already exists
- Asks "how does X work" without file context

### Triggers for "No Exploration Needed"
- Request targets specific file(s)
- Request is about implementing from spec
- Request references existing documentation

**Action**: If exploration needed, recommend using Explore agent (but get approval first due to token cost).

---

## 3. Subtask Identification

Look for compound requests that should be decomposed:

### Pattern Matching
```
"Analyze X, then build Y, and integrate with Z"
→ At least 3 subtasks → Recommend TodoWrite decomposition

"Refactor login function and add 2FA"
→ 2 distinct subtasks → Might be OK together or split

"Continue implementation based on session notes"
→ Single outcome but multiple phases → Decompose
```

**Action**: If multiple subtasks detected, offer to create structured todo list via TodoWrite.

---

## 4. Tool Coordination Heuristics

### When to Recommend MCP
- Database queries needed → Use Supabase MCPs
- GitHub operations → Use GitHub MCPs
- Context7 library docs needed → Use Context7 MCP
- Searching docs → Use appropriate documentation MCP

### When to Recommend Agent
- Code understanding/exploration complex → Use Explore agent
- Security review needed → Use security-pro:security-auditor
- Complex refactoring across codebase → Use general-purpose agent
- Data analysis → Use supabase-toolkit:data-scientist

### When to Recommend Skill
- Multi-step workflow with approval gates → Launch another Skill
- Specialized domain workflow → Use domain Skill
- When this Skill analysis suggests another workflow tool

### When to Execute Immediately
- Simple questions answerable from context
- File edits with clear scope
- Code writing with defined requirements

---

## 5. Model Recommendation Matrix

```
┌─────────────────────────────────────────┐
│  Complexity × Specificity → Model Choice │
└─────────────────────────────────────────┘

High Specificity + Simple Task     → Haiku
High Specificity + Medium Task     → Sonnet
High Specificity + Complex Task    → Sonnet (or Opus if reasoning-heavy)
Low Specificity + Any Complexity   → Sonnet
Requires Planning/Architecture      → Opus
Quick Questions                     → Haiku
```

### Token Budget Consideration
- Always default to Haiku for simple/exploratory questions
- Sonnet for development work
- Opus only when user approves or complexity demands it

---

## 6. Context Optimization Signals

Recommend `/clear` if:
- Moving to completely different project
- Previous context is 90%+ consumed
- User changing from deep debug to new feature

Recommend `/compact` if:
- Context >80% capacity
- Continuing on same topic for long session
