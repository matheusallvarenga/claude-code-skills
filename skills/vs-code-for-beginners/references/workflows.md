# VS Code Workflows: Step-by-Step

Complete step-by-step procedures for common VS Code tasks.

---

## Workflow 1: Setting Up Your First Project

### Prerequisites
- VS Code installed
- A folder with files (or create new one)

### Steps

**Step 1: Open VS Code**
- Launch VS Code (click icon or search)
- Should see empty window

**Step 2: Open Your Project Folder**
- File → Open Folder
- Navigate to your project folder
- Click "Open"
- VS Code loads the folder

**Step 3: Explore the File Structure**
- Left sidebar shows all files and folders
- Expand folders by clicking arrow
- Click any file to open it

**Step 4: Customize (Optional)**
- File → Preferences → Color Theme (pick a theme)
- File → Preferences → File Icon Theme (pick icons)
- These are optional, defaults are fine

**Step 5: You're Ready!**
- Start editing files
- Use keyboard shortcuts
- Save with `Cmd + S`

**You've opened your first project!** ✅

---

## Workflow 2: Creating and Editing a Markdown Document

### Scenario
You want to write a README.md file for your project.

### Steps

**Step 1: Create New File**
- Right-click in file explorer
- Select "New File"
- Type "README.md"
- Press Enter

**Step 2: Start Writing**
- File opens in editor
- Start typing your content
- Type markdown naturally

**Example**:
```markdown
# My Project

This is my amazing project.

## Features
- Feature 1
- Feature 2

## Installation
```

**Step 3: Open Preview**
- Press `Cmd + Shift + V`
- Preview opens on right side
- See formatted output

**Step 4: Format and Edit**
- Edit on left, see preview on right
- Use `Cmd + B` for bold
- Use `Cmd + I` for italic
- See changes live in preview

**Step 5: Save**
- Press `Cmd + S`
- File is saved
- Indicator next to filename disappears

**Step 6: Commit to Git (If Using)**
- Open integrated terminal: `Cmd + J`
- Type: `git add README.md`
- Type: `git commit -m "Add README"`
- Type: `git push`

**You've created a markdown document!** ✅

---

## Workflow 3: Coding in Your Project

### Scenario
You want to edit code files (JavaScript, Python, etc.)

### Steps

**Step 1: Open Code File**
- Click file in explorer: `index.js` or `main.py`
- File opens in editor
- Syntax highlighting applied automatically

**Step 2: Start Editing**
- Click where you want to edit
- Type code
- VS Code shows intelligent suggestions
- Press Escape to dismiss suggestions

**Step 3: Format Code**
- Select code or entire file
- Press `Cmd + Shift + I`
- Code auto-formats
- (Requires Prettier extension)

**Step 4: Find and Replace**
- `Cmd + H` (find and replace)
- Top box: what to find
- Bottom box: what to replace with
- Click replace buttons

**Step 5: Save and Test**
- `Cmd + S` to save
- Open terminal: `Cmd + J`
- Run your code: `python main.py` or `node index.js`
- See output in terminal
- Fix errors and repeat

**Step 6: Use Version Control**
- See changes in Source Control panel (`Cmd + Shift + G`)
- Stage, commit, push from there
- Or use terminal for more control

**You've edited code!** ✅

---

## Workflow 4: Managing Multiple Files

### Scenario
You're working with multiple files simultaneously.

### Steps

**Step 1: Open Multiple Files**
- Click files in explorer
- Each opens as a new tab
- White dot = unsaved file

**Step 2: Switch Between Files**
- Click tab to switch
- Or press `Ctrl + Tab` to cycle through
- Or press `Cmd + P` and type filename

**Step 3: Compare Two Files (Optional)**
- Open both files
- Right-click tab → "Split Right"
- Now you see files side-by-side
- Edit both at once

**Step 4: Organize Tabs**
- Drag tabs to reorder
- Close tabs with `x` or `Cmd + W`
- All tabs at top for quick switching

**Step 5: Save All**
- File → Save All
- Or `Cmd + Alt + S`
- All unsaved files saved

**You're managing multiple files!** ✅

---

## Workflow 5: Using Git from VS Code

### Scenario
You want to commit changes to Git.

### Steps

**Step 1: Open Source Control Panel**
- Press `Cmd + Shift + G`
- Or click branch icon on left

**Step 2: See Your Changes**
- Panel shows all modified files
- Green = added lines
- Red = removed lines

**Step 3: Stage Files**
- Click `+` next to files you want to commit
- Files move to "Staged Changes"
- Or stage all with "Stage All Changes" button

**Step 4: Write Commit Message**
- Click text box at top
- Type your commit message
- Example: "Add login feature"

**Step 5: Commit**
- Click checkmark button
- Commit is created
- Files are now committed locally

**Step 6: Push to GitHub**
- Click "..." menu
- Select "Push"
- Changes sent to GitHub

**Or use terminal** (more control):
```bash
git status           # See changes
git add .            # Stage all
git commit -m "msg"  # Commit
git push             # Push
```

**You've committed with Git!** ✅

---

## Workflow 6: Installing and Using Extensions

### Scenario
You want to install Markdown Preview Enhanced extension.

### Steps

**Step 1: Open Extensions Panel**
- Press `Cmd + Shift + X`
- Or click puzzle piece icon on left

**Step 2: Search for Extension**
- Type "Markdown Preview Enhanced"
- Click first result
- Read description to verify it's right

**Step 3: Install**
- Click "Install" button
- Wait for installation
- "Install" becomes "Uninstall" when done

**Step 4: Reload if Needed**
- Some extensions require reload
- Click "Reload" if prompted
- VS Code restarts

**Step 5: Use Extension**
- Open markdown file
- Click preview icon (top right)
- See enhanced preview
- Or press `Cmd + Shift + V`

**Step 6: Configure (Optional)**
- Click settings icon next to extension
- Adjust preferences if desired
- Most defaults work fine

**You've installed an extension!** ✅

---

## Workflow 7: Searching Across Your Project

### Scenario
You need to find all occurrences of "TODO" in your project.

### Steps

**Step 1: Open Find Across Files**
- Press `Cmd + Shift + F`
- Or click search icon on left

**Step 2: Search**
- Type "TODO" in search box
- Results show all occurrences
- Shows file and line number

**Step 3: Navigate Results**
- Click result to go to that file
- Cursor jumps to that location
- Highlights matching text

**Step 4: Replace (Optional)**
- Type replacement text in second box
- Click replace buttons
- "Replace" for one, "Replace All" for all

**Step 5: Examples**
- Search "console.log" to find debug statements
- Search "TODO" to find unfinished work
- Search "ERROR" to find error handling

**You've searched your project!** ✅

---

## Workflow 8: Debugging Your Code (Basic)

### Scenario
Your code has an error and you want to see what's happening.

### Steps

**Step 1: Add Debug Output**
- Add `console.log()` (JavaScript) or `print()` (Python)
- Example: `console.log("variable is:", myVar)`

**Step 2: Run Code**
- Open terminal: `Cmd + J`
- Run your code: `node file.js` or `python file.py`

**Step 3: Read Output**
- See debug output in terminal
- Check values
- Look for errors

**Step 4: Remove Debug Code**
- Delete `console.log()` and `print()` statements
- Clean up
- Don't commit debug code

**Step 5: Fix Issue**
- Edit code based on what you learned
- Re-run to test
- Repeat until working

**Alternative: Debugger**
- For advanced debugging: Run & Debug panel (`Cmd + Shift + D`)
- But terminal output is usually enough for beginners

**You've debugged your code!** ✅

---

## Workflow 9: Customizing VS Code

### Scenario
You want to change font size and theme.

### Steps

**Step 1: Open Settings**
- File → Preferences → Settings
- Or press `Cmd + ,`

**Step 2: Search for Setting**
- Type "font size" in search
- Find the setting
- Change value (click and edit)

**Step 3: Try Different Themes**
- `Cmd + Shift + P` → "theme"
- Click "Preferences: Color Theme"
- Use arrow keys to browse
- Press Enter to choose

**Step 4: Try Icon Themes**
- `Cmd + Shift + P` → "icon"
- Click "Preferences: File Icon Theme"
- Browse and choose

**Step 5: Save (Automatic)**
- Changes save automatically
- No need to manually save settings

**Step 6: More Customization**
- Font family
- Tab size
- Auto-save
- Line numbers
- Many more options

**You've customized VS Code!** ✅

---

## Workflow 10: Daily Development Routine

### Morning: Start Working

```
1. Open VS Code (or already have it open)
2. Cmd + Shift + G → Check Git status
3. git pull → Get latest changes
4. Open the file you're working on
5. Start coding
```

### During Work: Save Progress

```
1. Make changes
2. Cmd + S → Save file
3. Cmd + Shift + G → Review changes
4. When done with task:
   - Stage files
   - Write commit message
   - Commit
5. git push → Send to GitHub
```

### Afternoon: Continuous Work

```
1. Switch between files
2. Edit code
3. Save frequently
4. Test with terminal: Cmd + J
5. Commit progress when done
```

### Before Leaving: Clean Up

```
1. Save all files
2. Commit any pending changes
3. Push to GitHub
4. Close VS Code
```

**This becomes automatic over time!** ✅

---

## Quick Reference by Task

| Task | Steps |
|------|-------|
| Open project | File → Open Folder |
| Create file | Right-click → New File |
| Open file | Click in explorer |
| Save | Cmd + S |
| Find text | Cmd + F |
| Replace text | Cmd + H |
| Format code | Cmd + Shift + I |
| Open terminal | Cmd + J |
| Commit code | Cmd + Shift + G |
| Install extension | Cmd + Shift + X |
| Change theme | Cmd + Shift + P → theme |
| Git status | Cmd + Shift + G |
| Run command | Cmd + Shift + P |

---

## You're Ready!

You now know common VS Code workflows. Pick one workflow to try today. Practice until it feels natural. Add new workflows gradually.

Happy coding! 🚀
