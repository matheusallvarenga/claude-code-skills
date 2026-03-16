#!/usr/bin/env bash
# claude-code-skills installer v3.0.0
# Usage: ./install.sh [--skills] [--agents] [--commands] [--mcps] [--rules] [--templates] [--all]
#
# Installs Claude Code resources (skills, agents, commands, MCPs, rules, templates)
# into the appropriate directories for immediate use.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_GLOBAL="${HOME}/.claude"
CLAUDE_PROJECT=".claude"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

# Counters
INSTALLED=0
SKIPPED=0

# ─── Helpers ───────────────────────────────────────────────

info()    { echo -e "${GREEN}[+]${NC} $1"; }
warn()    { echo -e "${YELLOW}[!]${NC} $1"; }
error()   { echo -e "${RED}[x]${NC} $1"; }
header()  { echo -e "\n${BLUE}${BOLD}=== $1 ===${NC}\n"; }

confirm_overwrite() {
    local target="$1"
    if [ -d "$target" ] || [ -f "$target" ]; then
        echo -en "${YELLOW}[!]${NC} '$target' already exists. Overwrite? [y/N] "
        read -r reply
        if [[ ! "$reply" =~ ^[Yy]$ ]]; then
            warn "Skipped: $target"
            ((SKIPPED++))
            return 1
        fi
    fi
    return 0
}

usage() {
    cat <<EOF
${BOLD}claude-code-skills installer v3.0.0${NC}

Usage: ./install.sh [OPTIONS]

Options:
  --skills      Install 33 skills to ~/.claude/skills/
  --agents      Install 28 agents to ~/.claude/agents/
  --commands    Install slash commands (global + project)
  --mcps        Install custom MCP servers and config templates
  --rules       Install governance rules to .claude/rules/
  --templates   Copy configuration templates to .claude/
  --all         Install everything (default if no flags)
  --force       Skip overwrite confirmations
  --dry-run     Show what would be installed without doing it
  -h, --help    Show this help

Examples:
  ./install.sh --all              # Install everything
  ./install.sh --skills --agents  # Install only skills and agents
  ./install.sh --all --force      # Install everything, no prompts

Directories:
  Skills & Agents  -> ~/.claude/          (global, all projects)
  Global Commands  -> ~/.claude/commands/ (global, all projects)
  Project Commands -> .claude/commands/   (current project only)
  Rules & Templates-> .claude/            (current project only)
EOF
}

# ─── Install Functions ─────────────────────────────────────

install_skills() {
    header "Installing Skills (33)"
    mkdir -p "${CLAUDE_GLOBAL}/skills"

    for skill_dir in "${SCRIPT_DIR}/skills/"*/; do
        [ ! -d "$skill_dir" ] && continue
        local skill_name
        skill_name=$(basename "$skill_dir")
        local target="${CLAUDE_GLOBAL}/skills/${skill_name}"

        if [ "$FORCE" = true ] || confirm_overwrite "$target"; then
            rsync -a --exclude='.DS_Store' --exclude='__pycache__' \
                --exclude='node_modules' --exclude='data/*.json' \
                "$skill_dir" "$target/"
            info "  ${skill_name}"
            ((INSTALLED++))
        fi
    done
}

install_agents() {
    header "Installing Agents (28)"
    mkdir -p "${CLAUDE_GLOBAL}/agents"

    for agent_file in "${SCRIPT_DIR}/agents/"*.md; do
        [ ! -f "$agent_file" ] && continue
        local agent_name
        agent_name=$(basename "$agent_file")
        local target="${CLAUDE_GLOBAL}/agents/${agent_name}"

        if [ "$FORCE" = true ] || confirm_overwrite "$target"; then
            cp "$agent_file" "$target"
            info "  ${agent_name}"
            ((INSTALLED++))
        fi
    done
}

install_commands() {
    header "Installing Commands"

    # Global commands -> ~/.claude/commands/
    if [ -d "${SCRIPT_DIR}/commands/global" ]; then
        info "Global commands -> ~/.claude/commands/"
        mkdir -p "${CLAUDE_GLOBAL}/commands"
        rsync -a --exclude='.DS_Store' \
            "${SCRIPT_DIR}/commands/global/" "${CLAUDE_GLOBAL}/commands/"
        local global_count
        global_count=$(find "${SCRIPT_DIR}/commands/global" -name "*.md" | wc -l | tr -d ' ')
        info "  ${global_count} global commands installed"
        INSTALLED=$((INSTALLED + global_count))
    fi

    # Project commands -> .claude/commands/ (current directory)
    if [ -d "${SCRIPT_DIR}/commands/project" ]; then
        info "Project commands -> .claude/commands/"
        mkdir -p "${CLAUDE_PROJECT}/commands"
        rsync -a --exclude='.DS_Store' \
            "${SCRIPT_DIR}/commands/project/" "${CLAUDE_PROJECT}/commands/"
        local project_count
        project_count=$(find "${SCRIPT_DIR}/commands/project" -name "*.md" | wc -l | tr -d ' ')
        info "  ${project_count} project commands installed"
        INSTALLED=$((INSTALLED + project_count))
    fi
}

install_mcps() {
    header "Installing Custom MCPs"

    # obsidian-docs MCP
    if [ -d "${SCRIPT_DIR}/mcp/obsidian-docs" ]; then
        local target="${CLAUDE_GLOBAL}/mcps/obsidian-docs"
        mkdir -p "${CLAUDE_GLOBAL}/mcps"

        if [ "$FORCE" = true ] || confirm_overwrite "$target"; then
            rsync -a --exclude='.DS_Store' --exclude='node_modules' \
                "${SCRIPT_DIR}/mcp/obsidian-docs/" "$target/"
            info "  obsidian-docs MCP installed"
            warn "  Run: cd ~/.claude/mcps/obsidian-docs && npm install"
            ((INSTALLED++))
        fi
    fi

    # MCP config template
    if [ -f "${SCRIPT_DIR}/mcp/templates/mcp.json.template" ]; then
        local target="${CLAUDE_PROJECT}/mcp.json.template"
        cp "${SCRIPT_DIR}/mcp/templates/mcp.json.template" "$target"
        info "  mcp.json.template copied to ${CLAUDE_PROJECT}/"
        warn "  Rename to mcp.json and fill in your API keys"
        ((INSTALLED++))
    fi
}

install_rules() {
    header "Installing Rules"
    mkdir -p "${CLAUDE_PROJECT}/rules"

    for rule_file in "${SCRIPT_DIR}/rules/"*.md; do
        [ ! -f "$rule_file" ] && continue
        local rule_name
        rule_name=$(basename "$rule_file")
        cp "$rule_file" "${CLAUDE_PROJECT}/rules/${rule_name}"
        info "  ${rule_name}"
        ((INSTALLED++))
    done
}

install_templates() {
    header "Installing Configuration Templates"

    for tmpl_file in "${SCRIPT_DIR}/templates/"*.template; do
        [ ! -f "$tmpl_file" ] && continue
        local tmpl_name
        tmpl_name=$(basename "$tmpl_file")
        cp "$tmpl_file" "${CLAUDE_PROJECT}/${tmpl_name}"
        info "  ${tmpl_name}"
        ((INSTALLED++))
    done

    warn "Rename .template files and fill in your values before using"
}

# ─── Main ──────────────────────────────────────────────────

FORCE=false
DRY_RUN=false
DO_SKILLS=false
DO_AGENTS=false
DO_COMMANDS=false
DO_MCPS=false
DO_RULES=false
DO_TEMPLATES=false
DO_ALL=false

# Parse arguments
if [ $# -eq 0 ]; then
    DO_ALL=true
fi

while [ $# -gt 0 ]; do
    case "$1" in
        --skills)    DO_SKILLS=true ;;
        --agents)    DO_AGENTS=true ;;
        --commands)  DO_COMMANDS=true ;;
        --mcps)      DO_MCPS=true ;;
        --rules)     DO_RULES=true ;;
        --templates) DO_TEMPLATES=true ;;
        --all)       DO_ALL=true ;;
        --force)     FORCE=true ;;
        --dry-run)   DRY_RUN=true ;;
        -h|--help)   usage; exit 0 ;;
        *)           error "Unknown option: $1"; usage; exit 1 ;;
    esac
    shift
done

if [ "$DO_ALL" = true ]; then
    DO_SKILLS=true
    DO_AGENTS=true
    DO_COMMANDS=true
    DO_MCPS=true
    DO_RULES=true
    DO_TEMPLATES=true
fi

# Header
echo -e "\n${BOLD}claude-code-skills installer v3.0.0${NC}"
echo -e "Source: ${SCRIPT_DIR}\n"

if [ "$DRY_RUN" = true ]; then
    warn "DRY RUN - no changes will be made"
    echo ""
    [ "$DO_SKILLS" = true ]    && echo "  Would install: 33 skills -> ~/.claude/skills/"
    [ "$DO_AGENTS" = true ]    && echo "  Would install: 28 agents -> ~/.claude/agents/"
    [ "$DO_COMMANDS" = true ]  && echo "  Would install: 45 commands -> ~/.claude/commands/ + .claude/commands/"
    [ "$DO_MCPS" = true ]      && echo "  Would install: 1 custom MCP + config template"
    [ "$DO_RULES" = true ]     && echo "  Would install: 1 rule -> .claude/rules/"
    [ "$DO_TEMPLATES" = true ] && echo "  Would install: 2 config templates -> .claude/"
    echo ""
    exit 0
fi

# Execute
[ "$DO_SKILLS" = true ]    && install_skills
[ "$DO_AGENTS" = true ]    && install_agents
[ "$DO_COMMANDS" = true ]  && install_commands
[ "$DO_MCPS" = true ]      && install_mcps
[ "$DO_RULES" = true ]     && install_rules
[ "$DO_TEMPLATES" = true ] && install_templates

# Summary
header "Installation Complete"
info "Installed: ${INSTALLED} resources"
[ "$SKIPPED" -gt 0 ] && warn "Skipped: ${SKIPPED} resources (already existed)"

echo ""
echo -e "${BOLD}Next steps:${NC}"
echo "  1. Review installed files in ~/.claude/ and .claude/"
echo "  2. Rename .template files and add your API keys"
echo "  3. Run 'cd ~/.claude/mcps/obsidian-docs && npm install' (if MCPs installed)"
echo "  4. Restart Claude Code to load new resources"
echo ""
