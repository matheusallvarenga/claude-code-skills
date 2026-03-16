List and manage MCP (Model Context Protocol) servers.

Available MCPs (14 total):

**Cloud APIs (6):**
- notion: Workspace integration (docs, databases)
- supabase: Backend-as-a-Service (DB, auth, storage)
- figma-desktop: Design tool integration (local)
- shadcn: React/Tailwind components (npx)
- context7: Expanded context (Upstash)
- vercel: Deployment platform

**Built-in (6):**
- markitdown: Document conversion (PDF, DOCX, etc.)
- memory: Persistent memory between sessions
- filesystem: File system operations
- github: Repository management
- fetch: HTTP requests
- context7: Context enhancement

**Custom (1):**
- obsidian-docs: Obsidian documentation server

Configuration files:
- ~/.claude/mcp.json (server definitions)
- ~/.claude/settings.json (enabled servers)

Use /mcp-status to check active servers.
Use /mcp-add to add a new MCP server.
