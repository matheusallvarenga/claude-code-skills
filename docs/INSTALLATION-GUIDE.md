# Installation Guide - claude-code-skills v3.0.0

Complete step-by-step guide for installing all Claude Code resources.

---

## Prerequisites

- **Claude Code** CLI installed and working
- **Node.js** 18+ (for obsidian-docs MCP)
- **macOS or Linux** (Windows users: use WSL)

---

## Quick Install

```bash
# 1. Clone the repository
git clone https://github.com/matheusallvarenga/claude-code-skills.git
cd claude-code-skills

# 2. Run the installer
chmod +x install.sh
./install.sh --all
```

This installs everything: 33 skills, 28 agents, 45 commands, 1 custom MCP, rules, and templates.

---

## Selective Install

Install only what you need:

```bash
./install.sh --skills           # 33 skills only
./install.sh --agents           # 28 agents only
./install.sh --commands         # 45 slash commands
./install.sh --mcps             # Custom MCP servers
./install.sh --rules            # Governance rules
./install.sh --templates        # Configuration templates
./install.sh --skills --agents  # Combine flags
./install.sh --all --force      # Install all, skip confirmations
./install.sh --dry-run          # Preview without installing
```

---

## What Gets Installed Where

| Resource | Destination | Scope |
|----------|-------------|-------|
| Skills (33) | `~/.claude/skills/` | Global (all projects) |
| Agents (28) | `~/.claude/agents/` | Global (all projects) |
| Global Commands (31) | `~/.claude/commands/` | Global (all projects) |
| Project Commands (14) | `.claude/commands/` | Current project only |
| Custom MCPs | `~/.claude/mcps/` | Global (all projects) |
| Rules | `.claude/rules/` | Current project only |
| Templates | `.claude/` | Current project only |

---

## Manual Install

If you prefer manual installation:

### Skills

```bash
# Copy all skills
cp -r skills/* ~/.claude/skills/

# Or copy individual skills
cp -r skills/docx ~/.claude/skills/
cp -r skills/pdf ~/.claude/skills/
```

### Agents

```bash
# Copy all agents
cp agents/*.md ~/.claude/agents/
```

### Commands

```bash
# Global commands (available in all projects)
cp -r commands/global/* ~/.claude/commands/

# Project commands (current project only)
mkdir -p .claude/commands
cp -r commands/project/* .claude/commands/
```

### Custom MCPs

```bash
# obsidian-docs MCP
mkdir -p ~/.claude/mcps
cp -r mcp/obsidian-docs ~/.claude/mcps/
cd ~/.claude/mcps/obsidian-docs && npm install

# Clone Obsidian docs for the MCP to read
cd /tmp/claude
git clone --depth 1 https://github.com/obsidianmd/obsidian-developer-docs.git obsidian-docs
```

### Rules

```bash
mkdir -p .claude/rules
cp rules/*.md .claude/rules/
```

---

## Post-Installation Setup

### 1. Configure MCP Servers

Copy the template and fill in your API keys:

```bash
cp mcp/templates/mcp.json.template .claude/mcp.json
```

Edit `.claude/mcp.json` and replace:
- `<YOUR_SUPABASE_PROJECT_REF>` with your Supabase project ref
- `<YOUR_SUPABASE_PAT>` with your Supabase PAT token
- `<YOUR_N8N_DOMAIN>` with your n8n domain (if using)
- Set `TAVILY_API_KEY` environment variable (if using Tavily)

### 2. Configure Settings

Copy templates and customize:

```bash
cp templates/settings.json.template .claude/settings.json
cp templates/settings.local.json.template .claude/settings.local.json
```

Adjust permissions, enabled MCPs, and plugins as needed.

### 3. Install obsidian-docs MCP Dependencies

```bash
cd ~/.claude/mcps/obsidian-docs
npm install
```

### 4. Install Recommended Plugins

See `docs/PLUGINS-GUIDE.md` for the full list. Quick start:

```bash
# Via Claude Code
claude plugins install superpowers
claude plugins install coderabbit
claude plugins install episodic-memory
```

### 5. Restart Claude Code

After installation, restart Claude Code to load all new resources:

```bash
# Close and reopen, or:
claude --restart
```

---

## Verifying Installation

```bash
# Check skills
ls ~/.claude/skills/ | wc -l    # Should show 33

# Check agents
ls ~/.claude/agents/*.md | wc -l  # Should show 29 (28 agents + catalog)

# Check commands
ls ~/.claude/commands/ | wc -l    # Should show command directories

# Test a skill
# Open Claude Code and type: /ship (should activate the weekly ship protocol)

# Test an agent
# Open Claude Code and type: /agent fullstack-developer
```

---

## Updating

To update to the latest version:

```bash
cd claude-code-skills
git pull origin main
./install.sh --all --force
```

---

## Troubleshooting

### Skills not loading
- Verify files are in `~/.claude/skills/`
- Check that each skill has a `SKILL.md` file
- Restart Claude Code

### Commands not showing
- Global commands go in `~/.claude/commands/`
- Project commands go in `.claude/commands/` (relative to project root)
- Each command needs a `.md` file

### MCP server not connecting
- Check `~/.claude/mcps/obsidian-docs/node_modules` exists
- Verify the path in your `mcp.json` matches the actual file location
- Check Claude Code logs for connection errors

### Agents not activating
- Verify `.md` files are in `~/.claude/agents/`
- Use `/agent <name>` to activate
- Check the agent file has valid markdown with YAML frontmatter

---

## Directory Structure After Installation

```
~/.claude/
├── agents/                    # 28 agent definitions + catalog
│   ├── backend-architect.md
│   ├── fullstack-developer.md
│   ├── ...
│   └── AGENTS-CATALOG.md
├── skills/                    # 33 skill directories
│   ├── algorithmic-art/
│   ├── code-review/
│   ├── deep-research/
│   ├── docx/
│   ├── ...
│   └── youtube-transcript/
├── commands/                  # 31 global slash commands
│   ├── agents/
│   ├── dev/
│   ├── mcps/
│   ├── tools/
│   └── workflow/
└── mcps/                      # Custom MCP servers
    └── obsidian-docs/

.claude/                       # (in your project root)
├── commands/                  # 14 project-specific commands
│   ├── audit.md
│   ├── workflow-orchestrator.md
│   └── AIOS/agents/          # 12 AIOS agent commands
├── rules/
│   └── mcp-usage.md           # MCP governance rules
├── mcp.json                   # MCP server configuration
├── settings.json              # Project settings
└── settings.local.json        # Local overrides (git-ignored)
```
