# Git & GitHub Fundamentals

## Core Distinction: Git vs GitHub

### Git
- **What it is**: A version control system software installed on your computer
- **What it does**: Tracks changes to files, maintains history, enables collaboration
- **Analogy**: Like a "time machine" for your code - you can see what changed, when, and by whom
- **Where it runs**: Locally on your machine (command line)
- **Key feature**: Creates a complete history of all changes

### GitHub
- **What it is**: A cloud platform (website) that hosts Git repositories
- **What it does**: Provides storage, collaboration tools, and project management features
- **Analogy**: Like Google Drive, but specifically designed for code with special tools
- **Where it runs**: In the cloud (web browser and via CLI)
- **Key features**: Hosting, pull requests, issues, team collaboration

### The Relationship
```
Your Computer (Git)
       ↓
    Push/Pull
       ↓
GitHub (Cloud)
```

You use **Git commands locally**, then **push to GitHub** to share.

---

## Key Concepts

### 1. Repository (Repo)
**Simple definition**: A folder that Git watches and tracks.

**What it contains**:
- Your code files
- A hidden `.git` folder (this is what makes it a "repo")
- Complete history of all changes ever made

**Two types**:
- **Local repo**: On your computer
- **Remote repo**: On GitHub (the cloud copy)

**Example**:
```
Your computer:
📁 my-project/
  📁 .git/          ← This makes it a repo
  📄 app.js
  📄 style.css
```

### 2. Commit
**Simple definition**: A "save point" in your project's history.

**What it includes**:
- The changes you made
- A message describing what you changed (ex: "Add login button")
- The author (who made it)
- Timestamp (when it was made)
- A unique ID (SHA) so you can reference it later

**Analogy**: Like saving a document with a detailed change log.

**Example commit message**: `"Fix bug where login button didn't work on mobile"`

**Key principle**: Each commit should represent one logical change - don't mix unrelated changes in one commit.

### 3. Branch
**Simple definition**: An independent line of development - like a parallel version of your code.

**Why branches exist**:
- Work on features without breaking the main code
- Multiple people work on different features simultaneously
- Keep experimental code separate from stable code

**Common branches**:
- **`main`** (or `master`): The production-ready, stable version
- **`develop`**: The development version (might be unstable)
- **Feature branches**: `add-login`, `fix-bug-123`, etc.

**Mental model**:
```
main:        ●─────●─────●─────●
              ↑ Stable, production code

my-feature:          ↓
                     ●─────●─────●
                      ↑ Your experimental work
```

### 4. Merge
**Simple definition**: Combining changes from one branch into another.

**What happens**:
- Take all commits from branch A
- Add them to branch B
- Code from both branches is now combined

**Common scenario**:
1. You work on `fix-bug` branch
2. You finish and test thoroughly
3. You merge `fix-bug` into `main`
4. Everyone gets your fix

### 5. Remote
**Simple definition**: A version of your repo on a server (usually GitHub).

**Naming convention**:
- **`origin`**: Default name for the remote (almost always GitHub)
- Can have multiple remotes, but `origin` is standard

**What it represents**:
- The "cloud copy" of your project
- The source of truth for your team

### 6. Push
**Simple definition**: Sending your local commits to the remote (GitHub).

**Direction**: Local → GitHub

**When to do it**: After making commits, to share your work

**Example flow**:
```
1. You make commits locally
2. You run: git push
3. Your changes appear on GitHub
```

### 7. Pull
**Simple definition**: Getting updates from the remote (GitHub) to your local computer.

**Direction**: GitHub → Local

**When to do it**: When teammates push changes, you pull to get them

**Example flow**:
```
1. Teammate pushes changes to GitHub
2. You run: git pull
3. Their changes appear in your local files
```

### 8. Clone
**Simple definition**: Making a complete copy of a remote repository on your computer.

**What it includes**:
- All files and folders
- Complete history of all commits
- The connection to the remote (so you can push/pull later)

**When to use it**: First time setting up a project on your computer

**Example**:
```
git clone https://github.com/username/project-name
Result: A new folder "project-name" with everything inside
```

---

## The Git Workflow (Mental Model)

### Step 1: Make Changes
```
Edit files → Save them → They appear as "modified"
```

### Step 2: Stage Changes
```
Mark files → "I want to commit these specific files"
```

### Step 3: Commit
```
Create a save point → Include a message → History is recorded
```

### Step 4: Push
```
Send commits → To GitHub → Share with team
```

### In Commands:
```bash
# Step 1: Edit files
nano app.js

# Step 2: Stage
git add app.js

# Step 3: Commit
git commit -m "Add feature X"

# Step 4: Push
git push
```

---

## Common Workflows & Patterns

### Workflow 1: Solo Developer
1. Make changes on `main`
2. Commit frequently
3. Push regularly
4. Repeat

### Workflow 2: Team Development (Recommended)
1. Create a feature branch (ex: `add-login`)
2. Make changes on that branch
3. Commit as you work
4. Push your branch
5. Open a Pull Request (ask for review)
6. Get feedback and make changes
7. Merge when approved
8. Delete the branch

### Workflow 3: Large Team
1. Each feature gets its own branch
2. Branches are created from `develop`
3. Multiple review cycles in Pull Requests
4. Merge to `develop` when ready
5. `develop` is periodically merged to `main` as releases

---

## Why This Matters

### Collaboration
Without version control, multiple people can't work on the same project without losing work. Git solves this.

### History
You can see exactly what changed, when, and why. Super useful for debugging or understanding past decisions.

### Safety
You can always go back to a previous version if something breaks.

### Branching
Teams can work on multiple features in parallel without interfering with each other.

---

## The Mental Shift

**Beginner thinking**: "I save my file, and it's done."

**Git thinking**: "I edit files → I explicitly stage the ones I want → I create a snapshot → I give it a meaningful message → I push it to share."

This extra structure feels cumbersome at first, but it enables powerful collaboration and safety nets that you'll appreciate immediately.
