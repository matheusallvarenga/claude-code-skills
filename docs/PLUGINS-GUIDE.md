# Plugins Guide - Recommended Claude Code Plugins

This guide lists recommended plugins organized by category. Install via Claude Code's plugin manager.

---

## Official Claude Plugins

Core plugins maintained by Anthropic and partners.

### Development & Code Quality

| Plugin | Source | Description |
|--------|--------|-------------|
| superpowers | claude-plugins-official | Enhanced Claude Code capabilities (parallel agents, brainstorming, TDD, git worktrees) |
| coderabbit | claude-plugins-official | AI-powered code review |
| pyright-lsp | claude-plugins-official | Python type checking and language server |
| typescript-lsp | claude-plugins-official | TypeScript language server |
| skill-creator | claude-plugins-official | Create custom skills for Claude Code |
| plugin-dev | claude-plugins-official | Develop Claude Code plugins |
| pr-review-toolkit | claude-plugins-official | Pull request review automation |
| commit-commands | claude-plugins-official | Git commit workflow commands |
| code-simplifier | claude-plugins-official | Code simplification and cleanup |
| agent-sdk-dev | claude-plugins-official | Anthropic Agent SDK development |

### Integrations

| Plugin | Source | Description |
|--------|--------|-------------|
| firebase | claude-plugins-official | Firebase/Google Cloud integration |
| slack | claude-plugins-official | Slack messaging integration |
| playwright | claude-plugins-official | Browser automation and testing |
| figma | claude-plugins-official | Figma design tool integration |
| github | claude-plugins-official | GitHub repository management |
| vercel | claude-plugins-official | Vercel deployment platform |
| supabase | claude-plugins-official | Supabase backend-as-a-service |
| Notion | claude-plugins-official | Notion workspace integration |
| context7 | claude-plugins-official | Library documentation lookup |

### Productivity

| Plugin | Source | Description |
|--------|--------|-------------|
| claude-md-management | claude-plugins-official | CLAUDE.md file management |
| claude-code-setup | claude-plugins-official | Claude Code configuration automation |
| hookify | claude-plugins-official | Create hooks from conversation patterns |
| ralph-loop | claude-plugins-official | Ralph orchestrator integration |
| playground | claude-plugins-official | Interactive code playground |

### Output Styles

| Plugin | Source | Description |
|--------|--------|-------------|
| explanatory-output-style | claude-plugins-official | Educational explanations with insights |
| learning-output-style | claude-plugins-official | Interactive learning mode |

---

## Superpowers Marketplace

Extended capabilities from the Superpowers ecosystem.

| Plugin | Description |
|--------|-------------|
| superpowers | Core superpowers (parallel agents, brainstorming, TDD) |
| superpowers-chrome | Chrome browser automation via DevTools Protocol |
| superpowers-developing-for-claude-code | Claude Code plugin development tools |
| superpowers-lab | Experimental features (tmux, Slack, MCP CLI) |
| elements-of-style | Writing style guide enforcement |
| episodic-memory | Memory across sessions (search conversation history) |

---

## Knowledge Work Plugins

Business and enterprise productivity tools.

| Plugin | Description |
|--------|-------------|
| sales | Sales pipeline, forecasting, call summaries |
| enterprise-search | Cross-platform knowledge search and synthesis |
| productivity | Task management, memory, daily starts |
| finance | Financial statements, journal entries, reconciliation, SOX testing |
| data | Data exploration, visualization, dashboards, SQL queries |
| marketing | Brand review, campaigns, content creation, SEO, performance |
| legal | Contract review, compliance, NDA triage, risk assessment |
| customer-support | Ticket triage, response drafting, knowledge management |
| product-management | Feature specs, roadmaps, sprint planning, stakeholder updates |
| human-resources | Recruiting, onboarding, compensation, performance reviews |
| slack-by-salesforce | Slack channel digest, standup, announcements |
| cowork-plugin-management | Plugin customization and management |

---

## Healthcare Plugins

Specialized for healthcare and life sciences.

| Plugin | Description |
|--------|-------------|
| bio-research | Scientific research tools (bioRxiv, PubMed, clinical trials, ChEMBL) |
| prior-auth-review | Prior authorization review for medical procedures |
| clinical-trial-protocol | Clinical trial protocol development |
| cms-coverage | Medicare coverage policy lookup (NCDs, LCDs) |
| npi-registry | NPI provider lookup and verification |
| icd10-codes | ICD-10-CM/PCS code search and validation |
| pubmed | PubMed article search and retrieval |

---

## DAIR Academy Plugins

AI and creative tools.

| Plugin | Description |
|--------|-------------|
| image-generator | AI image generation |
| llm-council | Multi-LLM council for diverse perspectives |
| apollo | Knowledge work and lead enrichment |

---

## Design Plugins

| Plugin | Description |
|--------|-------------|
| design | Design critique, accessibility, handoff, design systems |
| brand-voice | Brand voice discovery, guidelines, enforcement |

---

## Operations Plugins

| Plugin | Description |
|--------|-------------|
| operations | Process optimization, vendor management, capacity planning, runbooks |

---

## Installation

Plugins are installed via Claude Code's built-in plugin manager:

```bash
# List available plugins
claude plugins list

# Install a plugin
claude plugins install <plugin-name>

# Or enable in settings.json
{
  "enabledPlugins": {
    "superpowers@claude-plugins-official": true,
    "episodic-memory@superpowers-marketplace": true
  }
}
```

## Recommended Starter Set

For a new Claude Code setup, we recommend starting with:

1. **superpowers** - Core enhanced capabilities
2. **coderabbit** - Code review
3. **episodic-memory** - Memory across sessions
4. **superpowers-chrome** - Browser automation
5. **skill-creator** - Create custom skills
6. **commit-commands** - Git workflow
7. **pr-review-toolkit** - PR reviews

These provide a solid foundation for development workflows.
