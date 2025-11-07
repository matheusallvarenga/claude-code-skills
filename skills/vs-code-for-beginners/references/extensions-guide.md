# Extensions Guide: Supercharge VS Code

Complete guide to understanding and using VS Code extensions.

---

## What are Extensions?

**Extensions** are plugins that add features to VS Code.

**Analogy**: Like apps on your phone
- VS Code = blank phone (basic functionality)
- Extensions = apps you install (added features)

### Key Principle

**VS Code is lightweight by default. Extensions add what you need.**

This is intentional design:
- Fast startup (don't load unnecessary code)
- Your choice what to install
- Community-driven features

---

## Why Extensions Matter

### Without Extensions
- Basic text editing
- Syntax highlighting for some languages
- No special tools
- Manual workflows

### With Extensions
- Language-specific features
- Formatting tools
- Themes and icons
- Productivity tools
- Git visualization
- Terminal integrations
- Markdown enhancements

You don't NEED extensions, but they make life easier.

---

## Finding Extensions

### Official VS Code Marketplace

Open VS Code and:
1. `Cmd + Shift + X` (or click Extension icon)
2. Search for what you want
3. Click "Install"

### What to Search For

Describe what you want:
- "markdown preview" → markdown tools
- "prettier" → code formatting
- "github" → GitHub integration
- "theme" → color themes

---

## Installing Extensions

### Method 1: VS Code UI (Recommended)

```
1. Cmd + Shift + X (open extensions)
2. Search for extension name
3. Click "Install" button
4. Wait for installation
5. Reload if needed
```

### Method 2: Command Palette

```
Cmd + Shift + P → "Install Extension" → search → install
```

---

## Recommended Extensions for You

Based on your usage (code projects + markdown):

### Tier 1: Essential (Install These)

#### 1. **Prettier** (Code Formatter)
- Formats code automatically
- Makes code consistent
- Works with JavaScript, Python, HTML, CSS, etc.

**Install**: Search "prettier"

**Usage**: `Cmd + Shift + I` to format

#### 2. **Markdown Preview Enhanced**
- Better markdown preview
- Side-by-side editing and preview
- Supports diagrams and more
- Much better than built-in

**Install**: Search "markdown preview enhanced"

**Usage**: Preview button next to file tabs

#### 3. **GitLens**
- Shows Git info inline
- See who changed each line
- Git blame annotations
- Branch information

**Install**: Search "gitlens"

**Usage**: Automatic, shows in code

#### 4. **GitHub Copilot** (Optional if you want AI in editor)
- AI code suggestions
- Or skip if using Claude Code only

**Install**: Search "github copilot"

**Note**: Paid feature for most users

#### 5. **Error Lens**
- Shows errors inline (in the code)
- Don't need to hover to see errors
- Very helpful

**Install**: Search "error lens"

**Usage**: Automatic

### Tier 2: Nice to Have (Install Later)

#### 6. **Indent Rainbow**
- Colors indentation levels
- Makes code structure clear
- Helpful for nested structures

#### 7. **Peacock**
- Color code your workspaces
- Different project, different color
- Makes switching projects easier

#### 8. **TODO Highlight**
- Highlights TODO, FIXME comments
- Keeps track of tasks
- Great for markdown docs

#### 9. **Better Comments**
- Colors different comment types
- !, ?, //, etc.
- Makes comments more readable

#### 10. **Markdown All in One**
- Keyboard shortcuts for markdown
- Easier list creation
- Bold, italic, links faster

#### 11. **Code Spell Checker**
- Catches spelling mistakes
- Helps in comments and strings
- Configurable dictionary

### Tier 3: Specific to Language (As Needed)

Depending on what languages you code in:

**Python**: Python (Microsoft)
**JavaScript**: ES Lint
**HTML**: HTML Snippets
**CSS**: CSS Peek
**JSON**: JSON Tools
**Docker**: Docker
**YAML**: YAML

Install as needed for your projects.

### Themes (Style)

**Color Themes** (syntax colors):
- Dracula
- One Dark Pro
- Solarized
- Nord
- Gruvbox

**Icon Themes** (file icons):
- Material Icon Theme
- VSCode Icons
- Dracula Icon Theme

---

## Managing Extensions

### Opening Extensions Panel

`Cmd + Shift + X`

Shows:
- Installed extensions (with version)
- Extension details
- Settings and options

### Disabling Extensions

Right-click extension → "Disable"

Or "Disable (Workspace)" to disable only in current project.

**Useful for**: Testing if extension causes problems

### Uninstalling Extensions

Right-click extension → "Uninstall"

**When to uninstall**: If you don't use it or it slows editor

### Updating Extensions

VS Code auto-updates most extensions.

Check for manual updates:
- Extensions panel → "Updates" tab
- Click "Update All"

### Searching Installed

In extensions panel, sort by "Installed"

See all currently installed extensions.

---

## Best Practices

### Start Minimal

- Don't install everything at once
- Start with Tier 1 essentials
- Add as you discover needs
- Fewer = faster editor

### Monitor Performance

- Too many extensions = slower startup
- Use `Cmd + Shift + P` → "Disable All Extensions"
- Re-enable gradually to find culprits
- Disable unnecessary ones

### Understand What Each Does

Before installing:
- Read description
- Check ratings and reviews
- See how many people use it
- (Popular extensions are usually good)

### Keep Up to Date

- Regularly update extensions
- New versions fix bugs
- But don't install beta versions casually

### Workspace-Specific Extensions

Enable extensions only for specific projects:
- Right-click extension → "Enable (Workspace)"
- Useful for project-specific tools
- Keeps main setup clean

---

## Configuring Extensions

### Extension Settings

Extensions have configurable options:

1. Open extensions panel
2. Find your extension
3. Click settings icon (gear)
4. Change options

Or use Command Palette:
- `Cmd + Shift + P` → "Extension: Show Extension Settings"

### Examples

**Prettier**:
- Line length
- Tab width
- Use semicolons (yes/no)
- Quote style

**GitLens**:
- Show/hide blame
- Show/hide hovers
- Color scheme

---

## For Your Specific Workflow

### For Markdown Writing

**Install**:
- Markdown Preview Enhanced (side-by-side preview)
- Markdown All in One (easier formatting)
- TODO Highlight (track tasks)
- Code Spell Checker (catch mistakes)

**Optional**:
- Markdown Math (for equations)
- Markdown Paste (paste images)
- Markdownlint (markdown style checking)

### For Code Projects

**Install**:
- Prettier (auto-format code)
- GitLens (see Git changes)
- Error Lens (inline errors)
- Error Lens (inline errors)
- Language-specific extensions as needed

**Optional**:
- GitHub Copilot (if you want AI suggestions)
- Better Comments (colored comments)
- Indent Rainbow (see indentation)

### For Terminal Integration

VS Code has integrated terminal. No extensions needed.

But you're using Warp, which is better anyway.

---

## Troubleshooting Extensions

### Extension Not Working?

1. Reload VS Code: `Cmd + Shift + P` → "Reload Window"
2. Restart VS Code completely
3. Check extension settings
4. Disable other extensions (might conflict)
5. Uninstall and reinstall

### Editor is Slow?

1. Disable all extensions
2. Re-enable one by one
3. Notice which one slows editor
4. Uninstall that one or find alternative

### Extension Won't Install?

1. Check internet connection
2. Try again
3. Restart VS Code
4. Clear extension cache (advanced)

---

## Popular Extensions Organized by Category

### Formatting & Code Quality
- Prettier - auto-format code
- ESLint - JavaScript linting
- StyleLint - CSS linting
- Markdownlint - markdown validation

### Git & Version Control
- GitLens - git information
- Git History - view git history
- GitHub Copilot - AI suggestions

### Markdown & Writing
- Markdown Preview Enhanced - better preview
- Markdown All in One - markdown shortcuts
- TODO Highlight - find TODOs
- Better Comments - colored comments

### Productivity
- Peacock - color workspaces
- Indent Rainbow - visual indentation
- Code Spell Checker - spell check
- Error Lens - inline errors

### Appearance
- Material Icon Theme - file icons
- Dracula Theme - color theme
- One Dark Pro - popular theme

### Language Support (Install as Needed)
- Python - Python language support
- JavaScript/TypeScript - built-in
- HTML, CSS - built-in but extensions available
- Pylance - Python IntelliSense
- Live Server - quick web server

---

## Extension Etiquette

### Credit Extension Authors

Extensions are usually free, made by volunteers.
- Rate them (⭐⭐⭐⭐⭐)
- Leave kind comments
- Report bugs politely

### Follow Extension Guidance

Extensions have README files:
- Read them
- Follow setup instructions
- Respect keyboard shortcuts they add

---

## Summary

**Start here**:
1. Install Prettier (code formatting)
2. Install Markdown Preview Enhanced (markdown preview)
3. Install GitLens (git info)
4. Use for a week

**Add later as needed**:
- Theme you like
- Language support for your code
- Productivity tools
- Other helpful extensions

**Remember**:
- Less is more (fewer extensions = faster editor)
- Start minimal, add gradually
- Keep editor responsive
- Quality > quantity

---

## For Your Setup

**You specifically need**:
- ✅ Markdown Preview Enhanced (markdown editing)
- ✅ Prettier (code formatting)
- ✅ GitLens (if using Git - which you are!)
- ✅ A theme you like (optional, defaults work fine)

That's it! Start with these and expand as you discover needs.

Everything else is nice-to-have, not need-to-have.

Happy extending! 🚀
