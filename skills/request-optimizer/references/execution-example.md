# Execution Example: Real Request Analysis

## User Request (POC Example)

> "Preciso analisar os arquivos do diretório `/Users/matheusallvarenga/Desktop/Dev-Tools-Projects/GitHub/intentum` e continuar com a implementação do projeto baseado nas sessões que estão em `/Users/matheusallvarenga/Desktop/Dev-Tools-Projects/ClaudeCode/Sessions/2025/11-November/2025-11-05`"

---

## Skill Analysis Output (What Gets Returned)

### 1. Specificity Analysis
**Assessment**: MEDIUM
- **Positive**: Clear directory paths provided, previous context location identified
- **Concern**: "Continue implementation" is broad - scope not fully defined
- **Recommendation**: Request is acceptable; exploration will clarify scope

### 2. Exploration Detection
**Need**: YES
**Reasoning**:
- Must understand project structure in `/intentum` directory
- Must review previous session context to understand current state
- Must identify what "continue implementation" means (bugs? features? refactor?)

### 3. Subtask Identification
**Suggested Decomposition**:
1. Explore project structure at `/GitHub/intentum`
2. Review session notes from `/Sessions/2025/11-November/2025-11-05`
3. Identify gap/next steps from previous context
4. Begin implementation based on findings

### 4. Tool Coordination
**Recommended MCPs/Agents**:
- **Explore Agent**: To understand project structure (with approval)
- **No MCPs needed initially** (local file exploration)
- Consider additional agents after understanding scope

### 5. Model Recommendation
**Optimal**: SONNET
**Reasoning**:
- Requires code understanding + planning (Haiku insufficient)
- Architecture/relationship understanding needed
- Subsequent implementation work will need Sonnet capability
- Switch to Haiku only if deep exploration not needed

---

## Recommended Strategy

```
Phase 1: Context Discovery (Explore Agent)
├─ Scan /intentum for project structure, README, config files
├─ Identify: Tech stack, current implementation status, open issues
└─ Report: Project overview to user

Phase 2: Session Context Review (File Read)
├─ Read latest session notes from 2025-11-05
├─ Extract: Goals, blockers, decisions made, next steps
└─ Report: Session summary to user

Phase 3: Gap Analysis (Analysis)
├─ Compare: Current project state vs. session goals
├─ Identify: What's been done, what remains
└─ Report: Specific next implementation tasks

Phase 4: Implementation Approval
├─ Present: Prioritized task list for implementation
├─ Ask: Which task to tackle first?
└─ Begin: Development work on approved task
```

---

## Approval Gate

**Ready to proceed with this strategy?**
- **YES** → Execute phases 1-3, present findings, ask for phase 4 approval
- **NO, ADJUST** → Refine strategy (e.g., skip exploration, focus on specific area)
- **NO, CLARIFY** → User provides more scope/direction before proceeding

---

## Implementation Notes

If approved, this strategy will:
- Use **Explore Agent** to scan /intentum (token cost: medium)
- Use **Read tool** to review session context (token cost: low)
- Generate **TodoWrite** for structured task list (minimal cost)
- Result: Clear roadmap before development begins
