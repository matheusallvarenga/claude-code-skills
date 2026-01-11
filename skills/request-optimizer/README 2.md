# Request Optimizer Skill - POC

## Overview

This is a **Proof of Concept** for an intelligent request optimization system that automatically analyzes every request to optimize context usage, recommend execution strategies, and coordinate tool activation with user approval gates.

## What It Does

When you send a request, this skill:

1. **Analyzes** your request using a structured framework
2. **Recommends** the best execution strategy
3. **Suggests** which tools/models/agents to use
4. **Requests approval** before executing heavy operations
5. **Executes** the approved strategy

## Structure

```
request-optimizer/
├── SKILL.md                              # Main skill definition
├── references/
│   ├── analysis-framework.md             # How to analyze requests
│   ├── decision-tree.md                  # How to decide tools/strategies
│   └── execution-example.md              # Real example with your use case
└── README.md                             # This file
```

## How to Use

### Automatic Mode (Recommended)

The skill runs automatically on requests. No special invocation needed.

**Your request** → Skill analyzes → Skill recommends → You approve/adjust → Skill executes

### Manual Mode (Future Enhancement)

Command: `/optimize <your request>`

---

## Key Features

### 5-Point Analysis
- ✅ Specificity Assessment
- ✅ Exploration Detection
- ✅ Subtask Identification
- ✅ Tool Coordination
- ✅ Model Recommendation

### Strategic Output
- Clear analysis summary
- Recommended strategy steps
- Model choice with reasoning
- Tool recommendations (MCPs/Agents/Skills)

### Approval Gates
- Always asks before heavy operations
- Respects token budget concerns
- Suggests context optimization
- Prevents unnecessary tool invocations

---

## Example Workflow

### Input
```
"Preciso analisar os arquivos do diretório `/intentum`
e continuar com a implementação do projeto baseado nas
sessões de 2025-11-05"
```

### Skill Output
```
ANALYSIS RESULTS
├─ Specificity: MEDIUM (clear paths, broad scope)
├─ Exploration: YES NEEDED (understand project + session context)
├─ Subtasks: 4 phases identified
├─ Tools: Explore Agent recommended (with approval gate)
└─ Model: SONNET (code understanding + planning needed)

RECOMMENDED STRATEGY
├─ Phase 1: Explore /intentum structure
├─ Phase 2: Review 2025-11-05 session notes
├─ Phase 3: Gap analysis (what's done vs. what remains)
└─ Phase 4: Implementation planning

Ready to proceed? (Yes/No/Adjust)
```

### User Approval
```
Yes, proceed!
```

### Skill Execution
Runs Explore Agent → Reviews sessions → Creates TodoWrite → Presents findings

---

## Configuration

### Enable Automatic Mode
Add to your Claude Code settings:
```
request-optimizer: enabled
```

### Model Preferences
By default:
- Haiku for simple questions
- Sonnet for development
- Opus only when explicitly approved

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

## POC Status

This is a **Proof of Concept**. Future enhancements:
- [ ] Full automation without manual approval (optional)
- [ ] Integration with `/cost` command for budget tracking
- [ ] Custom analysis templates for specific project types
- [ ] Learning from user approval patterns
- [ ] Integration with workspace rate limits

---

## Troubleshooting

### Skill Not Triggering
- Ensure skill is in `~/.claude/skills/request-optimizer/`
- Check SKILL.md has proper YAML frontmatter
- Verify skill name matches reference

### Analysis Seems Wrong
- Check `references/analysis-framework.md` for rules
- Review `references/execution-example.md` for examples
- Consider providing more specific request details

### Approval Gates Too Strict
- This is intentional for POC to prevent token waste
- Can be adjusted in future iterations
- Comment in SKILL.md for specific overrides

---

## Next Steps

1. **Test** with your actual requests
2. **Iterate** based on what works/doesn't work
3. **Refine** analysis rules in `references/`
4. **Extend** with project-specific patterns
5. **Automate** approval for known-good scenarios

---

## Files Reference

- **SKILL.md** - How the skill works and what to do
- **analysis-framework.md** - Detailed analysis rules and matrices
- **decision-tree.md** - Tool selection logic and approval gates
- **execution-example.md** - Real-world example with your use case
