Activate Obsidian Docs MCP server (Custom).

Transport: StdIO (Node.js)
Location: ~/.claude/mcps/obsidian-docs/

Tools Available:

1. search_obsidian_docs
   - Search official Obsidian documentation
   - Params: query, category (Plugins|Themes|Reference|All)
   - Returns top 10 relevant sections

2. get_obsidian_syntax_reference
   - Comprehensive syntax reference
   - Params: syntax_type (links|embeds|callouts|properties|tags|all)
   - Returns complete Obsidian Flavored Markdown syntax

3. get_plugin_documentation
   - Plugin development documentation
   - Params: topic
   - Returns relevant plugin dev guides

Resources:
- obsidian://docs/home - Documentation home
- obsidian://docs/syntax - Syntax reference

Example operations:
- "Search for callouts in Obsidian docs"
- "Get syntax reference for embeds"
- "Find plugin documentation for commands"

Prerequisite: Clone docs to /tmp/claude/obsidian-docs
git clone --depth 1 https://github.com/obsidianmd/obsidian-developer-docs.git /tmp/claude/obsidian-docs
