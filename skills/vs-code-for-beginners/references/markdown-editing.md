# Markdown Editing in VS Code

Complete guide to writing markdown documents in VS Code.

---

## Why Markdown in VS Code?

**Markdown** is a simple format for writing:
- Documentation
- README files
- Notes
- Blog posts
- Any text-based content

**VS Code is perfect for markdown**:
- Live preview
- Syntax highlighting
- Extensions for markdown
- Simple, distraction-free
- Integrates with Git

---

## Markdown Basics

### Headers

```markdown
# Level 1 Heading
## Level 2 Heading
### Level 3 Heading
#### Level 4 Heading
##### Level 5 Heading
###### Level 6 Heading
```

**Display**:
# Level 1
## Level 2
### Level 3

### Emphasis

```markdown
**Bold text**
*Italic text*
***Bold and italic***
~~Strikethrough~~
```

**Display**:
- **Bold text**
- *Italic text*
- ***Bold and italic***
- ~~Strikethrough~~

### Lists

**Unordered**:
```markdown
- Item 1
- Item 2
  - Nested item
  - Another nested
- Item 3
```

**Ordered**:
```markdown
1. First item
2. Second item
3. Third item
```

### Code

**Inline code**:
```markdown
Use `const x = 5` in JavaScript
```

**Code blocks**:
````markdown
```javascript
const greeting = "Hello";
console.log(greeting);
```
````

Specify language (javascript, python, etc.) for syntax highlighting.

### Links

```markdown
[Click here](https://example.com)
[GitHub](https://github.com)
```

### Images

```markdown
![Alt text](image.jpg)
![Screenshot](./screenshots/app.png)
```

### Blockquotes

```markdown
> This is a quote
> It can span multiple lines
```

### Horizontal Rule

```markdown
---
```

### Tables

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

---

## VS Code Features for Markdown

### Live Preview

**Open preview**:
1. Open markdown file
2. Click preview icon (eye) in top right
3. Side-by-side editing and preview

**Or use shortcut**:
```
Cmd + Shift + V
```

**Split view**:
- Edit on left
- Preview on right
- See changes live

### Syntax Highlighting

VS Code colors markdown elements:
- Headers in blue
- Links in color
- Code in different color
- Bold/italic colored

Helps you read and write quickly.

### Outline View

Shows document structure:

1. Click "Outline" tab (in file explorer area)
2. See all headers in your document
3. Click to jump to section

**Great for long documents**.

### Breadcrumbs

Shows current position:

```
README.md > # My Project > ## Features
```

Click to jump to specific heading.

### Formatting Helpers

**Bold**: Select text → `Cmd + B`
**Italic**: Select text → `Cmd + I`
**Strikethrough**: Select text → `Cmd + Shift + X`

(Requires Markdown All in One extension)

---

## Essential Markdown Extensions

### 1. Markdown Preview Enhanced

Better than built-in preview:
- Supports diagrams (Mermaid, PlantUML)
- Math equations
- Multiple preview themes
- Code execution
- Better styling

**Install**: Search "Markdown Preview Enhanced"

**Usage**:
- Open markdown file
- Click preview icon
- See enhanced preview

### 2. Markdown All in One

Keyboard shortcuts for markdown:

- `Cmd + B` → **bold**
- `Cmd + I` → *italic*
- `Cmd + Shift + X` → ~~strikethrough~~
- `Cmd + Alt + C` → code block
- Create lists faster
- Format tables

**Install**: Search "Markdown All in One"

### 3. Markdown Lint

Checks markdown style:
- Consistent formatting
- Proper spacing
- Valid structure
- Best practices

**Install**: Search "Markdownlint"

**Usage**: Automatic, shows warnings

### 4. Code Spell Checker

Catches spelling mistakes:
- In markdown content
- In code comments
- Configurable dictionary
- Custom word lists

**Install**: Search "Code Spell Checker"

---

## Markdown Editing Workflow

### Create New File

**Method 1**:
```
File → New File
Type content
Save as filename.md
```

**Method 2**:
```
Cmd + N (new file)
Type content
Cmd + S (save as)
Type filename.md
```

### Write Content

1. **Type your content** - Just write naturally
2. **Format as you go** - Use shortcuts
3. **Save frequently** - `Cmd + S`
4. **Preview often** - `Cmd + Shift + V`

### Preview Side-by-Side

1. Open markdown file
2. `Cmd + Shift + V` (open preview)
3. Edit on left, see changes on right live
4. No need to save for preview update

### Check Formatting

1. Click "Outline" tab
2. Review all sections
3. Jump to sections
4. Check structure

### Use Keyboard Shortcuts

**Common markdown actions**:
```
Cmd + B         Bold
Cmd + I         Italic
Cmd + Alt + C   Code block
Cmd + Shift + P Command palette
Cmd + F         Find
Cmd + H         Find & replace
```

### Save and Commit

When document is ready:

```bash
git add filename.md
git commit -m "Add documentation"
git push
```

(Or use VS Code Git integration)

---

## Markdown Best Practices

### Structure

**Good structure**:
```markdown
# Main Title

## Section 1
Content here

### Subsection 1.1
Details here

## Section 2
More content

### Subsection 2.1
Details here
```

**Bad structure**:
- Jumping between heading levels
- No logical organization
- All content under one header

### Writing

**Be clear**:
- Short paragraphs
- Descriptive headers
- Active voice
- Concrete examples

**Use formatting**:
- **Bold** for important terms
- `code` for technical terms
- Lists for multiple items
- Blockquotes for emphasis

### Code Examples

**Good**:
````markdown
```python
def hello():
    print("Hello World")
```
````

**Bad**:
````markdown
```
def hello():
    print("Hello World")
```
````

Always specify language.

### Links

**Good**:
```markdown
[Read the documentation](https://docs.example.com)
```

**Bad**:
```markdown
Click here https://docs.example.com
```

Use descriptive link text.

### Images

**Good**:
```markdown
![Homepage screenshot](./images/homepage.png)
```

**Bad**:
```markdown
![image](img.jpg)
```

Use descriptive alt text.

---

## Common Markdown Scenarios

### Creating a README

```markdown
# Project Name

Description of project.

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation
Steps here

## Usage
Examples here

## Contributing
How to contribute

## License
License info
```

### Creating Documentation

```markdown
# Documentation

## Getting Started
Quick start guide

## Concepts
Core concepts explained

## Tutorials
Step-by-step guides

## API Reference
Function/method documentation

## Troubleshooting
Common issues and solutions

## FAQ
Frequently asked questions
```

### Creating Notes

```markdown
# Note Title

## Key Points
- Point 1
- Point 2

## Details
Detailed information

## Links
[Reference 1](url)
[Reference 2](url)

## Follow-up
Things to explore
```

---

## Keyboard Shortcuts for Markdown

| Action | Shortcut |
|--------|----------|
| Bold | `Cmd + B` |
| Italic | `Cmd + I` |
| Strikethrough | `Cmd + Shift + X` |
| Code block | `Cmd + Alt + C` |
| Preview | `Cmd + Shift + V` |
| Find | `Cmd + F` |
| Replace | `Cmd + H` |
| Open outline | (Click outline tab) |
| Go to line | `Cmd + G` |

---

## Tips for Markdown Writing

1. **Write first, format later** - Get ideas down, then clean up
2. **Use preview frequently** - See how it looks
3. **Structure matters** - Logical headers help readers
4. **Keep it simple** - Markdown is meant to be simple
5. **Use keyboard shortcuts** - Faster than menus
6. **Version control** - Commit your docs to Git
7. **Spell check** - Use Code Spell Checker
8. **Test links** - Click links in preview to verify
9. **Use extensions** - They make writing easier
10. **Share your work** - Commit and push to GitHub

---

## Exporting Markdown

VS Code doesn't export to PDF/Word natively, but you can:

### Export as PDF

**Method 1**: Use Markdown Preview Enhanced
- Open preview
- Click "Export" button
- Choose PDF
- Save

**Method 2**: Print to PDF
- Preview in browser
- Print → Save as PDF

### Export as HTML

**Method 1**: Markdown Preview Enhanced
- Open preview
- Click "Export" button
- Choose HTML
- Save

### Keep Source

Always keep markdown file:
- Easy to edit later
- Version control friendly
- Platform independent

---

## Troubleshooting Markdown

### Preview Won't Open

1. `Cmd + Shift + V` again
2. Check file is saved as .md
3. Reload VS Code
4. Check Markdown Preview extension

### Preview Looks Wrong

1. Check markdown syntax
2. Use Markdownlint to find issues
3. Read preview error messages
4. Preview with different extension

### Formatting Not Working

1. Check extension installed (Markdown All in One)
2. Try Command Palette: `Cmd + Shift + P` → "Bold"
3. Check file is markdown (.md extension)
4. Select text before using shortcut

### Images Not Showing

1. Check image path is correct
2. Use relative paths (not absolute)
3. Images must be local (not remote links)
4. Check file exists at path

---

## Your Markdown Editing Setup

**Install**:
- ✅ Markdown Preview Enhanced (better preview)
- ✅ Markdown All in One (shortcuts)
- ✅ Code Spell Checker (spell check)
- Optional: Markdownlint (style checking)

**Shortcuts to learn**:
- `Cmd + Shift + V` - Preview
- `Cmd + B` - Bold
- `Cmd + I` - Italic
- `Cmd + F` - Find

**Workflow**:
1. Create .md file
2. Write content
3. Open preview side-by-side
4. Use keyboard shortcuts
5. Save and commit

**You're ready to write!** 📝
