# Claude Code Skills & MCPs

A collection of production-ready skills and Model Context Protocols (MCPs) for Claude Code, designed to extend Claude's capabilities with specialized workflows, domain expertise, and tool integrations.

## 📚 What's Included

### Skills

Skills are modular, self-contained packages that extend Claude's capabilities with specialized knowledge and workflows.

#### 1. **Full-Stack Project Finisher**
- **Purpose**: Help developers complete projects from 70-100% to production-ready status
- **Use Cases**: Project completion, gap analysis, database design, API specifications, testing strategies
- **Contents**: Scripts for analysis, references for design patterns, deployment checklists
- **Size**: 188 KB | **Status**: Production Ready
- **Location**: `skills/full-stack-project-finisher/`

#### 2. **GitHub for Beginners**
- **Purpose**: Comprehensive learning path for Git and GitHub fundamentals
- **Use Cases**: Teaching Git concepts, PR creation, merge conflict resolution, GitHub workflows
- **Contents**: Reference guides, troubleshooting, mental models, hands-on workflows
- **Size**: 88 KB | **Status**: Production Ready
- **Location**: `skills/github-for-beginners/`

#### 3. **VS Code for Beginners**
- **Purpose**: Master VS Code editor and markdown editing
- **Use Cases**: Learning editor features, keyboard efficiency, workspace setup, Warp terminal integration
- **Contents**: Interface guides, keyboard shortcuts, extensions, markdown workflows
- **Size**: 144 KB | **Status**: Production Ready
- **Location**: `skills/vs-code-for-beginners/`

#### 4. **Skill Creator**
- **Purpose**: Meta-skill for creating new skills (teaches skill design methodology)
- **Use Cases**: Creating custom skills, packaging skills for distribution, skill validation
- **Contents**: 6-step creation process, templates, validation scripts, packaging tools
- **Size**: 44 KB | **Status**: Production Ready
- **Location**: `skills/skill-creator/`

#### 5. **Request Optimizer** (NEW!)
- **Purpose**: Intelligent request analysis for context optimization and workflow strategy
- **Use Cases**: Analyzing complex requests, decomposing tasks, recommending execution strategies, managing token budget
- **Contents**: 5-point analysis framework, decision trees, approval gates, real-world examples
- **Size**: 40 KB | **Status**: Proof of Concept (v1.0)
- **Location**: `skills/request-optimizer/`

### MCPs (Model Context Protocols)

#### **obsidian.md**
- **Purpose**: Obsidian workflow optimization following best practices and official documentation
- **Use Cases**: Personal knowledge management, note structure, tagging strategies, daily notes, plugin usage
- **Contents**: Core principles, syntax reference, workflow patterns, plugin ecosystem guidance
- **Size**: 3.8 KB | **Status**: Production Ready
- **Location**: `mcp/obsidian.md`

## 🚀 Quick Start

### Using a Skill

1. **Copy the skill to your Claude environment:**
   ```bash
   cp -r skills/[skill-name] ~/.claude/skills/
   ```

2. **Use in Claude Code:**
   - Skills are automatically available after copying to `~/.claude/skills/`
   - They'll activate when relevant to your task

3. **Reference the skill:**
   - Check the `SKILL.md` in each skill folder for exact usage instructions
   - Read `README.md` for overview and examples

### Using an MCP

1. **Copy the MCP command to your Claude environment:**
   ```bash
   cp mcp/obsidian.md ~/.claude/commands/
   ```

2. **Use in Claude Code:**
   - MCPs are automatically available after copying to `~/.claude/commands/`
   - Reference in your prompts or workflows

## 📁 Directory Structure

```
claude-code-skills/
├── README.md (this file)
├── .gitignore
├── skills/
│   ├── full-stack-project-finisher/
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   ├── scripts/
│   │   ├── references/
│   │   └── assets/
│   ├── github-for-beginners/
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   ├── references/
│   │   └── assets/
│   ├── vs-code-for-beginners/
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   ├── references/
│   │   └── assets/
│   ├── skill-creator/
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   ├── scripts/
│   │   └── LICENSE.txt
│   └── request-optimizer/
│       ├── SKILL.md
│       ├── README.md
│       ├── POC-SUMMARY.md
│       └── references/
└── mcp/
    └── obsidian.md
```

## 🎓 Learning Path

**New to Claude Code?** Start here:
1. Read `skills/github-for-beginners/` - Learn Git fundamentals
2. Read `skills/vs-code-for-beginners/` - Master your editor
3. Use `skills/full-stack-project-finisher/` - Complete a project
4. Read `skills/skill-creator/` - Learn to create custom skills

## 🔧 Understanding Skill Structure

Each skill follows this structure:

- **SKILL.md**: Official skill definition with YAML frontmatter (name, description) and instructions
- **README.md**: Quick start guide, overview, and examples
- **scripts/**: Executable code (Python, Bash) for deterministic tasks
- **references/**: Documentation and reference material to load into context
- **assets/**: Templates, boilerplate, icons, and other output files

## 💡 Skill Design Philosophy

These skills follow best practices:

- **Progressive Disclosure**: Information loads in 3 levels (metadata → SKILL.md → resources)
- **No Duplication**: Information lives in SKILL.md OR references, not both
- **Imperative Form**: Use verb-first instructions, not second person
- **Self-Contained**: Each skill works independently
- **Reusable**: Designed for different users and projects

## 🤝 Contributing

To contribute improvements to existing skills:

1. Fork this repository
2. Create a feature branch
3. Make improvements to the skill
4. Test thoroughly
5. Submit a pull request with description of changes

## 📄 License

All skills and MCPs are provided under the MIT License. See individual skill folders for details.

## 🔗 Related Resources

- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)
- [Obsidian Official Docs](https://docs.obsidian.md)
- [GitHub Docs](https://docs.github.com)

## 💬 Questions?

Each skill includes detailed documentation:
- Check the specific skill's `SKILL.md` for implementation details
- Read `references/` for deep dives into methodology
- Review examples in `README.md` files

---

**Created**: 2025-11-07
**Last Updated**: 2025-11-07
**Total Skills**: 5
**Total MCPs**: 1
**Status**: Ready for production use

Enjoy extending Claude's capabilities! 🚀