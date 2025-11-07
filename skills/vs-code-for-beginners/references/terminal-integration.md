# VS Code & Warp Terminal Integration

Complete guide to using Warp terminal with VS Code.

---

## Overview

**VS Code** has an integrated terminal at the bottom.

**Warp** is your external terminal (better and more powerful).

**This guide** shows how to use both together efficiently.

---

## The Integrated Terminal

### Opening the Terminal

**Method 1: Keyboard**
```
Cmd + J
```

**Method 2: Menu**
```
View → Terminal
```

**Result**: Terminal appears at bottom of VS Code

### Terminal Basics

The integrated terminal works like any terminal:
- Type commands (git, npm, python, etc.)
- See output
- Press Enter to run

**Examples**:
```bash
git status          # Check Git status
npm install         # Install packages
python script.py    # Run Python script
ls                  # List files
cd folder           # Change directory
```

### Common Commands You'll Use

```bash
# Git commands
git status
git add .
git commit -m "message"
git push

# npm/JavaScript
npm install
npm start
npm test

# Python
python script.py
pip install package

# Navigation
ls / ll             # List files
cd foldername       # Change directory
pwd                 # Show current folder
mkdir newfolder     # Create folder
```

### Resizing Terminal

Drag the divider between editor and terminal to resize.

- Drag up = bigger terminal
- Drag down = smaller terminal
- Close = `Cmd + J`

---

## Warp Terminal

### What is Warp?

**Warp** is a modern terminal application:
- Faster than Apple's Terminal
- Better UI and UX
- AI-powered suggestions
- Modern design

You have Warp installed separately.

### Opening Warp

Click Warp icon in Dock or:
```bash
open -a Warp
```

Or press:
```
Command + Space → type "warp" → Enter
```

### Why Warp > Apple Terminal

| Feature | Apple Terminal | Warp |
|---------|----------------|------|
| Speed | Slow | Fast ⚡ |
| UI | Basic | Modern |
| AI Suggestions | No | Yes ✅ |
| Customization | Limited | Great |
| Themes | Few | Many |
| Command Recording | No | Yes ✅ |

---

## Two Terminals, One Workflow

### Integrated Terminal is For

**Quick commands** while editing:
- Run test while looking at code
- Check Git status between commits
- Start development server
- Quick file operations

**Advantages**:
- Doesn't require switching apps
- Can see both code and terminal
- Less context switching

### Warp is For

**Dedicated terminal work**:
- Long-running processes
- Complex command chains
- Full-screen terminal work
- Serious development

**Advantages**:
- Full terminal screen
- Better visual design
- AI suggestions
- More powerful

### Typical Workflow

```
1. Open project in VS Code
2. Use integrated terminal for quick commands
3. For serious work, open Warp
4. Switch between apps with Command + Tab
5. Git commands can use either
```

---

## Using Terminal in VS Code

### Running Commands

```bash
# In integrated terminal, type:
npm start

# See output in terminal
# Keep working in VS Code while it runs
```

### Running Tests

```bash
npm test

# Watch tests run while editing code
# Switch between terminal and editor
```

### Git Operations

```bash
# Stage and commit
git add .
git commit -m "Save progress"
git push

# View status while working
git status
```

### Python Scripts

```bash
python script.py

# Output appears in terminal
# Edit and re-run
```

### Multiple Terminals

Create multiple terminal tabs:
- Click `+` next to terminal tab
- Run different commands in each
- Switch between tabs

### Switching to Warp

You can always switch to Warp for bigger tasks:
```bash
Cmd + Tab → switch to Warp

# Do complex work there
# Come back to VS Code
Cmd + Tab → back to VS Code
```

---

## Terminal Best Practices

### Keep It Organized

- Clear screen with `clear`
- Organize tabs by purpose
- Close tabs when done
- Use meaningful commands

### Use keyboard shortcuts

```
Cmd + J             Toggle terminal visibility
Cmd + Alt + Down    New terminal
Cmd + Shift + Down  Focus next terminal
Cmd + Shift + Up    Focus previous terminal
```

### Read Error Messages

Errors tell you what went wrong:
- "File not found" = check file path
- "Permission denied" = need to use `sudo`
- "Command not found" = command not installed

### Keep Terminal Visible

While developing:
- Keep terminal visible (drag divider)
- Watch output in real-time
- React quickly to errors

---

## Warp Specific Features

### AI Command Suggestions

Warp suggests commands based on what you describe:

1. Start typing a description
2. Warp suggests the command
3. Press Tab to use suggestion
4. Or keep typing

**Example**:
```
"find all javascript files"
↓
find . -name "*.js"
```

### Command Palette

View previous commands:
- `Ctrl + R` - search command history
- Type to search
- Click or press Enter

### Creating Command Groups

Organize frequently used commands:
- Save command groups
- Quick access to complex commands

### Themes and Customization

Warp is highly customizable:
- Change colors
- Change font
- Change keybindings
- Custom settings

---

## Connecting Both

### VS Code Git Integration

VS Code has Git built-in:

**Alternative to terminal**:
- Source Control panel (`Cmd + Shift + G`)
- Visual commit interface
- Easier for beginners

**But terminal is more powerful**:
- More control
- Faster for experienced users
- Handle complex operations

### Choose Your Style

**Visual (Git panel)**:
- Click files to stage
- Write commit message
- Click commit

**Command line (Terminal)**:
- `git add .`
- `git commit -m "message"`
- `git push`

Both work. Pick what feels natural.

---

## Common Terminal Workflows

### Workflow 1: Web Development

```bash
# Open Warp or integrated terminal
npm install                    # Install dependencies
npm start                      # Start dev server
# See "Server running on localhost:3000"
# Switch to browser
# Edit code in VS Code
# Browser auto-refreshes (if configured)
```

### Workflow 2: Python Development

```bash
python -m venv venv            # Create virtual env
source venv/bin/activate       # Activate it
pip install -r requirements.txt # Install packages
python app.py                  # Run script
# Keep running while editing
```

### Workflow 3: Git Workflow

```bash
git status                     # Check status
git add .                      # Stage files
git commit -m "Add feature"    # Commit
git push                       # Push to GitHub
```

### Workflow 4: Documentation

```bash
# Edit markdown in VS Code
# In terminal:
npm install markdown-it        # Install if needed
# Build docs
npm run build-docs

# Check output while editing
```

---

## Troubleshooting Terminal

### Terminal Won't Open

1. Try `Cmd + J` again
2. Check View → Terminal
3. Restart VS Code

### Commands Don't Work

1. Check command is installed
2. Check PATH environment variable
3. Try in Warp (external terminal)
4. Check spelling

### Terminal Slow

1. Close unused terminals
2. Clear terminal with `clear`
3. Restart terminal
4. Check what's running

### Can't Find File

1. Check path is correct
2. Use `pwd` to see current directory
3. Use `ls` to list files
4. Use `cd` to navigate

### Permission Denied

1. Check file permissions
2. Use `sudo` if needed (careful!)
3. Check you own the file/folder

---

## Terminal Commands Quick Reference

**Navigation**:
```bash
pwd                 # Show current folder
cd foldername       # Change folder
ls                  # List files
mkdir newfolder     # Create folder
```

**Git**:
```bash
git status          # Check status
git add .           # Stage all files
git commit -m "msg" # Create commit
git push            # Push to GitHub
git pull            # Get updates
```

**npm/JavaScript**:
```bash
npm install         # Install packages
npm start           # Start app
npm test            # Run tests
npm run build       # Build app
```

**Python**:
```bash
python script.py    # Run script
python --version    # Check version
pip install pkg     # Install package
```

**File Operations**:
```bash
cp file.txt copy.txt     # Copy file
mv file.txt folder/      # Move file
rm file.txt              # Delete file (careful!)
touch newfile.txt        # Create empty file
```

---

## Pro Tips

1. **Keep VS Code + Warp visible** - Drag to arrange windows side-by-side
2. **Use keyboard shortcuts** - Switch apps with `Cmd + Tab`
3. **Read output carefully** - Errors tell you what's wrong
4. **Keep terminal organized** - Close tabs when done
5. **Use git in terminal** - More powerful than UI
6. **Watch for long-running processes** - Some commands take time
7. **Ask for help** - `command --help` shows options
8. **Use man pages** - `man git` shows full documentation

---

## Your Setup

You have:
- ✅ VS Code with integrated terminal
- ✅ Warp external terminal
- ✅ Both ready to use

**Recommended workflow**:
1. Use integrated terminal for quick commands
2. Use Warp for major work or watching output
3. Git operations in either (your choice)
4. Keep both visible when developing

**You're all set!** 🚀
