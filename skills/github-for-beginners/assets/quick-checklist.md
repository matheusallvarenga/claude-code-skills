# GitHub Quick Checklist

Print or bookmark this checklist for your daily GitHub work.

---

## Before Starting Work

- [ ] Navigate to your project directory
- [ ] Run `git pull` to get latest changes
- [ ] Check `git status` to see current state
- [ ] Create feature branch if starting new work: `git switch -c feature-name`

---

## While Working (Repeat as Needed)

- [ ] Edit files
- [ ] Test changes locally
- [ ] Review changes: `git diff`
- [ ] Stage files: `git add .`
- [ ] Commit: `git commit -m "Clear message"`
- [ ] Repeat steps 1-4 as you work

---

## Before Pushing

- [ ] Run tests: `npm test` or similar
- [ ] Review commit history: `git log --oneline -5`
- [ ] Verify all changes are staged: `git status`
- [ ] Check for uncommitted changes: `git diff`

---

## Pushing to GitHub

- [ ] Pull latest first: `git pull`
- [ ] Push changes: `git push`
  - First time on new branch: `git push -u origin branch-name`
  - Subsequent: `git push`

---

## Creating a Pull Request

- [ ] Go to your GitHub repository
- [ ] Click "Compare & Pull Request" (or "New Pull Request")
- [ ] Fill in:
  - [ ] Clear title describing what you changed
  - [ ] Description explaining why and what
  - [ ] Link to related issue if applicable
- [ ] Click "Create Pull Request"

---

## Handling Code Review

- [ ] Read reviewer comments carefully
- [ ] Make requested changes
- [ ] Commit changes: `git commit -m "Address review feedback"`
- [ ] Push: `git push`
- [ ] Comment on PR to notify reviewer
- [ ] Repeat until approved

---

## Merging to Main

- [ ] Get approval from reviewer
- [ ] Click "Merge Pull Request" on GitHub
- [ ] Choose merge type: "Create a merge commit"
- [ ] Click "Confirm merge"
- [ ] Click "Delete branch" (cleanup)

---

## After Merging

- [ ] Switch to main locally: `git switch main`
- [ ] Pull: `git pull`
- [ ] Delete local branch: `git branch -d branch-name`
- [ ] Verify on GitHub that changes are there

---

## Common Commands Quick Reference

```bash
# Setup
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Daily Work
git status                    # What changed?
git diff                      # Show changes
git add .                     # Stage all
git commit -m "message"       # Create save point
git push                      # Send to GitHub
git pull                      # Get updates

# Branching
git switch -c new-feature     # Create branch
git switch main               # Switch branch
git branch -d old-feature     # Delete branch

# Viewing History
git log --oneline             # See commits
git show commit-id            # Details of commit

# Undo
git reset --soft HEAD~1       # Undo last commit, keep changes
git restore filename          # Undo changes to file
```

---

## Emergency Commands

```bash
# "I messed up, let me go back"
git status                    # See the damage
git reset --hard HEAD        # Undo all local changes
git pull                     # Get fresh copy

# "I committed the wrong thing"
git reset --soft HEAD~1      # Undo last commit
git add .                    # Re-stage what you want
git commit -m "Fixed"        # Commit again

# "I have a merge conflict"
git status                   # See conflicted files
# Open files, remove conflict markers
git add .
git commit -m "Resolve conflict"
git push
```

---

## Red Flags - Don't Do This

- ❌ Don't commit to `main` directly
- ❌ Don't force push to `main`
- ❌ Don't commit passwords or API keys
- ❌ Don't commit `node_modules` or build files
- ❌ Don't merge without reviewing
- ❌ Don't ignore merge conflicts
- ❌ Don't make commits with vague messages
- ❌ Don't mix multiple features in one commit

---

## Using Claude Code

```bash
# In GitHub issue or PR comment:
@claude fix the login button styling on mobile

# Claude will:
# 1. Analyze your code
# 2. Make changes
# 3. Create commit
# 4. Push changes
# 5. Comment with summary

# Then:
# 1. Review Claude's changes
# 2. Test locally
# 3. Merge if satisfied
```

---

## Getting Help

- Check commit history: `git log`
- See what changed: `git diff`
- Confused about merge?: Check troubleshooting guide
- Lost commits?: Use `git reflog`
- Need to learn more?: Check references in skill
