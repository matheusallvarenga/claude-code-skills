# Troubleshooting: Common VS Code Problems

Solutions for common VS Code issues.

---

## Performance Issues

### Problem: VS Code is Slow

**Symptoms**:
- Slow to start
- Sluggish when typing
- Freezes frequently

**Solutions**:

**1. Check Extensions**
```
Cmd + Shift + P → "Extensions: Show Extensions"
Disable unnecessary extensions
Reload VS Code
Test if faster
```

**2. Restart VS Code**
- Close completely
- Reopen
- Often fixes temporary issues

**3. Clear Cache**
```
Cmd + Shift + P → "Developer: Reload Window"
```

**4. Check Workspace Size**
- Very large workspaces can be slow
- Consider splitting into smaller projects
- Or add folders to `.gitignore`

### Problem: Extensions Slowing Down Startup

**Symptoms**:
- Takes forever to start
- Other apps are fine

**Solutions**:

**1. Disable All Extensions**
```
Cmd + Shift + P → "Extensions: Disable All"
Restart
```

**2. Re-enable Gradually**
```
Cmd + Shift + X → Click extension
Click "Enable"
Restart VS Code
Test speed
Repeat
```

**3. Identify Culprit**
- When you find the slow extension
- Uninstall it
- Find alternative or go without

---

## File and Folder Issues

### Problem: Files Not Showing in Explorer

**Symptoms**:
- File exists but doesn't show
- Folder appears empty

**Solutions**:

**1. Check .gitignore**
- File might be ignored
- Edit .gitignore to include it
- Or remove from .gitignore

**2. Refresh Explorer**
- `Cmd + Shift + P` → "Reload"
- Or press `F5`

**3. Check Sidebar**
- Click folder icon in sidebar
- Make sure correct folder is open
- File → Open Folder (open correct folder)

### Problem: Can't Edit Files

**Symptoms**:
- File won't let you type
- Editor is read-only

**Solutions**:

**1. Check File Permissions**
- Right-click file → Get Info
- Check "Writable" is checked
- Or use terminal: `chmod +w filename`

**2. Check File Lock**
- File might be open elsewhere
- Close in other programs
- Come back to VS Code

**3. Check File Status**
- Look for lock icon next to filename
- Close that file and reopen

### Problem: "File Already Exists" Error

**Symptoms**:
- Can't create file with that name
- File exists but can't see it

**Solutions**:

**1. Check Case Sensitivity**
- `README.md` and `readme.md` might both exist
- Delete duplicate
- Use consistent naming

**2. Check Hidden Files**
- Cmd + Shift + . (period)
- Shows/hides hidden files
- Look for the file
- Delete if duplicate

---

## Editing Issues

### Problem: Syntax Highlighting Wrong

**Symptoms**:
- Colors don't make sense
- Code looks wrong

**Solutions**:

**1. Check File Language**
- Look at bottom right status bar
- Shows file language (JavaScript, Python, etc.)
- Click to change if wrong

**2. Change Language**
- `Cmd + Shift + P` → "Change Language Mode"
- Select correct language
- Highlighting updates

**3. Check File Extension**
- File must have correct extension
- `script.js` for JavaScript
- `script.py` for Python
- `readme.md` for Markdown

### Problem: Indentation is Wrong

**Symptoms**:
- Spaces look weird
- Tabs look weird

**Solutions**:

**1. Check Tab Size**
- Status bar shows "Spaces: 2" or similar
- Click to change
- Set to 2, 4, or 8 spaces

**2. Correct Indentation**
- Select problematic code
- `Cmd + Shift + P` → "Indent"
- Choose "Indent Using Spaces" or "Tabs"

**3. Auto-Format**
- `Cmd + Shift + I` to format
- Requires Prettier extension
- Fixes indentation automatically

### Problem: Undo/Redo Not Working

**Symptoms**:
- `Cmd + Z` doesn't work
- `Cmd + Shift + Z` doesn't work

**Solutions**:

**1. Try Again**
- Make sure you're in editor (not search)
- Try `Cmd + Z` multiple times
- It might have limit

**2. Check Keyboard Layout**
- Different keyboard might have different keys
- Check Settings → Keyboard Shortcuts

**3. Restart VS Code**
- Close and reopen
- Sometimes fixes input issues

---

## Terminal Issues

### Problem: Terminal Won't Open

**Symptoms**:
- `Cmd + J` doesn't work
- Terminal doesn't appear

**Solutions**:

**1. Try Menu**
```
View → Terminal
```

**2. Restart VS Code**
- Close completely
- Reopen
- Try again

**3. Check Terminal Preference**
- Cmd + , (Settings)
- Search "terminal"
- Check settings are correct

### Problem: Commands Don't Run

**Symptoms**:
- Command not recognized
- Error message when running

**Solutions**:

**1. Check Command**
- Verify spelling
- Type `python --version` to test
- Should show version

**2. Install Tool**
- Tool might not be installed
- Use external terminal (Warp) to install
- Then try in VS Code

**3. Check PATH**
- Advanced issue
- Usually works out of the box
- If stuck, ask for help

### Problem: Terminal Text is Garbled

**Symptoms**:
- Strange characters appear
- Text doesn't display right

**Solutions**:

**1. Clear Terminal**
- Type `clear`
- Press Enter
- Clears the terminal

**2. Close and Reopen**
- Close terminal: `Cmd + J`
- Reopen: `Cmd + J`
- Often fixes display issues

---

## Git and Version Control

### Problem: Git Commands Don't Work

**Symptoms**:
- `git status` shows error
- Terminal says "git: command not found"

**Solutions**:

**1. Check Git Installed**
```bash
git --version
```

If error: Git not installed
- Install from https://git-scm.com
- Or install via Homebrew: `brew install git`

**2. Try in Warp**
- Might be VS Code issue
- Open Warp terminal
- Try `git status`
- If works in Warp, VS Code setting issue

### Problem: Can't See Git Changes

**Symptoms**:
- Source Control panel is empty
- Changed files not showing

**Solutions**:

**1. Check Folder is Git Repo**
- Check for `.git` folder
- `ls -la` in terminal
- Should see `.git` folder

**2. Initialize Git**
```bash
git init  # If no .git folder
```

**3. Reload VS Code**
```
Cmd + Shift + P → "Reload Window"
```

**4. Check Git Panel**
- `Cmd + Shift + G`
- Should show changes

---

## Extension Issues

### Problem: Extension Won't Install

**Symptoms**:
- Install button doesn't work
- Installation fails

**Solutions**:

**1. Check Internet**
- Make sure connected
- Try to open website
- Restart Wi-Fi if needed

**2. Try Again**
- Sometimes temporary glitch
- Click Install again

**3. Restart VS Code**
- Close completely
- Reopen
- Try installing again

### Problem: Extension Causes Errors

**Symptoms**:
- Error message in VS Code
- Editor stops working

**Solutions**:

**1. Disable Extension**
- Right-click extension
- Click "Disable"
- Test if error goes away

**2. Uninstall Extension**
- If disabling helps
- Right-click → "Uninstall"
- Remove the problem extension

**3. Find Alternative**
- Search for similar extension
- Try different one

### Problem: Shortcuts from Extension Conflict

**Symptoms**:
- Multiple shortcuts do same thing
- Can't figure out which is which

**Solutions**:

**1. Open Keyboard Shortcuts**
```
Cmd + K, Cmd + S
```

**2. Search Shortcut**
- Type shortcut: `Cmd + B`
- See all commands with that shortcut

**3. Change Conflicting Shortcut**
- Click extension shortcut
- Change to different key
- Test both work

---

## Search and Find Issues

### Problem: Find/Replace Not Working

**Symptoms**:
- `Cmd + F` doesn't open
- Can't replace text

**Solutions**:

**1. Make Sure in Editor**
- Click in editor area
- Not in terminal or elsewhere
- Try `Cmd + F` again

**2. Check Syntax**
- If using regex, make sure enabled
- Alt + R toggle regex mode

**3. Try Replacing Manually**
- Understand scope first
- Replace one at a time
- Click "Replace" button

### Problem: Search Results Wrong

**Symptoms**:
- Finds wrong things
- Misses some matches

**Solutions**:

**1. Check Match Case**
- Alt + C toggles case sensitivity
- "Hello" won't find "hello" if enabled

**2. Check Whole Word**
- Alt + W toggles whole word
- "cat" won't find "concatenate" if enabled

**3. Check Regex**
- If using regex, verify pattern
- Simple text search if unsure
- Alt + R toggles regex

---

## Display and Visual Issues

### Problem: Text is Too Small/Large

**Symptoms**:
- Hard to read text
- Text too big

**Solutions**:

**1. Zoom In/Out**
```
Cmd + +         Zoom in
Cmd + -         Zoom out
Cmd + 0         Reset
```

**2. Change Font Size**
```
File → Preferences → Settings
Search "font size"
Change value
```

### Problem: Theme Looks Wrong

**Symptoms**:
- Colors are off
- Dark/light theme wrong

**Solutions**:

**1. Change Theme**
```
Cmd + Shift + P → "theme"
Select "Color Theme"
Try different theme
```

**2. Reset to Default**
- Try built-in theme
- "Light (Visual Studio Code)"
- "Dark (Visual Studio Code)"

### Problem: Sidebar Disappeared

**Symptoms**:
- Can't see file explorer
- No file browser visible

**Solutions**:

**1. Toggle Sidebar**
```
Cmd + B
```

**2. Use Menu**
```
View → Explorer
```

---

## Keyboard and Input Issues

### Problem: Keyboard Shortcuts Don't Work

**Symptoms**:
- `Cmd + S` doesn't save
- Other shortcuts don't work

**Solutions**:

**1. Check Focus**
- Click in editor
- Terminal might have focus
- Click editor and try again

**2. Check Keyboard Language**
- Different language might need different keys
- System Preferences → Keyboard → Input Sources

**3. Check Customization**
```
Cmd + K, Cmd + S
Search shortcut
See if it's mapped
Change if needed
```

### Problem: Can't Type Special Characters

**Symptoms**:
- Some characters won't type
- Keyboard acting weird

**Solutions**:

**1. Check Keyboard Layout**
- Change to US layout temporarily
- Test if works
- Change back if not issue

**2. Restart VS Code**
- Sometimes fixes input issues

**3. Check Keyboard Settings**
```
Settings → Keyboard
Check "Keyboard Shortcut" setting
```

---

## Recovery

### Problem: Lost Work / Accidental Delete

**Symptoms**:
- Deleted file by mistake
- Lost unsaved changes

**Solutions**:

**1. Undo Before Closing**
- `Cmd + Z` multiple times
- Might recover unsaved changes
- Don't close file yet!

**2. Check Git**
```bash
git status      # See changes
git diff file   # See deleted content
git restore file # Restore file
```

**3. Check Autosave**
- File → Auto Save (might be enabled)
- Recovers some work

**4. Check Trash**
- Files deleted go to Trash
- Trash → Drag file back

---

## Getting Help

### Where to Find Answers

1. **Error Message**: Google the exact error
2. **Feature**: Google "VS Code how to [feature]"
3. **Shortcut**: `Cmd + K, Cmd + S` to see all
4. **Documentation**: https://code.visualstudio.com/docs
5. **Extensions**: Read extension README

### Asking for Help

1. Google the problem first
2. Read error messages carefully
3. Try the solutions provided
4. Ask teammate or online community
5. Include:
   - Error message
   - What you were trying to do
   - Steps to reproduce

---

## Prevention

✅ **Do**:
- Save frequently (`Cmd + S`)
- Use Git for version control
- Commit often
- Test changes
- Read error messages
- Install only needed extensions

❌ **Avoid**:
- Deleting files carelessly
- Ignoring error messages
- Installing random extensions
- Not backing up (Git is backup)
- Complex customizations when starting

---

## Still Stuck?

1. Restart VS Code completely
2. Check if issue is VS Code or something else
3. Try in fresh project
4. Disable all extensions
5. Ask for help with error message

You'll figure it out! Most issues are simple once you know the solution. 🚀
