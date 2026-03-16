#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Path to the cloned Obsidian documentation
const OBSIDIAN_DOCS_PATH = "/tmp/claude/obsidian-docs/en";

class ObsidianDocsMCPServer {
  constructor() {
    this.server = new Server(
      {
        name: "obsidian-docs-mcp-server",
        version: "1.0.0",
      },
      {
        capabilities: {
          tools: {},
          resources: {},
        },
      }
    );

    this.setupHandlers();
    this.server.onerror = (error) => console.error("[MCP Error]", error);
    process.on("SIGINT", async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  setupHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: "search_obsidian_docs",
          description: "Search for specific topics in the official Obsidian documentation. Returns relevant documentation sections with examples and explanations.",
          inputSchema: {
            type: "object",
            properties: {
              query: {
                type: "string",
                description: "Search query (e.g., 'wikilinks', 'callouts', 'properties', 'canvas')",
              },
              category: {
                type: "string",
                description: "Optional category filter: 'Plugins', 'Themes', 'Reference', or 'All'",
                enum: ["Plugins", "Themes", "Reference", "All"],
                default: "All",
              },
            },
            required: ["query"],
          },
        },
        {
          name: "get_obsidian_syntax_reference",
          description: "Get comprehensive syntax reference for Obsidian Flavored Markdown including wikilinks, embeds, callouts, properties, and more.",
          inputSchema: {
            type: "object",
            properties: {
              syntax_type: {
                type: "string",
                description: "Type of syntax reference",
                enum: ["links", "embeds", "callouts", "properties", "tags", "all"],
                default: "all",
              },
            },
            required: [],
          },
        },
        {
          name: "get_plugin_documentation",
          description: "Get detailed documentation for developing Obsidian plugins, including API references and best practices.",
          inputSchema: {
            type: "object",
            properties: {
              topic: {
                type: "string",
                description: "Plugin development topic (e.g., 'getting started', 'views', 'commands', 'settings')",
              },
            },
            required: ["topic"],
          },
        },
      ],
    }));

    // List available resources
    this.server.setRequestHandler(ListResourcesRequestSchema, async () => ({
      resources: [
        {
          uri: "obsidian://docs/home",
          mimeType: "text/markdown",
          name: "Obsidian Developer Docs Home",
          description: "Main page of Obsidian developer documentation",
        },
        {
          uri: "obsidian://docs/syntax",
          mimeType: "text/markdown",
          name: "Obsidian Syntax Reference",
          description: "Complete reference for Obsidian Flavored Markdown syntax",
        },
      ],
    }));

    // Read resource
    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const uri = request.params.uri;

      if (uri === "obsidian://docs/home") {
        try {
          const content = await fs.readFile(path.join(OBSIDIAN_DOCS_PATH, "Home.md"), "utf-8");
          return {
            contents: [
              {
                uri,
                mimeType: "text/markdown",
                text: content,
              },
            ],
          };
        } catch (error) {
          throw new Error(`Failed to read resource: ${error.message}`);
        }
      }

      if (uri === "obsidian://docs/syntax") {
        const syntaxContent = await this.generateSyntaxReference();
        return {
          contents: [
            {
              uri,
              mimeType: "text/markdown",
              text: syntaxContent,
            },
          ],
        };
      }

      throw new Error(`Unknown resource URI: ${uri}`);
    });

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      switch (name) {
        case "search_obsidian_docs":
          return await this.searchDocs(args.query, args.category || "All");

        case "get_obsidian_syntax_reference":
          return await this.getSyntaxReference(args.syntax_type || "all");

        case "get_plugin_documentation":
          return await this.getPluginDocs(args.topic);

        default:
          throw new Error(`Unknown tool: ${name}`);
      }
    });
  }

  async searchDocs(query, category) {
    try {
      const searchResults = [];
      const searchPath = category === "All" ? OBSIDIAN_DOCS_PATH : path.join(OBSIDIAN_DOCS_PATH, category);

      const files = await this.findMarkdownFiles(searchPath);

      for (const file of files) {
        const content = await fs.readFile(file, "utf-8");
        if (content.toLowerCase().includes(query.toLowerCase())) {
          const relativePath = path.relative(OBSIDIAN_DOCS_PATH, file);
          const excerpt = this.extractExcerpt(content, query);
          searchResults.push({
            file: relativePath,
            excerpt,
          });
        }
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify({
              query,
              category,
              results: searchResults.slice(0, 10), // Limit to top 10 results
              total_found: searchResults.length,
            }, null, 2),
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `Error searching documentation: ${error.message}`,
          },
        ],
        isError: true,
      };
    }
  }

  async getSyntaxReference(syntaxType) {
    const syntaxContent = await this.generateSyntaxReference(syntaxType);
    return {
      content: [
        {
          type: "text",
          text: syntaxContent,
        },
      ],
    };
  }

  async getPluginDocs(topic) {
    try {
      const pluginPath = path.join(OBSIDIAN_DOCS_PATH, "Plugins");
      const files = await this.findMarkdownFiles(pluginPath);

      const relevantFiles = files.filter(f =>
        f.toLowerCase().includes(topic.toLowerCase())
      );

      if (relevantFiles.length === 0) {
        return {
          content: [
            {
              type: "text",
              text: `No plugin documentation found for topic: ${topic}`,
            },
          ],
        };
      }

      const contents = await Promise.all(
        relevantFiles.slice(0, 3).map(async (file) => {
          const content = await fs.readFile(file, "utf-8");
          const relativePath = path.relative(OBSIDIAN_DOCS_PATH, file);
          return `## ${relativePath}\n\n${content}\n\n---\n\n`;
        })
      );

      return {
        content: [
          {
            type: "text",
            text: `# Plugin Documentation: ${topic}\n\n${contents.join("\n")}`,
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `Error retrieving plugin documentation: ${error.message}`,
          },
        ],
        isError: true,
      };
    }
  }

  async generateSyntaxReference(syntaxType = "all") {
    const references = {
      links: `# Internal Links
- \`[[Note Name]]\` - Basic wikilink
- \`[[Note Name|Display Text]]\` - Custom display text
- \`[[Note Name#Heading]]\` - Link to heading
- \`[[Note Name#^block-id]]\` - Link to block
- \`^block-id\` - Define block reference`,

      embeds: `# Embedding
- \`![[Note Name]]\` - Embed entire note
- \`![[Note Name#Heading]]\` - Embed specific heading
- \`![[image.png]]\` - Embed image
- \`![[image.png|200]]\` - Resize image (200px width)
- \`![[document.pdf#page=3]]\` - PDF specific page`,

      callouts: `# Callouts
\`\`\`markdown
> [!note] Optional Title
> Content with **markdown** and [[links]]
\`\`\`

Types: note, abstract, info, todo, tip, success, question, warning, failure, danger, bug, example, quote
Modifiers: \`[!note]-\` (collapsed) or \`[!note]+\` (expanded)`,

      properties: `# Properties (YAML Frontmatter)
\`\`\`yaml
---
title: Note Title
tags: [tag1, tag2]
aliases: [Alias 1, Alias 2]
created: 2024-01-15
status: in-progress
---
\`\`\`

Types: text, number, checkbox, date, datetime, list, link`,

      tags: `# Tags
- Inline: #tag or #parent/child
- Frontmatter: tags: [recipe, cooking]
- Nested: #parent/child/grandchild
- Search: tag:#meeting`,
    };

    if (syntaxType === "all") {
      return Object.values(references).join("\n\n---\n\n");
    }

    return references[syntaxType] || "Unknown syntax type";
  }

  async findMarkdownFiles(dir) {
    const files = [];

    try {
      const entries = await fs.readdir(dir, { withFileTypes: true });

      for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);

        if (entry.isDirectory()) {
          files.push(...(await this.findMarkdownFiles(fullPath)));
        } else if (entry.isFile() && entry.name.endsWith(".md")) {
          files.push(fullPath);
        }
      }
    } catch (error) {
      console.error(`Error reading directory ${dir}:`, error.message);
    }

    return files;
  }

  extractExcerpt(content, query, contextLength = 200) {
    const lowerContent = content.toLowerCase();
    const lowerQuery = query.toLowerCase();
    const index = lowerContent.indexOf(lowerQuery);

    if (index === -1) return "";

    const start = Math.max(0, index - contextLength / 2);
    const end = Math.min(content.length, index + query.length + contextLength / 2);

    let excerpt = content.slice(start, end);
    if (start > 0) excerpt = "..." + excerpt;
    if (end < content.length) excerpt = excerpt + "...";

    return excerpt;
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error("Obsidian Docs MCP Server running on stdio");
  }
}

const server = new ObsidianDocsMCPServer();
server.run().catch(console.error);
