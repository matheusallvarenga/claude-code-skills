# Troubleshooting Common GitHub & Git Problems

Organized by problem type with diagnostic questions and solutions.

---

## Authentication Issues

### Problem: "Permission denied (publickey)"

**Symptoms**:
- Can't push or pull
- Error mentions "publickey" or "authentication failed"

**Diagnostic Questions**:
- Have you set up SSH keys?
- Did you use `git clone` with SSH or HTTPS?

**Solutions**:

**Option 1: Check SSH Setup**
```bash
ssh -T git@github.com
```

**If it fails, set up SSH**:
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
cat ~/.ssh/id_ed25519.pub
```

Copy that key and add it to GitHub: Settings → SSH and GPG keys → New SSH key

**Option 2: Use HTTPS Instead**
If SSH is too complicated, use HTTPS authentication:
```bash
git clone https://github.com/username/repo.git
# You'll be prompted for username/password or token
```

**Option 3: Switch Repository URL**
If you cloned with HTTPS but want SSH:
```bash
git remote set-url origin git@github.com:username/repo.git
```

---

### Problem: "fatal: could not read Username"

**Symptoms**:
- Pushing/pulling asks for username repeatedly
- Terminal hangs waiting for input

**Solutions**:

**Store Credentials**:
```bash
# macOS
git config --global credential.helper osxkeychain

# Windows
git config --global credential.helper wincred

# Linux
git config --global credential.helper cache
```

**Or use Personal Access Token**:
- GitHub Settings → Developer settings → Personal access tokens
- Generate new token (classic)
- Use token as password when prompted

---

## Merge Conflicts

### Problem: "CONFLICT (content merge)"

**Symptoms**:
- Error message mentioning "merge conflict"
- Can't complete `git pull` or `git merge`
- Conflicted files show merge markers

**Diagnostic Questions**:
- Did multiple people edit the same part of a file?
- Are you merging two branches?

**The File Looks Like**:
```javascript
<<<<<<< HEAD
your code here
=======
their code here
>>>>>>> branch-name
```

**Solutions**:

**Step 1: Understand the Conflict**
```bash
git status
# Shows which files have conflicts
```

**Step 2: Open the Conflicted File**
- Open in your editor
- You'll see the markers (see above)

**Step 3: Choose Which Code to Keep**
- Delete the marker lines
- Keep the code you want
- If both versions are needed, merge them manually

**Example Resolution**:
```javascript
// Before:
<<<<<<< HEAD
function greet() {
  console.log("Hello");
}
=======
function greet() {
  console.log("Hi there");
}
>>>>>>> feature-branch

// After (keep whichever you want):
function greet() {
  console.log("Hello");
}
```

**Step 4: Mark as Resolved**
```bash
git add filename
git commit -m "Resolve merge conflict"
git push
```

**Prevention Tips**:
- Pull before pushing
- Merge frequently (don't let branches diverge too much)
- Coordinate with teammates on shared files
- Use `git pull --rebase` for cleaner history

---

## Commit Issues

### Problem: "nothing added to commit"

**Symptoms**:
- `git add .` doesn't stage changes
- Nothing shows in `git status`

**Diagnostic Questions**:
- Did you actually change files?
- Are the changes in a subdirectory you're not in?

**Solutions**:

**Check What Changed**:
```bash
git status
# Shows all modified files
```

**Stage Files Explicitly**:
```bash
git add specific-file.js
git commit -m "message"
```

**Common Mistake**:
```bash
# Wrong - staging nothing
git add
git commit -m "message"

# Right - staging all changes
git add .
git commit -m "message"
```

---

### Problem: "Amend" - Need to Fix Last Commit

**Symptoms**:
- Committed with wrong message
- Forgot to include a file
- Just noticed a typo

**Solutions**:

**Fix Message Only**:
```bash
git commit --amend -m "New message"
git push -f origin branch-name
```

**Include Forgotten File**:
```bash
git add forgotten-file.js
git commit --amend --no-edit
git push -f origin branch-name
```

**⚠️ Warning**: Only amend commits you haven't shared yet. If already pushed, consider using `git revert` instead.

---

## Branch Issues

### Problem: "Branch doesn't exist" or Can't Switch

**Symptoms**:
- `git switch branch-name` says branch doesn't exist
- Created a branch but can't find it

**Diagnostic Questions**:
- Did you push the branch to GitHub?
- Is it a local-only branch?

**Solutions**:

**See All Branches**:
```bash
git branch -a
# -a shows all (local + remote)
```

**If Branch is Remote Only**:
```bash
git switch -c local-name origin/remote-name
# Or
git fetch origin remote-name
git switch remote-name
```

**Delete a Branch**:
```bash
git branch -d branch-name  # Safe delete
git branch -D branch-name  # Force delete
```

**Rename a Branch**:
```bash
git branch -m old-name new-name
git push origin :old-name new-name
```

---

### Problem: "Your branch is ahead of origin"

**Symptoms**:
- Status says "ahead by X commits"
- Changes not on GitHub yet

**Solution**:
```bash
git push
# Sends your commits to GitHub
```

---

### Problem: "Detached HEAD"

**Symptoms**:
- Status shows weird branch name like commit ID
- Changes seem to be in limbo

**Explanation**: You checked out a specific commit instead of a branch.

**Solution**:
```bash
git switch main
# Go back to a real branch
```

**If You Made Changes in Detached State**:
```bash
# Save your work
git branch save-my-work

# Then switch to main
git switch main
git merge save-my-work
```

---

## Remote Issues

### Problem: "Repository not found"

**Symptoms**:
- Can't clone a repository
- Says repository doesn't exist

**Diagnostic Questions**:
- Is the URL correct?
- Is the repository private and are you authorized?
- Did you spell the name correctly?

**Solutions**:

**Verify URL**:
```bash
# Go to GitHub, click Code button, copy URL
# Make sure it's exactly right

git clone https://github.com/correct-username/correct-repo-name.git
```

**For Private Repositories**:
- Make sure you have access
- Verify SSH keys are set up
- Use `git clone https://...` and enter token if needed

---

### Problem: "Failed to connect to server"

**Symptoms**:
- Network-related error
- Can't push/pull
- "Could not resolve host"

**Solutions**:

**Check Internet Connection**:
```bash
ping github.com
# If this fails, you're offline
```

**Check Firewall/VPN**:
- Try disabling VPN temporarily
- Check if corporate firewall blocks git
- Try HTTPS instead of SSH

**Retry the Operation**:
```bash
# Often works after brief disconnection
git pull
git push
```

---

## History & Undo Issues

### Problem: "I Made a Terrible Commit - How Do I Undo?"

**Symptoms**:
- Committed code that breaks things
- Committed sensitive data
- Wrong commit message

**Solutions by Severity**:

**Option 1: Last Commit Only (Easiest)**
```bash
git reset --soft HEAD~1
# Changes go back to staging, edit them
git add .
git commit -m "Fixed version"
git push -f origin branch-name
```

**Option 2: Undo Specific Old Commit**
```bash
git log --oneline  # Find the commit
git revert commit-id  # Creates new commit that undoes it
git push
```

**Option 3: Go Back to Previous Commit**
```bash
git reset --hard HEAD~1  # Last commit
git reset --hard HEAD~3  # Last 3 commits
git push -f origin branch-name
```

**⚠️ WARNING**: `--hard` deletes everything. Only use on unpushed commits or your own branch.

---

### Problem: "Lost Commits - Where Did They Go?"

**Symptoms**:
- Made commits but they disappeared
- Branch history looks wrong

**Solution - Use Reflog**:
```bash
git reflog
# Shows all commits you've made, even deleted ones

# You'll see something like:
# a1b2c3d (HEAD) commit message
# e4f5g6h previous commit

git checkout a1b2c3d
# Go back to the lost commit

git branch recovery
# Save it in a new branch

git switch main
git merge recovery
# Get the commits back
```

---

## Push/Pull Issues

### Problem: "Failed to push - rejected"

**Symptoms**:
- Can't push changes
- Says "updates were rejected"
- Suggests you "pull first"

**Solution**:
```bash
git pull
# Gets latest from GitHub
# Merges with your changes

# Resolve any conflicts if they occur
git push
# Now you can push
```

**This is the most common issue** - teammates pushed while you were working.

---

### Problem: "Force Push Warnings"

**Symptoms**:
- Trying to do `git push -f`
- Warning about force pushing to main
- Unsure if it's safe

**Guidance**:

**Safe to Force Push**:
- Your own feature branches
- Branches only you are working on
- Before merging (not after)

**Never Force Push**:
- Main branch
- Shared branches
- After teammates have pulled from it

**Better Alternative**:
```bash
# Instead of: git push -f
# Use revert to undo safely:
git revert commit-id
git push
```

---

## Performance Issues

### Problem: "Git Operations Are Slow"

**Symptoms**:
- `git status` takes forever
- `git pull` is very slow
- Repository seems laggy

**Solutions**:

**Check Repository Size**:
```bash
du -sh .git
# If over 1GB, repository might be too large
```

**Remove Large Files**:
```bash
git gc
# Garbage collection, optimizes repository
```

**Shallow Clone (For Very Large Repos)**:
```bash
git clone --depth 1 repository-url
# Only gets latest commits, not full history
```

---

## Working Directory Issues

### Problem: "Changes Being Tracked That Shouldn't Be"

**Symptoms**:
- Files showing as modified in `git status` that you don't want to commit
- `.env`, `node_modules`, or build files appearing

**Solution - Use .gitignore**:
```bash
# Create .gitignore file
echo "node_modules/" >> .gitignore
echo ".env" >> .gitignore
echo "build/" >> .gitignore

# Remove already-tracked files
git rm --cached node_modules -r
git commit -m "Remove node_modules from tracking"
```

---

### Problem: "Accidental Large File Commit"

**Symptoms**:
- Committed a huge file by mistake
- Repository size exploded
- Now it's stuck in history

**Solution**:
```bash
# Identify the large file
git rev-list --all --objects | sort -k 2 | tail -10

# Remove it from history (complex operation)
# Consider: git filter-branch or BFG Repo-Cleaner

# For now, simplest approach:
git rm --cached large-file.bin
echo "large-file.bin" >> .gitignore
git commit -m "Remove large file from tracking"
```

**Prevention**: Add to `.gitignore` before committing.

---

## Special Cases

### Problem: "How Do I Check Out Someone Else's Branch?"

**Solution**:
```bash
git fetch origin
git switch -c local-branch origin/their-branch
# or
git switch their-branch
```

---

### Problem: "Need to Work on Multiple Branches"

**Solution - Stashing**:
```bash
# You're on branch A with changes
git stash
# Changes are saved temporarily

git switch branch-b
# Work on B

git switch branch-a
git stash pop
# Get your A changes back
```

---

## Getting Help

**General Debugging Steps**:
1. Run `git status` - what's the current state?
2. Run `git diff` - what exactly changed?
3. Run `git log --oneline` - what's the commit history?
4. Read the error message carefully - it usually tells you the problem
5. Try `git --help command-name` for command documentation

**For Complex Issues**:
- Check GitHub documentation
- Search Stack Overflow for your error message
- Ask teammates for help
- Create a minimal example to understand the problem

---

## Prevention Tips

✅ **Do These**:
- Pull before you start work
- Commit frequently with clear messages
- Push regularly so work isn't lost
- Pull before pushing
- Create feature branches for new work
- Review your diff before committing
- Use `.gitignore` for temporary files

❌ **Avoid These**:
- Committing without message
- Committing large binaries
- Working directly on main
- Force pushing shared branches
- Ignoring merge conflicts
- Committing secrets (.env files)
- Large commits with mixed changes
