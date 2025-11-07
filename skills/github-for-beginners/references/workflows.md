# Common GitHub Workflows (Step-by-Step)

Complete procedures for the most common tasks you'll encounter.

---

## Workflow 1: Setting Up Git (First Time Only)

### Prerequisites
- Git installed on your computer ([download here](https://git-scm.com/))
- GitHub account created

### Steps

**Step 1: Configure Your Identity**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Step 2: Generate SSH Key (Recommended)**
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
# Press Enter for default location
# Create a passphrase (or press Enter for none)
```

**Step 3: Add SSH Key to GitHub**
- Copy your SSH key: `cat ~/.ssh/id_ed25519.pub`
- Go to GitHub Settings → SSH and GPG Keys
- Click "New SSH Key"
- Paste the key and save

**Step 4: Verify It Works**
```bash
ssh -T git@github.com
# Should output: "Hi username! You've successfully authenticated..."
```

**You're done!** Now you're ready to use GitHub.

---

## Workflow 2: Cloning Your First Repository

### Scenario
You have a GitHub repository and want to work on it locally.

### Prerequisites
- Git configured (see Workflow 1)
- GitHub repository URL (e.g., `https://github.com/matheusallvarenga/claude-code`)

### Steps

**Step 1: Navigate to Where You Want the Project**
```bash
cd ~/Projects  # Or wherever you keep code
```

**Step 2: Clone the Repository**
```bash
git clone https://github.com/matheusallvarenga/claude-code.git
```

**Step 3: Navigate Into the Project**
```bash
cd claude-code
```

**Step 4: Verify It Worked**
```bash
git status
# Should show: "On branch main" (or main branch name)
```

**You're done!** The project is now on your computer with full history.

---

## Workflow 3: Making Your First Commit

### Scenario
You've made changes to your code and want to save them to Git.

### Prerequisites
- A Git repository on your computer (see Workflow 2)
- Changes made to files

### Steps

**Step 1: Check What Changed**
```bash
git status
```

**Example output**:
```
On branch main
Changes not staged for commit:
  modified: app.js
  modified: style.css
```

**Step 2: Review the Changes (Optional but Recommended)**
```bash
git diff
```

This shows exactly what changed so you can verify before committing.

**Step 3: Stage the Files You Want to Commit**
```bash
# Option A: Stage specific files
git add app.js style.css

# Option B: Stage all changes
git add .
```

**Step 4: Verify What's Staged**
```bash
git status
```

Should show files in green (staged).

**Step 5: Create the Commit**
```bash
git commit -m "Fix styling issues on buttons"
```

**Step 6: Verify It Worked**
```bash
git log --oneline
# Should show your new commit at the top
```

**You're done!** Your changes are now saved in Git history.

---

## Workflow 4: Pushing Changes to GitHub

### Scenario
You've made commits locally and want to share them with your team on GitHub.

### Prerequisites
- Made commits locally (see Workflow 3)
- Connected to GitHub remote

### Steps

**Step 1: Check Current Branch**
```bash
git status
# Note the branch name (e.g., "On branch main")
```

**Step 2: Pull Latest Changes (Important!)**
```bash
git pull
```

This gets any changes teammates pushed, avoiding conflicts.

**Step 3: Push Your Commits**

**First time pushing to a new branch:**
```bash
git push -u origin branch-name
# Example: git push -u origin main
```

**Subsequent pushes:**
```bash
git push
```

**Step 4: Verify on GitHub**
- Go to your repository on GitHub
- You should see your commits in the history
- Click "Commits" tab to see all

**You're done!** Your changes are now on GitHub.

---

## Workflow 5: Creating a Feature Branch

### Scenario
You want to work on a new feature without affecting the main code.

### Prerequisites
- A Git repository on your computer
- Currently on `main` branch (or starting branch)

### Steps

**Step 1: Make Sure You're on the Base Branch**
```bash
git switch main
git pull  # Get latest before creating branch
```

**Step 2: Create and Switch to Feature Branch**
```bash
git switch -c add-user-authentication
# or
git checkout -b add-user-authentication
```

**Step 3: Verify You're on the New Branch**
```bash
git status
# Should show: "On branch add-user-authentication"
```

**Step 4: Make Your Changes**
- Edit files as needed
- Test your changes

**Step 5: Commit Your Changes**
```bash
git add .
git commit -m "Implement user authentication system"
```

**Step 6: Push Your Branch to GitHub**
```bash
git push -u origin add-user-authentication
```

**You're done!** Your branch is on GitHub and ready for a Pull Request.

---

## Workflow 6: Creating Your First Pull Request

### Scenario
You've completed a feature branch and want to get code review before merging to main.

### Prerequisites
- Feature branch pushed to GitHub (see Workflow 5)
- Changes are complete and tested

### Steps

**Step 1: Go to Your Repository on GitHub**
- Navigate to https://github.com/matheusallvarenga/claude-code

**Step 2: You'll See a Banner**
```
"Your recently pushed branches"
add-user-authentication  [Compare & Pull Request]
```

Click `[Compare & Pull Request]`

**Step 3: Fill in PR Details**
- **Title**: Brief description (e.g., "Add user authentication system")
- **Description**: Explain what you changed and why
  ```
  ## What Changed
  - Implemented login form
  - Added password validation
  - Added JWT token handling

  ## Testing
  - Tested on Chrome and Firefox
  - Verified password validation works
  - Tested session timeout

  ## Related Issues
  Fixes #123
  ```

**Step 4: Click "Create Pull Request"**

**Step 5: Request Review (Optional)**
- Right side panel → Reviewers
- Select teammate(s) to review

**Step 6: Wait for Review**
- Reviewers will comment on your code
- Make requested changes
- Push new commits to the same branch
- Comments are automatically updated

**Step 7: Merge When Approved**
- Once approved, click "Merge Pull Request"
- Choose merge type (usually "Create a merge commit")
- Click "Confirm merge"

**Step 8: Delete the Branch (Cleanup)**
```bash
# In GitHub UI: Click "Delete branch" button
# Or locally:
git switch main
git branch -d add-user-authentication
```

**You're done!** Your code is merged and deployed.

---

## Workflow 7: Syncing With Teammates' Changes

### Scenario
Teammates pushed changes while you were working, and you need to get their updates.

### Prerequisites
- A Git repository on your computer
- Remote is configured (automatic if cloned)

### Steps

**Step 1: Check If There Are Remote Changes**
```bash
git fetch
# This downloads info about changes without modifying your code
```

**Step 2: Pull the Changes**
```bash
git pull
```

This combines fetch + merge.

**Step 3: If There's a Merge Conflict**
```bash
# You'll see:
# CONFLICT (content merge): app.js

# Check status
git status

# The file will show conflicts like:
# <<<<<<< HEAD
# your code
# =======
# their code
# >>>>>>> branch-name
```

**Step 4: Resolve the Conflict**
- Open the conflicted file
- Keep the code you want (delete the markers)
- You might need both versions

**Step 5: Commit the Resolution**
```bash
git add app.js
git commit -m "Resolve merge conflict in app.js"
git push
```

**You're done!** You have all the latest changes.

---

## Workflow 8: Undoing a Mistake

### Scenario
You made a commit you want to undo.

### Prerequisites
- Know which commit to undo

### Steps

**Option A: Undo Last Commit (Keep Changes)**
```bash
git reset --soft HEAD~1
# Changes go back to staging area
# Edit if needed, then commit again
git add .
git commit -m "Corrected commit"
git push -f origin branch-name
```

**Option B: Undo Last Commit (Discard Changes)**
```bash
git reset --hard HEAD~1
# ALL changes are discarded - be careful!
git push -f origin branch-name
```

**Option C: Undo Specific Older Commit**
```bash
git log --oneline  # Find the commit ID
# Let's say it's: a1b2c3d

git revert a1b2c3d
# This creates a NEW commit that undoes the old one
git push
```

**⚠️ Important**: Use `git reset` only on your own branches. Use `git revert` when changes are already pushed and shared.

**You're done!** The mistake is undone.

---

## Workflow 9: Integrating with Claude Code (Your Setup)

### What Is Claude Code?
Claude Code is an AI agent that can make code changes directly in your repository when you ask it to.

### Prerequisites
- GitHub App installed on your repository
- `ANTHROPIC_API_KEY` secret configured
- `.github/workflows/claude.yml` in your repository

### Steps to Use It

**Step 1: Create an Issue or Open a PR**
- Go to your GitHub repository
- Click "Issues" → "New issue"
- Or comment on existing PR/issue

**Step 2: Mention @claude**
```
@claude fix the login button styling on mobile
```

**Step 3: Claude Code Will:
- Receive your request
- Analyze the code
- Make changes
- Create a commit
- Push to your repository
- Comment with summary

### Best Practices

**Be specific:**
- ✅ "Add form validation to the email field"
- ❌ "make it better"

**Include context:**
- ✅ "The search button doesn't work on mobile, fix the CSS media query"
- ❌ "broken"

**One thing at a time:**
- ✅ Multiple issues for multiple features
- ❌ "Fix everything"

**Review changes:**
- Always review Claude's code before merging
- Run tests locally
- Ask for modifications if needed

### Example Workflow with Claude Code

```
1. You create Issue: "Add password validation"
2. You comment: "@claude implement password validation for signup form"
3. Claude Code analyzes your codebase
4. Claude Code makes changes and commits
5. You review the changes
6. You merge or ask for revisions
7. Changes are deployed
```

---

## Workflow 10: Daily Workflow Loop

### The Standard Day

**Morning: Start of Day**
```bash
cd my-project
git pull  # Get latest from teammates
```

**During Work: Regular Commits**
```bash
# Make changes
git add .
git commit -m "Add feature X"
git push
```

**As Needed: Check Status**
```bash
git status      # What changed?
git diff        # Show me the changes
git log --oneline  # Recent commits
```

**Afternoon: Handle Review Comments**
```bash
# Teammate left comments on your PR
# Make requested changes
git add .
git commit -m "Address PR feedback"
git push  # Automatically updates PR
```

**Before Merging**
```bash
git pull  # Get latest from main in case teammates merged
git merge main  # Merge main into your branch
# Resolve any conflicts
git push
```

**After Merging**
```bash
git switch main
git pull
git branch -d feature-branch-name
```

---

## Troubleshooting Quick Links

- **Merge conflict**: See Workflow 7, Step 3
- **Undo mistake**: See Workflow 8
- **Branches not showing**: Run `git fetch -p` to remove deleted branches
- **Password/auth issues**: Check SSH key configuration (Workflow 1, Step 2)
- **Lost commits**: Use `git reflog` to find them
