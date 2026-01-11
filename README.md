# Claude Code Skills, Agents & MCPs

A comprehensive collection of production-ready skills, specialized agents, and Model Context Protocols (MCPs) for Claude Code, designed to extend Claude's capabilities with specialized workflows, domain expertise, and tool integrations.

## Quick Stats

| Category | Count | Status |
|----------|-------|--------|
| **Skills** | 27 | Production Ready |
| **Agents** | 27 | Production Ready |
| **MCPs** | 14 | Production Ready |

---

## What's Included

### Skills (27)

Skills are modular, self-contained packages that extend Claude's capabilities with specialized knowledge and workflows.

#### Document & Office Suite (5)
| Skill | Description |
|-------|-------------|
| `docx` | Comprehensive DOCX creation, editing, tracked changes, and comments |
| `pdf` | PDF manipulation: text extraction, merging, splitting, forms |
| `pptx` | PowerPoint creation and editing with templates |
| `xlsx` | Excel spreadsheet operations and data analysis |
| `doc-coauthoring` | Collaborative document editing workflows |

#### Notion Integration (4)
| Skill | Description |
|-------|-------------|
| `notion-spec-to-implementation` | Transform specs into implementation tasks |
| `notion-meeting-intelligence` | Meeting notes to actionable items |
| `notion-research-documentation` | Research organization and documentation |
| `notion-knowledge-capture` | Knowledge base management |

#### Design & Creative (5)
| Skill | Description |
|-------|-------------|
| `algorithmic-art` | Generative p5.js art with seeded randomness |
| `canvas-design` | Visual design philosophy to PDF/PNG art |
| `theme-factory` | 10 pre-set professional themes for artifacts |
| `brand-guidelines` | Brand identity and style guide creation |
| `frontend-design` | UI/UX design patterns and components |

#### Development & Testing (5)
| Skill | Description |
|-------|-------------|
| `mcp-builder` | Guide for creating MCP servers (Python/TypeScript) |
| `webapp-testing` | Playwright-based web application testing |
| `web-artifacts-builder` | Interactive web artifact creation |
| `full-stack-project-finisher` | Complete projects from 70% to production |
| `skill-creator` | Meta-skill for creating new skills |

#### Research & Content (4)
| Skill | Description |
|-------|-------------|
| `content-research-writer` | Writing partner with research and citations |
| `lead-research-assistant` | Lead identification and qualification |
| `request-optimizer` | Request analysis and optimization |
| `internal-comms` | Internal communications templates |

#### Learning & Productivity (3)
| Skill | Description |
|-------|-------------|
| `github-for-beginners` | Complete GitHub learning path |
| `vs-code-for-beginners` | VS Code mastery guide |
| `video-downloader` | Video download from various platforms |

#### Data & Audit (1)
| Skill | Description |
|-------|-------------|
| `itm-audit` | Forensic data audit and deduplication system |

---

### Agents (27)

Specialized agents are pre-configured AI personas optimized for specific tasks. See `agents/AGENTS-CATALOG.md` for complete documentation.

#### By Category

**Obsidian/PKM (5)**
| Agent | Model | Purpose |
|-------|-------|---------|
| `connection-agent` | Sonnet | Discover links between notes |
| `moc-agent` | Sonnet | Create Maps of Content |
| `metadata-agent` | Sonnet | Standardize frontmatter |
| `tag-agent` | Sonnet | Normalize tag taxonomy |
| `review-agent` | Sonnet | QA for vault enhancements |

**Podcast & Media (6)**
| Agent | Model | Purpose |
|-------|-------|---------|
| `podcast-content-analyzer` | Opus | Identify viral moments |
| `podcast-metadata-specialist` | Opus | Show notes & SEO |
| `podcast-trend-scout` | Sonnet | Find trending topics |
| `timestamp-precision-specialist` | Opus | Frame-accurate cuts |
| `seo-podcast-optimizer` | Sonnet | SEO for episodes |
| `social-media-copywriter` | Sonnet | Social content creation |

**Business & Intelligence (4)**
| Agent | Model | Purpose |
|-------|-------|---------|
| `competitive-intelligence-analyst` | Sonnet | Market research & SWOT |
| `market-research-analyst` | Sonnet | Industry analysis |
| `sales-automator` | Sonnet | Email sequences & scripts |
| `seo-analyzer` | Sonnet | Technical SEO audits |

**Design & Interface (4)**
| Agent | Model | Purpose |
|-------|-------|---------|
| `cli-ui-designer` | Sonnet | Terminal-style interfaces |
| `ui-ux-designer` | Sonnet | User-centered design |
| `visual-analysis-ocr` | Sonnet | Extract text from images |
| `video-editor` | Opus | Professional video editing |

**Development (6)**
| Agent | Model | Purpose |
|-------|-------|---------|
| `prompt-engineer` | Opus | Optimize LLM prompts |
| `fullstack-developer` | Opus | End-to-end application development |
| `frontend-developer` | Sonnet | React/Next.js, TypeScript, Tailwind |
| `backend-architect` | Opus | System architecture, APIs, databases |
| `code-reviewer` | Sonnet | Code review, best practices, security |
| `task-decomposition-expert` | Sonnet | Break down complex tasks |

**Management & Curation (2)**
| Agent | Model | Purpose |
|-------|-------|---------|
| `context-manager` | Opus | Multi-agent context management |
| `content-curator` | Sonnet | Content quality & curation |

---

### MCPs (14)

Model Context Protocols allow Claude Code to connect to external services. See `mcp/MCP-CATALOG.md` for complete documentation.

**Cloud APIs (6)**
| MCP | Description |
|-----|-------------|
| `notion` | Workspace integration (docs, databases) |
| `supabase` | Backend-as-a-Service (DB, auth, storage) |
| `figma-desktop` | Design tool integration (local) |
| `shadcn` | React/Tailwind components (npx) |
| `context7` | Expanded context (Upstash) |
| `vercel` | Deployment platform |

**Built-in (6)**
| MCP | Description |
|-----|-------------|
| `markitdown` | Document conversion (PDF, DOCX, etc.) |
| `memory` | Persistent memory between sessions |
| `filesystem` | File system operations |
| `github` | Repository management |
| `fetch` | HTTP requests |
| `context7` | Context enhancement |

**Custom (1)**
| MCP | Description |
|-----|-------------|
| `obsidian-docs` | Obsidian documentation server (Node.js) |

**Development (1)**
| MCP | Description |
|-----|-------------|
| `genkit` | Google AI development framework |

---

## Quick Start

### Using a Skill

1. **Copy the skill to your Claude environment:**
   ```bash
   cp -r skills/[skill-name] ~/.claude/skills/
   ```

2. **Use in Claude Code:**
   - Skills are automatically available after copying (hot-reload in v2.1.0+)
   - Reference the skill in your prompts or use `/skill-name`

3. **Check the skill:**
   - Read `SKILL.md` for instructions
   - Read `README.md` for overview (if available)

### Using an Agent

1. **Copy the agent to your Claude environment:**
   ```bash
   cp agents/[agent-name].md ~/.claude/agents/
   ```

2. **Invoke in Claude Code:**
   - Agents activate based on task context
   - Use `/agent [agent-name]` to invoke directly

### Using an MCP

1. **Add to your MCP configuration:**
   ```bash
   # Edit ~/.claude/mcp.json
   ```

2. **Enable in settings:**
   ```bash
   # Edit ~/.claude/settings.json
   ```

3. **Restart Claude Code**

---

## Directory Structure

```
claude-code-skills/
├── README.md
├── CHANGELOG.md
├── .gitignore
├── skills/                              # 27 skills
│   ├── algorithmic-art/                 # Generative p5.js art
│   ├── brand-guidelines/                # Brand identity
│   ├── canvas-design/                   # Visual design to art
│   ├── content-research-writer/         # Research & writing
│   ├── doc-coauthoring/                 # Collaborative editing
│   ├── docx/                            # Word document operations
│   ├── frontend-design/                 # UI/UX patterns
│   ├── full-stack-project-finisher/     # Project completion
│   ├── github-for-beginners/            # GitHub learning
│   ├── internal-comms/                  # Internal communications
│   ├── itm-audit/                       # Data audit system
│   ├── lead-research-assistant/         # Lead research
│   ├── mcp-builder/                     # MCP server creation
│   ├── notion-knowledge-capture/        # Notion knowledge base
│   ├── notion-meeting-intelligence/     # Meeting to actions
│   ├── notion-research-documentation/   # Research docs
│   ├── notion-spec-to-implementation/   # Spec to tasks
│   ├── pdf/                             # PDF manipulation
│   ├── pptx/                            # PowerPoint operations
│   ├── request-optimizer/               # Request optimization
│   ├── skill-creator/                   # Create new skills
│   ├── theme-factory/                   # Professional themes
│   ├── video-downloader/                # Video download
│   ├── vs-code-for-beginners/           # VS Code learning
│   ├── web-artifacts-builder/           # Web artifacts
│   ├── webapp-testing/                  # Playwright testing
│   └── xlsx/                            # Excel operations
├── agents/                              # 27 agents
│   ├── AGENTS-CATALOG.md                # Full documentation
│   ├── backend-architect.md
│   ├── cli-ui-designer.md
│   ├── code-reviewer.md
│   ├── competitive-intelligence-analyst.md
│   ├── connection-agent.md
│   ├── content-curator.md
│   ├── context-manager.md
│   ├── frontend-developer.md
│   ├── fullstack-developer.md
│   ├── market-research-analyst.md
│   ├── metadata-agent.md
│   ├── moc-agent.md
│   ├── podcast-content-analyzer.md
│   ├── podcast-metadata-specialist.md
│   ├── podcast-trend-scout.md
│   ├── prompt-engineer.md
│   ├── review-agent.md
│   ├── sales-automator.md
│   ├── seo-analyzer.md
│   ├── seo-podcast-optimizer.md
│   ├── social-media-copywriter.md
│   ├── tag-agent.md
│   ├── task-decomposition-expert.md
│   ├── timestamp-precision-specialist.md
│   ├── ui-ux-designer.md
│   ├── video-editor.md
│   └── visual-analysis-ocr.md
└── mcp/                                 # MCP configurations
    ├── MCP-CATALOG.md                   # Full documentation
    └── obsidian.md                      # Obsidian workflow MCP
```

---

## Skill Design Philosophy

These skills follow best practices:

- **Progressive Disclosure**: Information loads in 3 levels (metadata -> SKILL.md -> resources)
- **No Duplication**: Information lives in SKILL.md OR references, not both
- **Imperative Form**: Use verb-first instructions, not second person
- **Self-Contained**: Each skill works independently
- **Reusable**: Designed for different users and projects

---

## Agent Design Principles

Agents are optimized for:

- **Single Responsibility**: Each agent has one clear purpose
- **Model Selection**: Opus for complex tasks, Sonnet for general use
- **Tool Access**: Only necessary tools are enabled
- **Proactive Activation**: Agents activate when relevant to task

---

## Compatibility

- **Claude Code**: v2.1.0+ (hot-reload support)
- **Skills Hot-Reload**: Automatic (place in `~/.claude/skills/`)
- **MCP Protocol**: Compatible with Claude Code MCP specification

---

## Contributing

To contribute improvements:

1. Fork this repository
2. Create a feature branch
3. Make improvements
4. Test thoroughly
5. Submit a pull request

---

## License

All skills, agents, and MCPs are provided under the MIT License unless otherwise specified in individual LICENSE.txt files.

---

## Related Resources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)
- [Claude Code Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

---

**Created**: 2024-11-07
**Last Updated**: 2025-01-11
**Version**: 2.0.0
**Total Skills**: 27
**Total Agents**: 27
**Total MCPs**: 14
**Status**: Production Ready
