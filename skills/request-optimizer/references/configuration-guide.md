# Configuration & Integration Guide

## Setup

### 1. Verify Skill Location
```bash
ls -la ~/.claude/skills/request-optimizer/
```

Should see:
- SKILL.md
- README.md
- references/
  - analysis-framework.md
  - decision-tree.md
  - execution-example.md
  - configuration-guide.md

### 2. No Additional Configuration Needed for POC
The skill works as-is. It automatically analyzes requests when invoked.

---

## How It Integrates With Your Workflow

### Before Optimization Skill
```
You: Send request
├─ Claude: Maybe explores wrong area
├─ Claude: Uses expensive model when simple one suffices
├─ Claude: Does heavy work without asking
└─ Result: Token waste, context overload
```

### After Optimization Skill
```
You: Send request
├─ Skill: Analyzes (5-point framework)
├─ Skill: Recommends strategy
├─ Skill: Suggests model, tools, subtasks
├─ Skill: Asks for approval
├─ You: Approve or adjust
├─ Skill: Executes with approval
└─ Result: Optimized context, clear roadmap, token efficiency
```

---

## Integration with Other Tools

### With TodoWrite
When skill detects multiple subtasks:
```
Skill: "This has 4 phases. Create structured todo?"
You: "Yes"
Skill: Invokes TodoWrite with phase breakdown
Result: Clear task list from start
```

### With Explore Agent
When skill recommends exploration:
```
Skill: "Need to understand /projectdir structure?"
You: "Yes"
Skill: Invokes Explore Agent with focused scope
Result: Targeted exploration, not blind wandering
```

### With MCP Tools
When skill recommends external data:
```
Skill: "Need to query database for user counts?"
You: "Yes, please"
Skill: Recommends Supabase MCP with specific query
Result: Efficient data fetch, not general data load
```

### With Model Selection
```
Skill: "Simple question → Recommend Haiku"
Skill: "Complex architecture → Recommend Sonnet"
Skill: "Heavy reasoning → Recommend Opus (token cost warning)"
Result: Right tool for right job, token budget respected
```

### With Context Optimization
```
Skill: "Context >80% → Recommend /compact"
Skill: "Switching projects → Recommend /clear"
Result: Efficient context management
```

---

## Customization Points

### Adjust Analysis Rules
Edit: `references/analysis-framework.md`
- Change specificity thresholds
- Adjust tool recommendation weights
- Update model selection criteria

### Adjust Decision Logic
Edit: `references/decision-tree.md`
- Add new approval gates
- Modify exploration triggers
- Update tool priorities

### Add Project-Specific Patterns
Add new file: `references/project-patterns.md`
- Company-specific architecture patterns
- Known tool preferences
- Team conventions

Example:
```markdown
## Intentum Project Patterns

When request mentions:
- "authentication" → Recommend checking auth.ts
- "database" → Recommend schema review
- "UI changes" → Recommend component audit
```

---

## Approval Gate Tuning

### Current Defaults (Conservative)
```
Ask approval for:
- Any Explore Agent invocation
- MCP queries for >1000 rows
- Model upgrade to Opus
- TodoWrite subtask creation
```

### For Aggressive Optimization
Modify SKILL.md:
```
"Execute without asking:
- Haiku for simple questions
- Pre-approved tool patterns
- Known-good workflows"
```

### For Maximum Safety
Modify SKILL.md:
```
"Ask approval for:
- Everything above +
- Any model change
- Any tool invocation
- Any context operation"
```

---

## Monitoring & Tuning

### Metrics to Track (Future)
- Analysis accuracy (do recommendations match what you'd choose?)
- Token savings (vs. without skill)
- Approval rate (what % of recommendations you approve?)
- Tool effectiveness (did recommended tools work well?)

### Iteration Based on Real Usage
1. Use skill for a week
2. Note patterns of approval/rejection
3. Adjust rules based on patterns
4. Re-test with adjusted rules

---

## Troubleshooting Configuration

### Skill Not Activating
**Check**: Is SKILL.md valid YAML?
```bash
cat ~/.claude/skills/request-optimizer/SKILL.md | head -5
```

Should show proper frontmatter:
```
---
name: request-optimizer
description: This skill analyzes...
---
```

### Recommendations Seem Off
**Check**: Are you reading `references/analysis-framework.md`?

Modify based on your patterns. Example:
```markdown
If you notice all simple requests being routed to Sonnet:
Edit: analysis-framework.md > Model Recommendation Matrix
Change: "High Specificity + Simple Task → Sonnet"
To: "High Specificity + Simple Task → Haiku"
```

### Approval Gates Too Strict/Loose
**Check**: `references/decision-tree.md` Approval Gates section

Adjust what needs approval vs. what executes automatically.

---

## Future Enhancements

### Phase 2: Learning
- Track which recommendations you approve most
- Auto-adjust thresholds
- Learn project-specific patterns

### Phase 3: Automation
- Pre-approved workflows skip approval
- Familiar patterns execute automatically
- Only unusual requests need approval

### Phase 4: Integration
- Connect to workspace rate limits
- Sync with `/cost` tracking
- Dashboard of optimization metrics

---

## Quick Reference

| Need | File to Edit | What to Change |
|------|--------------|----------------|
| Better specificity detection | analysis-framework.md | Specificity Analysis section |
| Different tool recommendations | decision-tree.md | Decision Rules section |
| Project-specific patterns | Create project-patterns.md | Add new patterns |
| Fewer approval gates | SKILL.md | Execution Phase (After Approval) |
| More approval gates | decision-tree.md | Approval Gates section |
| Different model recommendations | analysis-framework.md | Model Recommendation Matrix |
