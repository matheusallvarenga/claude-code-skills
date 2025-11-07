# Keyboard Shortcuts Mastery

Essential shortcuts for working efficiently in VS Code.

---

## Philosophy: Why Shortcuts Matter

**Keyboard is 10x faster than mouse.**

Learn 3-5 shortcuts this week. Next week, learn 3-5 more. Within a month, you'll be flying through VS Code.

**Strategy**: Learn by frequency. Use the most common shortcuts until automatic. Add new ones gradually.

---

## The Essential 5 (Start Here)

Master these first. They account for 80% of actions:

### 1. Command Palette
```
Cmd + Shift + P
```
Runs ANY command. The most powerful shortcut.

**Examples**:
- Type "format" → Format document
- Type "theme" → Change theme
- Type "git commit" → Git operations
- Type "extensions" → Install extension

### 2. Quick Open
```
Cmd + P
```
Open any file by typing its name.

**Usage**:
- Press shortcut
- Start typing filename
- Press Enter to open

**Example**:
```
Cmd + P
→ README.md
→ Enter (opens README.md)
```

### 3. Find in File
```
Cmd + F
```
Search for text in current file.

**Usage**:
- Opens find dialog
- Type what you're looking for
- Press Enter or click arrows to navigate

**Quick tip**: Press `Cmd + F` again to focus in the file (not the search box)

### 4. Find and Replace
```
Cmd + H
```
Find text and replace it.

**Usage**:
- First box: what to find
- Second box: what to replace with
- Buttons to replace one or all

**Example**: Change all `var` to `const`

### 5. Go to Line
```
Cmd + G
```
Jump to a specific line number.

**Usage**:
- Press shortcut
- Type line number
- Press Enter

**Great for**: "Error on line 42, let me jump there"

---

## File Operations (Very Common)

### New File
```
Cmd + N
```
Create untitled file (save it with a name later).

### Open File
```
Cmd + O
```
Open file browser dialog.

### Save File
```
Cmd + S
```
Save current file.

**Pro tip**: Enable auto-save to never worry about this.

### Save All
```
Cmd + Alt + S
```
Save all open files.

### Close File/Tab
```
Cmd + W
```
Close current file.

### Close All Files
```
Cmd + K, Cmd + W
```
Close all open files.

### Switch Between Files
```
Ctrl + Tab
```
Cycle through open files.

**Or**: `Cmd + P`, then press Ctrl+Tab within the quick open menu.

---

## Navigation (Moving Around Fast)

### Next Error/Warning
```
Cmd + F8
```
Jump to next error in file.

### Previous Error/Warning
```
Cmd + Shift + F8
```
Jump to previous error.

### Go to Line
```
Cmd + G
```
(Already covered above)

### Go to Symbol
```
Cmd + Shift + O
```
Jump to function, class, or heading in file.

**Useful for markdown**: Jump to sections/headings

### Go to Definition
```
Cmd + Click on name
```
Jump to where something is defined (code files).

### Breadcrumbs
```
Click the breadcrumb trail
```
Shows current position in file.

---

## Editing (Most Used)

### Cut Line
```
Cmd + X
```
Cut entire line (or selection).

**Smart**: If nothing selected, cuts the whole line.

### Copy Line
```
Cmd + C
```
Copy entire line (or selection).

**Smart**: If nothing selected, copies the whole line.

### Paste
```
Cmd + V
```
Paste clipboard.

### Delete Line
```
Cmd + Shift + K
```
Delete entire line.

### Duplicate Line
```
Cmd + Shift + D
```
Duplicate current line (useful!).

### Move Line Up
```
Option + Up Arrow
```
Move line up.

### Move Line Down
```
Option + Down Arrow
```
Move line down.

**Great for**: Reordering markdown sections

### Insert Line Below
```
Cmd + Enter
```
Insert new line below and move cursor there.

### Insert Line Above
```
Cmd + Shift + Enter
```
Insert new line above and move cursor there.

### Select Line
```
Cmd + L
```
Select entire line.

### Select All
```
Cmd + A
```
Select all content in file.

---

## Search and Replace (Advanced)

### Find in All Files
```
Cmd + Shift + F
```
Search across entire workspace.

**Usage**:
- Top box: search term
- Second box: replace term (optional)
- Use buttons to replace

### Replace in All Files
```
Same as above, but use replace box
```

### Find Next Match
```
Cmd + G
```
Go to next search result.

### Find Previous Match
```
Cmd + Shift + G
```
Go to previous search result.

### Toggle Match Case
```
Alt + C
```
Within find dialog, match exact case.

### Toggle Whole Word
```
Alt + W
```
Within find dialog, match whole words only.

### Toggle Regex
```
Alt + R
```
Within find dialog, use regular expressions.

---

## Code Formatting (Clean Code)

### Format Document
```
Cmd + Shift + I
```
Auto-format entire file.

**Requires**: Formatter extension installed

**Great for**: Cleaning up code, consistent style

### Format Selection
```
Cmd + K, Cmd + F
```
Format just the selected text.

### Indent Line
```
Cmd + ]
```
Increase indentation.

### Outdent Line
```
Cmd + [
```
Decrease indentation.

### Add Line Comment
```
Cmd + /
```
Comment/uncomment line (for code files).

---

## Multi-Cursor Editing (Power User)

### Add Cursor Above
```
Cmd + Alt + Up
```
Add another cursor above current one.

### Add Cursor Below
```
Cmd + Alt + Down
```
Add another cursor below current one.

### Select All Occurrences
```
Cmd + Shift + L
```
Select all instances of current selection.

**Great for**: Renaming multiple instances at once

### Select Next Occurrence
```
Cmd + D
```
Select next instance of current selection.

---

## Sidebar and Views (Managing Interface)

### Toggle Sidebar
```
Cmd + B
```
Show/hide file explorer and panels.

### Toggle Terminal
```
Cmd + J
```
Show/hide integrated terminal.

### Toggle Zen Mode
```
Cmd + K, Z
```
Full-screen editing mode (minimal UI).

### Explorer
```
Cmd + Shift + E
```
Show file explorer.

### Search
```
Cmd + Shift + F
```
Show search across files.

### Source Control
```
Cmd + Shift + G
```
Show Git panel.

### Extensions
```
Cmd + Shift + X
```
Show extensions browser.

### Toggle Minimap
```
View → Toggle Minimap
```
(No default shortcut, use Command Palette)

---

## Editing Multiple Files

### Split Editor Right
```
Cmd + \
```
Open second editor beside current.

### Split Editor Down
```
Cmd + K, Cmd + \
```
Open editor below current.

### Switch Editor
```
Cmd + 1, Cmd + 2, Cmd + 3
```
Switch between editor groups.

Example: `Cmd + 1` goes to first editor group (left), `Cmd + 2` goes to second (right).

---

## Undo/Redo (Mistakes Happen)

### Undo
```
Cmd + Z
```
Undo last action.

### Redo
```
Cmd + Shift + Z
```
Redo undone action.

---

## Less Common but Useful

### Preview in Side-by-Side
```
Cmd + Alt + Right Arrow
```
Open file in split view.

### Increase/Decrease Font Size
```
Cmd + +
Cmd + -
```
Zoom in/out.

### Reset Zoom
```
Cmd + 0
```
Reset to default zoom level.

### Show Keyboard Shortcuts
```
Cmd + K, Cmd + S
```
View all shortcuts (in VS Code).

---

## Learning Strategy

### Week 1: The Essential 5
- Command Palette
- Quick Open
- Find in File
- Find and Replace
- Go to Line

Use these constantly until automatic.

### Week 2: Add These
- Save File
- Cut/Copy/Paste
- Delete Line
- Format Document
- Toggle Sidebar

### Week 3: Add These
- Duplicate Line
- Move Line Up/Down
- Split Editor
- Select All Occurrences
- Go to Symbol

### Week 4: Everything Else
Once you're comfortable, explore the others.

---

## Tips for Learning Shortcuts

1. **Start with one shortcut** - Learn it by using it repeatedly
2. **Use stickers** - Put shortcut labels on your keyboard
3. **Write them down** - Muscle memory comes from repetition
4. **Practice daily** - Small, consistent practice beats cramming
5. **Mouse is fine at first** - Transition gradually to keyboard
6. **Build habit** - Start with essential 5, expand slowly

---

## Customizing Shortcuts

You can change shortcuts to whatever you want:

File → Preferences → Keyboard Shortcuts

But don't change them early. Learn the defaults first.

---

## Quick Reference by Task

| Task | Shortcut |
|------|----------|
| Run command | `Cmd + Shift + P` |
| Open file | `Cmd + P` |
| Find text | `Cmd + F` |
| Find and replace | `Cmd + H` |
| Go to line | `Cmd + G` |
| Save | `Cmd + S` |
| Undo | `Cmd + Z` |
| Redo | `Cmd + Shift + Z` |
| Cut line | `Cmd + X` |
| Copy line | `Cmd + C` |
| Paste | `Cmd + V` |
| Delete line | `Cmd + Shift + K` |
| Duplicate line | `Cmd + Shift + D` |
| Format | `Cmd + Shift + I` |
| Toggle sidebar | `Cmd + B` |
| Toggle terminal | `Cmd + J` |

---

## You Got This!

Pick 3 shortcuts right now and use them today. Tomorrow, add 2 more. Consistency beats intensity.

In 2 weeks, you'll be shocked at how much faster you work! 🚀
