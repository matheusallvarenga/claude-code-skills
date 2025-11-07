# Git Commands Reference

## Organization

Commands are organized by frequency of use and workflow category. Look up what you need by task.

---

## Initial Setup (Do Once)

### Configure Git Identity
**Why**: Git needs to know who you are for each commit.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Explanation**:
- `--global` means this applies to all repositories on your computer
- Replace "Your Name" with your actual name
- Use the same email you registered with on GitHub

**Verify it worked**:
```bash
git config --global user.name
# Output: Your Name
```

---

## Daily Workflow (Most Frequent)

### Check Status
**What it does**: Shows what files changed and what's staged.

```bash
git status
```

**Common output**:
```
On branch main
Changes not staged for commit:
  modified: app.js
  modified: style.css

Untracked files:
  new-file.txt
```

**Interpretation**:
- "Changes not staged" = modified but not yet committed
- "Untracked" = new files Git doesn't know about

### View Recent Changes
**What it does**: Shows what's different from the last commit.

```bash
git diff
```

**Usage**:
- No arguments = show unstaged changes
- `git diff --staged` = show staged changes

**Output example**:
```
- console.log("old code")
+ console.log("new code")
```

The `-` lines are removed, `+` lines are added.

### Stage Files for Commit
**What it does**: Mark specific files to include in the next commit.

```bash
# Stage one file
git add app.js

# Stage all changed files
git add .

# Stage specific files
git add app.js style.css config.js
```

**Why do we stage separately?**
- Only commit related changes together
- Review what you're committing
- Leave out work-in-progress files

### Commit Changes
**What it does**: Create a save point with a message.

```bash
git commit -m "Your commit message here"
```

**Good commit messages**:
- ✅ `"Fix login button alignment on mobile"`
- ✅ `"Add database connection pooling"`
- ✅ `"Remove unused imports from utils.js"`

**Bad commit messages**:
- ❌ `"fix"`
- ❌ `"updates"`
- ❌ `"asdf"`

**Pro tip - include more context**:
```bash
git commit -m "Fix login bug

The login button was not visible on mobile devices.
Adjusted CSS media query to show button at smaller breakpoints.
Tested on iPhone and Android devices."
```

The first line is the title, then blank line, then details.

### Send Commits to GitHub
**What it does**: Push your local commits to the remote (GitHub).

```bash
git push
```

**During your first push to a new branch**:
```bash
git push -u origin branch-name
```

The `-u` flag sets the "upstream" so future pushes know where to go.

### Get Latest Changes
**What it does**: Download updates from GitHub and merge them locally.

```bash
git pull
```

**When to use**:
- Before starting work (get latest from teammates)
- When someone else pushed changes

---

## Branching (Essential for Team Work)

### Create a New Branch
**What it does**: Create a new line of development separate from main.

```bash
# Create and switch to new branch
git checkout -b feature-name

# Or (newer way)
git switch -c feature-name

# Where feature-name examples:
# - add-login-form
# - fix-bug-123
# - improve-performance
```

**Naming conventions**:
- Use lowercase
- Use hyphens for spaces
- Be descriptive: `fix-crash-on-startup` not `fix1`

### List Branches
**What it does**: Show all branches on your computer.

```bash
# Local branches
git branch

# All branches (local + remote)
git branch -a

# Example output:
# main
# * add-login-form
# fix-bug-123
# The * shows which one you're on
```

### Switch Between Branches
**What it does**: Move to a different branch.

```bash
# Using older command
git checkout branch-name

# Using newer command (preferred)
git switch branch-name
```

**Example**:
```bash
git switch main          # Go to main
git switch add-login     # Go to feature branch
```

### Delete a Branch
**What it does**: Remove a branch (usually after merging).

```bash
# Delete local branch
git branch -d branch-name

# Force delete (if not fully merged)
git branch -D branch-name
```

**Example**:
```bash
git branch -d add-login-form  # Delete after merging
```

---

## Pull Requests & Merging

### Push a Branch to GitHub
**What it does**: Send your branch to GitHub so you can create a Pull Request.

```bash
# First push to new branch
git push -u origin branch-name

# Subsequent pushes
git push
```

### View Recent Commits
**What it does**: See your commit history.

```bash
git log

# Shorter format
git log --oneline

# Example output with --oneline:
# a1b2c3d Fix login button styling
# e4f5g6h Add password validation
# i7j8k9l Initial commit
```

### Merge a Branch (After Pull Request is approved)
**What it does**: Combine a feature branch back into main.

```bash
# Switch to the branch you want to merge INTO
git switch main

# Merge the feature branch
git merge branch-name

# Example:
git switch main
git merge add-login
```

**After successful merge**:
```bash
# Delete the feature branch (it's done)
git branch -d branch-name
```

---

## Undoing Changes (Very Important!)

### Undo Changes to a File (Not Yet Staged)
**What it does**: Discard changes to a file since last commit.

```bash
git checkout -- filename
# Or newer way
git restore filename
```

**Example**:
```bash
# You edited app.js and messed it up
git restore app.js
# app.js is back to how it was in the last commit
```

### Unstage a File (Remove from Staging)
**What it does**: Remove a file from the staging area without losing changes.

```bash
git reset filename
# Or
git restore --staged filename
```

**Scenario**:
```bash
git add . # Accidentally staged everything
git reset app.js # Remove app.js from staging
```

### Undo Last Commit (But Keep Changes)
**What it does**: Go back one commit but keep your changes.

```bash
git reset --soft HEAD~1
```

**What this does**:
- Removes the last commit
- Keeps all changes staged
- You can now edit and re-commit

**Example scenario**:
```bash
# You committed something and want to edit it
git reset --soft HEAD~1
# Edit your files
git add .
git commit -m "Corrected commit message"
```

### Undo Last Commit (Discard Changes)
**What it does**: Go back one commit AND discard all changes.

**WARNING: This is destructive!**

```bash
git reset --hard HEAD~1
```

### View and Restore Old Versions
**What it does**: Go back to a specific commit.

```bash
# See the history
git log --oneline

# Go back to a specific commit
git checkout commit-id

# Where commit-id is like: a1b2c3d

# Get back to latest
git checkout main
```

---

## Remote Management

### See Remote Information
**What it does**: Shows where your remote repository is.

```bash
git remote -v
```

**Example output**:
```
origin  https://github.com/username/repo-name.git (fetch)
origin  https://github.com/username/repo-name.git (push)
```

This shows you're connected to GitHub at that URL.

### Add a Remote
**What it does**: Connect to a GitHub repository (usually done automatically when cloning).

```bash
git remote add origin https://github.com/username/repo.git
```

Normally you don't need to do this - it's automatic.

---

## Cloning & Initial Setup

### Clone a Repository
**What it does**: Download an entire project from GitHub to your computer.

```bash
git clone https://github.com/username/project-name.git
cd project-name
```

**Result**:
- A new folder is created with the repo name
- All files and history are downloaded
- You're ready to work

### Clone to a Specific Folder
```bash
git clone https://github.com/username/project-name.git my-custom-folder
```

---

## Viewing Information

### See Global Configuration
**What it does**: Shows your Git settings.

```bash
git config --global --list
```

### See What Branch You're On
**What it does**: Shows current branch (also appears in terminal prompt).

```bash
git status
# Output includes "On branch main"
```

### Detailed Log
**What it does**: Shows commit history with more details.

```bash
# Show last 5 commits
git log -5

# Show with file changes
git log --name-status

# Show with what changed
git log -p
```

---

## Common Command Patterns

### Pattern: Before Starting Work
```bash
git pull                    # Get latest changes
git switch -c new-feature   # Create feature branch
```

### Pattern: While Working
```bash
git add .                   # Stage changes
git commit -m "message"     # Commit
# Repeat as needed
```

### Pattern: Ready to Share
```bash
git push -u origin branch-name  # First time
git push                        # Subsequent times
# Then create PR on GitHub
```

### Pattern: After PR Approved
```bash
git switch main             # Go to main
git pull                    # Get latest
git merge branch-name       # Merge feature
git push                    # Send to GitHub
git branch -d branch-name   # Clean up
```

---

## Tips for Better Command Usage

### Always Check Status
Run `git status` frequently to know what state you're in.

### Commit Frequently
Make commits often with clear messages - easier to debug later.

### Pull Before Push
Always `git pull` before `git push` to avoid conflicts.

### Meaningful Messages
Spend 10 seconds writing a good commit message - future you will thank you.

### Check the Diff
Use `git diff` to review what you're about to commit.

### Branch Naming
Use descriptive branch names - they document what you were working on.
