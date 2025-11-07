Optimize for Obsidian workflow following official documentation from https://docs.obsidian.md and https://help.obsidian.md

CORE PRINCIPLES:
- Second brain structure
- Zettelkasten method
- PKM (Personal Knowledge Management)
- Atomic notes (one idea per note)
- Bi-directional linking
- Local-first, Markdown-based

OBSIDIAN SYNTAX (Official Obsidian Flavored Markdown):

Internal Links:
- [[Note Name]] - Basic wikilink
- [[Note Name|Display Text]] - Custom display text
- [[Note Name#Heading]] - Link to heading
- [[Note Name#^block-id]] - Link to block
- ^block-id - Define block reference

Embedding:
- ![[Note Name]] - Embed entire note
- ![[Note Name#Heading]] - Embed specific heading
- ![[Note Name#^block-id]] - Embed block
- ![[image.png]] - Embed image
- ![[image.png|200]] - Resize image (200px width)
- ![[document.pdf]] - Embed PDF
- ![[document.pdf#page=3]] - PDF specific page
- ![[audio.mp3]] - Embed audio

Callouts (Official Syntax):
```markdown
> [!note] Optional Title
> Content with **markdown** and [[links]]
```

Callout Types: note, abstract, info, todo, tip, success, question, warning, failure, danger, bug, example, quote

Callout Modifiers:
- Foldable: `> [!note]-` (default collapsed) or `> [!note]+` (default expanded)
- Nested callouts supported

Properties (YAML Frontmatter):
```yaml
---
title: Note Title
tags: [tag1, tag2]
aliases: [Alias 1, Alias 2]
created: 2024-01-15
due: 2024-03-01
status: in-progress
publish: true
permalink: custom-url
cssclasses: [class1, class2]
---
```

Property Types:
- text: Simple text
- number: 42
- checkbox: true/false
- date: 2024-01-15
- datetime: 2024-01-15T14:30:00
- list: [item1, item2]
- link: "[[Note]]"

Tags:
- Inline: #tag or #parent/child
- Frontmatter: tags: [recipe, cooking]
- Nested tags: #parent/child/grandchild
- Search: tag:#meeting

Markdown Extensions:
- ==highlight== - Highlighted text
- ~~strikethrough~~ - Strikethrough
- %% comment %% - Comments (not rendered)
- - [ ] Task - Unchecked task
- - [x] Task - Checked task

Advanced Features:

Canvas (.canvas files):
- JSON structure for visual note layouts
- Supports text cards, file cards, link cards
- Connections between nodes with labels

Templates:
- Use {{date}}, {{time}}, {{title}} placeholders
- Core plugin: Templates
- Location: specify in Settings → Templates

Daily Notes:
- Auto-create with date format (YYYY-MM-DD recommended)
- Template support
- Settings: Daily Notes plugin

Maps/Bases (Database Views):
```markdown
view: table
from: "Projects"
where: status = "active"
columns: [name, status, due_date]
sort: due_date asc
```

WORKFLOW PATTERNS:

File Organization:
- Avoid deep folder hierarchies
- Use links over folders
- MOCs (Maps of Content) for structure
- Index notes for topic overviews

Note-Taking Best Practices:
- One idea per note (atomic)
- Link liberally
- Use descriptive titles
- Add context in links: [[Note Name|meaningful context]]
- Create MOCs to organize related notes

OBSIDIAN PUBLISH:
```yaml
---
publish: true
permalink: custom-url-slug
description: SEO description
cover: path/to/image.png
---
```

FORMATTING GUIDELINES:
- Use blank lines between blocks
- Headings: # H1, ## H2, ### H3
- Lists support nesting
- Tables: standard Markdown
- Code blocks: triple backticks with language
- Math: $inline$ or $$block$$

PLUGIN ECOSYSTEM:
- Core plugins: built-in (Templates, Daily Notes, Graph, etc.)
- Community plugins: third-party extensions
- Dataview: query language for notes
- Excalidraw: drawing integration
- Kanban: project boards

SYNCING OPTIONS:
- Obsidian Sync (official, paid)
- Git (version control)
- Third-party cloud services
- Local network sync

RESPONSE STYLE:
- Direct implementation, no explanation
- Use official Obsidian syntax
- Include proper frontmatter
- Create atomic, well-linked notes
- Follow markdown best practices
- Assume vault exists and is properly configured
