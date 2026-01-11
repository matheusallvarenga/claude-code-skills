# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2025-01-11

### Major Release - Complete Restructure

This release represents a complete restructure of the repository, adding 27 specialized agents, 22 new skills, and comprehensive MCP documentation.

### Added

#### Skills (22 new skills)

**Document & Office Suite**
- `docx` - Comprehensive DOCX creation, editing, tracked changes, redlining, and comments using python-docx and docx-js
- `pdf` - PDF manipulation toolkit: text extraction, merging, splitting, forms, watermarks, OCR
- `pptx` - PowerPoint creation and editing with templates and styling
- `xlsx` - Excel spreadsheet operations, formulas, and data analysis
- `doc-coauthoring` - Collaborative document editing workflows

**Notion Integration**
- `notion-spec-to-implementation` - Transform product/tech specs into Notion tasks with acceptance criteria
- `notion-meeting-intelligence` - Convert meeting notes to actionable items and follow-ups
- `notion-research-documentation` - Research organization, citation management, and documentation
- `notion-knowledge-capture` - Knowledge base management and information architecture

**Design & Creative**
- `algorithmic-art` - Generative p5.js art with seeded randomness and interactive exploration
- `canvas-design` - Visual design philosophy to PDF/PNG art with museum-quality output
- `theme-factory` - 10 pre-set professional themes (colors/fonts) for artifacts
- `brand-guidelines` - Brand identity and style guide creation
- `frontend-design` - UI/UX design patterns and component systems

**Development & Testing**
- `mcp-builder` - Complete guide for creating MCP servers in Python (FastMCP) or TypeScript
- `webapp-testing` - Playwright-based web application testing with server lifecycle management
- `web-artifacts-builder` - Interactive web artifact creation for demos and prototypes

**Research & Content**
- `internal-comms` - Internal communications templates and best practices

**Data & Audit**
- `itm-audit` - Forensic data audit system with scanning, hashing, deduplication, and classification

#### Agents (27 specialized agents)

**Obsidian/PKM (5)**
- `connection-agent` - Discover and suggest links between notes
- `moc-agent` - Create and maintain Maps of Content
- `metadata-agent` - Standardize frontmatter and metadata
- `tag-agent` - Normalize tag taxonomy
- `review-agent` - Quality assurance for vault enhancements

**Podcast & Media (6)**
- `podcast-content-analyzer` (Opus) - Identify viral moments and engagement potential
- `podcast-metadata-specialist` (Opus) - SEO-optimized show notes and metadata
- `podcast-trend-scout` - Find trending topics and timely content
- `timestamp-precision-specialist` (Opus) - Frame-accurate cut points
- `seo-podcast-optimizer` - SEO optimization for episodes
- `social-media-copywriter` - Social content creation for multiple platforms

**Business & Intelligence (4)**
- `competitive-intelligence-analyst` - Market research, SWOT analysis, competitor tracking
- `market-research-analyst` - Industry analysis and trend identification
- `sales-automator` - Email sequences, proposals, scripts
- `seo-analyzer` - Technical SEO audits and recommendations

**Design & Interface (4)**
- `cli-ui-designer` - Terminal-inspired web interfaces
- `ui-ux-designer` - User-centered design and research
- `visual-analysis-ocr` - Extract and analyze text from images
- `video-editor` (Opus) - Professional video editing with FFmpeg

**Development (6)**
- `prompt-engineer` (Opus) - LLM prompt optimization
- `fullstack-developer` (Opus) - End-to-end application development
- `frontend-developer` - React/Next.js, TypeScript, Tailwind
- `backend-architect` (Opus) - System architecture, APIs, databases
- `code-reviewer` - Code review, security, best practices
- `task-decomposition-expert` - Break down complex tasks

**Management & Curation (2)**
- `context-manager` (Opus) - Multi-agent context management
- `content-curator` - Content quality and curation

#### MCPs (13 documented)

**Cloud APIs (6)**
- Notion - Workspace integration
- Supabase - Backend-as-a-Service
- Figma Desktop - Design tool integration
- shadcn/ui - React/Tailwind components
- Context7 - Expanded context (Upstash)
- Vercel - Deployment platform

**Built-in (6)**
- markitdown - Document conversion
- memory - Persistent memory
- filesystem - File system operations
- github - Repository management
- fetch - HTTP requests
- context7 - Context enhancement

**Custom (1)**
- obsidian-docs - Obsidian documentation server (Node.js)

#### Documentation
- `agents/AGENTS-CATALOG.md` - Complete agent documentation with usage guides
- `mcp/MCP-CATALOG.md` - Complete MCP documentation with configuration examples

### Changed
- Restructured README.md with comprehensive skill/agent/MCP tables
- Updated directory structure to support agents and expanded MCPs
- Improved skill categorization by function

### Compatibility
- Compatible with Claude Code v2.1.0+ (skills hot-reload)
- Supports new Claude Code 2.1.x features:
  - `context: fork` in skills
  - Hooks in skills
  - Agent field specification
  - Auto-continue on token limit

---

## [1.0.0] - 2024-11-07

### Initial Release

#### Added

**Skills (5)**
- `full-stack-project-finisher` - Complete projects from 70% to production
- `github-for-beginners` - Complete GitHub learning path
- `vs-code-for-beginners` - VS Code mastery guide
- `skill-creator` - Meta-skill for creating new skills
- `request-optimizer` - Request analysis and optimization

**MCPs (1)**
- `obsidian.md` - Obsidian workflow optimization

---

## Version History Summary

| Version | Date | Skills | Agents | MCPs |
|---------|------|--------|--------|------|
| 2.0.0 | 2025-01-11 | 27 | 27 | 14 |
| 1.0.0 | 2024-11-07 | 5 | 0 | 1 |

---

## Upgrade Guide

### From 1.0.0 to 2.0.0

1. **Backup existing skills**
   ```bash
   cp -r ~/.claude/skills ~/.claude/skills.backup
   ```

2. **Update skills**
   ```bash
   cp -r skills/* ~/.claude/skills/
   ```

3. **Add agents**
   ```bash
   mkdir -p ~/.claude/agents
   cp agents/*.md ~/.claude/agents/
   ```

4. **Update MCPs** (optional)
   - Review `mcp/MCP-CATALOG.md` for new MCP options
   - Update `~/.claude/mcp.json` as needed

5. **Restart Claude Code** to load new components

---

## Contributors

- Matheus Allvarenga (@matheusallvarenga)

---

## Links

- [Repository](https://github.com/matheusallvarenga/claude-code-skills)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Model Context Protocol](https://modelcontextprotocol.io)
