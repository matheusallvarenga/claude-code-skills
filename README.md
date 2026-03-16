# Claude Code Skills, Agents & MCPs v3.0.0

A comprehensive, installable collection of production-ready skills, specialized agents, slash commands, and MCP integrations for Claude Code.

## Quick Stats

| Resource | Count | Description |
|----------|-------|-------------|
| Skills | 33 | Reusable capability modules |
| Agents | 28 | Specialized AI personas |
| Commands | 45 | Slash commands for workflows |
| Custom MCPs | 1 | obsidian-docs server with source |
| MCP Configs | 9 | Pre-configured server templates |
| Rules | 1 | MCP governance policy |
| Config Templates | 3 | Settings and MCP templates |

## Quick Install

```bash
git clone https://github.com/matheusallvarenga/claude-code-skills.git
cd claude-code-skills
chmod +x install.sh
./install.sh --all
```

See [docs/INSTALLATION-GUIDE.md](docs/INSTALLATION-GUIDE.md) for detailed instructions.

### Selective Install

```bash
./install.sh --skills           # 33 skills only
./install.sh --agents           # 28 agents only
./install.sh --commands         # 45 slash commands
./install.sh --mcps             # Custom MCP servers
./install.sh --all --force      # Everything, no prompts
./install.sh --dry-run          # Preview without changes
```

---

## Skills (33)

### Document & Office Suite (5)

| Skill | Description |
|-------|-------------|
| `docx` | DOCX creation, editing, tracked changes, comments |
| `pdf` | PDF text extraction, merge/split, forms, watermarks |
| `pptx` | PowerPoint creation and editing with templates |
| `xlsx` | Excel operations, formulas, data analysis |
| `doc-coauthoring` | Collaborative document editing workflows |

### Notion Integration (4)

| Skill | Description |
|-------|-------------|
| `notion-spec-to-implementation` | Transform specs into Notion tasks with acceptance criteria |
| `notion-meeting-intelligence` | Convert meetings to action items and follow-ups |
| `notion-research-documentation` | Research organization and documentation |
| `notion-knowledge-capture` | Knowledge base management |

### Design & Creative (5)

| Skill | Description |
|-------|-------------|
| `algorithmic-art` | Generative art with p5.js and seeded randomness |
| `canvas-design` | Visual design to PDF/PNG with 60+ fonts |
| `theme-factory` | 10 professional themes (colors/fonts) |
| `brand-guidelines` | Brand identity and style guides |
| `frontend-design` | UI/UX design patterns and components |

### Development & Testing (5)

| Skill | Description |
|-------|-------------|
| `mcp-builder` | Create MCP servers in Python (FastMCP) or TypeScript |
| `webapp-testing` | Playwright-based web application testing |
| `web-artifacts-builder` | Interactive web artifacts for demos |
| `full-stack-project-finisher` | Complete projects from 70% to production |
| `skill-creator` | Meta-skill for creating new skills |

### Research & Content (4)

| Skill | Description |
|-------|-------------|
| `content-research-writer` | Research, writing, and citation management |
| `lead-research-assistant` | Lead generation and contact strategies |
| `request-optimizer` | **v4.0** Intelligent request analysis and routing |
| `internal-comms` | Internal communications templates |

### Research Orchestration (1)

| Skill | Description |
|-------|-------------|
| `deep-research` | Multi-agent parallel research orchestration |

### Learning & Productivity (3)

| Skill | Description |
|-------|-------------|
| `github-for-beginners` | Complete GitHub learning path |
| `vs-code-for-beginners` | VS Code mastery guide |
| `video-downloader` | Video download from YouTube and other platforms |

### Code Quality (1)

| Skill | Description |
|-------|-------------|
| `code-review` | AI-powered code review with CodeRabbit |

### Discovery (1)

| Skill | Description |
|-------|-------------|
| `find-skills` | Discover and install Claude Code skills |

### Media Production (2)

| Skill | Description |
|-------|-------------|
| `remotion-best-practices` | Video creation in React with Remotion |
| `whisper-transcription` | Audio/video transcription with OpenAI Whisper |

### Data Extraction (1)

| Skill | Description |
|-------|-------------|
| `youtube-transcript` | Extract transcripts from YouTube videos |

### Data & Audit (1)

| Skill | Description |
|-------|-------------|
| `itm-audit` | Forensic data auditing with deduplication |

---

## Agents (28)

### Development Team (6)

| Agent | Model | Description |
|-------|-------|-------------|
| `fullstack-developer` | Opus | Full-stack: React, Node.js, databases, APIs |
| `frontend-developer` | Sonnet | React/Next.js, TypeScript, Tailwind |
| `backend-architect` | Opus | System architecture, microservices, databases |
| `code-reviewer` | Sonnet | Code review, security, best practices |
| `supabase-specialist` | Opus | Supabase: RLS, Edge Functions, LGPD/GDPR |
| `task-decomposition-expert` | Sonnet | Complex task breakdown and orchestration |

### Design & UX (3)

| Agent | Model | Description |
|-------|-------|-------------|
| `cli-ui-designer` | Sonnet | Terminal-inspired web interfaces |
| `ui-ux-designer` | Sonnet | User research, wireframes, design systems |
| `visual-analysis-ocr` | Sonnet | Text extraction from images, OCR |

### Content & Media (6)

| Agent | Model | Description |
|-------|-------|-------------|
| `podcast-content-analyzer` | Opus | Viral moments, chapter markers, engagement |
| `podcast-metadata-specialist` | Sonnet | SEO titles, show notes, publishing metadata |
| `podcast-trend-scout` | Sonnet | Emerging topics, breaking developments |
| `timestamp-precision-specialist` | Sonnet | Frame-accurate cut points, speech detection |
| `seo-podcast-optimizer` | Sonnet | SEO optimization for episodes |
| `social-media-copywriter` | Sonnet | Twitter, LinkedIn, Instagram content |

### Business & Intelligence (4)

| Agent | Model | Description |
|-------|-------|-------------|
| `competitive-intelligence-analyst` | Sonnet | Market research, SWOT, competitor tracking |
| `market-research-analyst` | Sonnet | Industry analysis, trends, strategic insights |
| `sales-automator` | Sonnet | Email sequences, proposals, scripts |
| `seo-analyzer` | Sonnet | Technical SEO audits and recommendations |

### Obsidian/PKM (5)

| Agent | Model | Description |
|-------|-------|-------------|
| `connection-agent` | Sonnet | Knowledge graph links, orphaned notes |
| `moc-agent` | Sonnet | Maps of Content generation |
| `metadata-agent` | Sonnet | Frontmatter standardization |
| `tag-agent` | Sonnet | Tag taxonomy normalization |
| `review-agent` | Sonnet | Vault quality assurance |

### Specialized (4)

| Agent | Model | Description |
|-------|-------|-------------|
| `prompt-engineer` | Opus | LLM prompt optimization |
| `video-editor` | Opus | Video production with FFmpeg |
| `context-manager` | Opus | Multi-agent context management |
| `content-curator` | Sonnet | Content quality and curation |

---

## Commands (45)

### Agent Launchers (11)

| Command | Description |
|---------|-------------|
| `/agent [name]` | Invoke any specialized agent |
| `/prompt-engineer` | LLM prompt optimization (Opus) |
| `/competitive-intel` | Competitive analysis and SWOT |
| `/podcast-analyze` | Podcast content analysis (Opus) |
| `/social-copy` | Social media content creation |
| `/cli-design` | CLI/Terminal interface design |
| `/context-mgr` | Multi-agent context management |
| `/vault-enhance` | Obsidian agent suite |
| `/sales-auto` | Sales and email automation |
| `/market-research` | Market research |
| `/seo-audit` | Technical SEO audit |

### Workflow (7)

| Command | Description |
|---------|-------------|
| `/ship` | Weekly ship protocol |
| `/focus` | Hyperfocus mode |
| `/council` | Archetypal Council (6 voices) |
| `/evaluate` | Friday evaluation |
| `/80-20` | Pareto filter |
| `/session-type` | Switch session type |
| `/export-session` | Export session summary |

### MCP (8)

| Command | Description |
|---------|-------------|
| `/mcp` | List all available MCPs |
| `/notion-mcp` | Notion integration |
| `/supabase-mcp` | Backend-as-a-Service |
| `/shadcn-mcp` | React/Tailwind components |
| `/vercel-mcp` | Deployment and infrastructure |
| `/obsidian-mcp` | Obsidian documentation |
| `/memory-mcp` | Persistent memory |
| `/markitdown-mcp` | Document conversion |

### Development (2)

| Command | Description |
|---------|-------------|
| `/debug` | Quick debug workflow |
| `/optimize` | Code optimization |

### Tools (3)

| Command | Description |
|---------|-------------|
| `/obsidian` | PKM workflow |
| `/notion` | Project management |
| `/miro` | Visual thinking |

### AIOS Project Commands (14)

| Command | Description |
|---------|-------------|
| `/audit` | Data and file auditing |
| `/workflow-orchestrator` | Complex workflow orchestration |
| 12 AIOS agent commands | Scrum Master, Dev, QA, DevOps, PM, PO, Architect, Analyst, Data Engineer, UX Expert, Squad Creator, Master |

---

## MCP Servers

### Configured (9 servers in template)

| Server | Type | Description |
|--------|------|-------------|
| Notion | Cloud API | Workspace document integration |
| Supabase | Cloud API | Database, auth, Edge Functions |
| Figma Desktop | Local | Design tool integration |
| shadcn/ui | NPX | React/Tailwind components |
| Context7 | NPX | Library documentation lookup |
| Vercel | Cloud API | Deployment platform |
| n8n | NPX Gateway | Automation workflows |
| Tavily | Cloud API | Web search API |
| Slack | Cloud API | Messaging integration |

### Custom MCP (included with source)

| Server | Description |
|--------|-------------|
| `obsidian-docs` | Node.js MCP for Obsidian syntax, plugins, and API documentation |

### Built-in (enabled via settings)

markitdown, memory, filesystem, context7, github, fetch

---

## Configuration Templates

| Template | Purpose |
|----------|---------|
| `mcp.json.template` | MCP server configuration with placeholder keys |
| `settings.json.template` | Project settings with recommended plugins |
| `settings.local.json.template` | Local settings with expanded permissions |

---

## Plugins

See [docs/PLUGINS-GUIDE.md](docs/PLUGINS-GUIDE.md) for 70+ recommended plugins organized by category, including official, superpowers, knowledge work, healthcare, and creative plugins.

---

## Directory Structure

```
claude-code-skills/
├── README.md
├── CHANGELOG.md
├── install.sh                # Automated installer
├── skills/ (33)              # Skill modules
├── agents/ (28 + catalog)    # Agent definitions
├── commands/
│   ├── project/ (14)         # Project-scope commands
│   └── global/ (31)          # Global commands
├── mcp/
│   ├── MCP-CATALOG.md        # MCP documentation
│   ├── obsidian-docs/        # Custom MCP source
│   └── templates/            # Config templates
├── rules/
│   └── mcp-usage.md          # MCP governance
├── templates/                # Settings templates
└── docs/
    ├── PLUGINS-GUIDE.md      # Plugin recommendations
    └── INSTALLATION-GUIDE.md # Setup guide
```

---

## Requirements

- Claude Code v2.1.0+ (skills hot-reload support)
- Node.js 18+ (for obsidian-docs MCP)
- macOS or Linux (Windows via WSL)

---

## Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feat/new-skill`)
3. Add your skill to `skills/` with a `SKILL.md` file
4. Update this README
5. Submit a Pull Request

---

## License

This project is open source. Individual skills may include their own licenses.

---

## Author

Matheus Allvarenga ([@matheusallvarenga](https://github.com/matheusallvarenga))
