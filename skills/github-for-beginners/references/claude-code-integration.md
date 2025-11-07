# GitHub + Claude Code Integration

Complete guide for using Claude Code with your GitHub repository.

---

## What Is Claude Code?

Claude Code is an AI-powered agent that integrates with GitHub to help with code development. It can:

- **Read and understand** your entire codebase
- **Make code changes** based on your instructions
- **Create commits** and push changes automatically
- **Participate in discussions** on issues and pull requests

Think of it as a highly skilled developer who can work on your repository when you ask.

---

## How Your Setup Works

### The Architecture

You have configured:

1. **GitHub App**: Installed on your repository at `https://github.com/apps/claude`
2. **Workflow File**: `.github/workflows/claude.yml` that triggers Claude Code
3. **Authentication**: `ANTHROPIC_API_KEY` secret for API access

### The Flow

```
1. You create issue/PR or comment @claude
          ↓
2. GitHub detects mention
          ↓
3. GitHub Actions runs the Claude Code workflow
          ↓
4. Claude Code receives your request
          ↓
5. Claude analyzes your codebase
          ↓
6. Claude makes changes and commits
          ↓
7. Claude pushes changes to GitHub
          ↓
8. Claude comments with summary
```

---

## Using Claude Code

### Basic Usage

In any GitHub issue, PR, or discussion, mention Claude Code like this:

```
@claude fix the login button styling on mobile devices
```

Claude will:
1. Analyze your repository
2. Understand the problem
3. Make necessary changes
4. Create a commit
5. Push to the repository
6. Comment with what was done

### Where You Can Use It

**Issues**:
- Create new issue
- Write description with @claude mention
- Claude responds with changes

**Pull Requests**:
- Comment on PR: `@claude address the review feedback`
- Claude makes changes and pushes to the PR

**PR Reviews**:
- Comment on specific code line
- Mention @claude to request fix
- Claude updates the code

**Discussions**:
- Use in any discussion or comment

### Command Formats

**Direct Request**:
```
@claude add email validation to the signup form
```

**Specific File**:
```
@claude fix the bug in src/components/Button.js related to click handling
```

**With Context**:
```
@claude implement the feature described in issue #42

The feature should:
- Allow users to export data
- Support CSV and JSON formats
- Show progress indicator
```

**Complex Request**:
```
@claude refactor the authentication system

Current issues:
- Password stored in plaintext
- No session management
- Login endpoint vulnerable to timing attacks

Requirements:
- Use bcrypt for passwords
- Implement JWT tokens
- Add rate limiting

See issue #15 for more context.
```

---

## Getting Good Results

### Be Specific

**Vague Requests** (Poor Results):
- "Make it better"
- "Fix bugs"
- "Improve the code"

**Specific Requests** (Good Results):
- "Add input validation to the email field that checks for valid format"
- "Fix the crash that happens when user uploads files larger than 5MB"
- "Improve performance of database query in getUser function by adding indexes"

### Provide Context

Include relevant information:
```
@claude fix the layout issue

The navbar is overlapping the main content on mobile.
It should be below the content or collapse into a hamburger menu.
I've already attempted fix in PR #45 but it didn't work.

This is blocking the mobile launch.
```

### One Task at a Time

**Good**:
- 🟢 Issue: "Add password reset email feature"
- 🟢 Issue: "Implement dark mode toggle"
- 🟢 Issue: "Add database connection pooling"

**Poor**:
- 🔴 Issue: "Add password reset, dark mode, connection pooling, and refactor the entire auth system"

### Include Acceptance Criteria

```
@claude implement user registration form

Acceptance Criteria:
- [ ] Form has email and password fields
- [ ] Email validation checks for @ symbol
- [ ] Password requires minimum 8 characters
- [ ] Submit button is disabled while loading
- [ ] Success message shown after registration
- [ ] Form is responsive on mobile (tested on iPhone)

Related issue: #23
```

---

## Reviewing Claude's Changes

Always review what Claude Code creates before merging.

### Checklist

**Code Quality**:
- [ ] Code is readable and well-formatted
- [ ] Changes match the request
- [ ] Unnecessary changes are minimized
- [ ] No obvious bugs

**Testing**:
- [ ] Run tests locally: `npm test` or similar
- [ ] Manually test the feature if possible
- [ ] Check for edge cases

**Commit Quality**:
- [ ] Commit message is clear and descriptive
- [ ] Commit doesn't mix unrelated changes

**Security**:
- [ ] No secrets committed (API keys, passwords)
- [ ] No SQL injection vulnerabilities
- [ ] User input is validated
- [ ] No dangerous dependencies added

### Asking for Revisions

If Claude's work isn't quite right:

```
@claude the implementation is close but needs adjustments:

1. The email validation is too strict - should accept emails with + symbol
2. Password should show strength indicator
3. The form should clear after successful submission

Can you update the code with these changes?
```

Claude will read the comments and update the code.

---

## Workflow Patterns

### Pattern 1: Simple Feature Implementation

```
1. Create Issue: "Add dark mode toggle"
2. Comment: "@claude implement dark mode toggle in settings"
3. Claude makes changes and commits
4. You test locally
5. You merge if satisfied
6. Done!
```

### Pattern 2: Bug Fix with Debugging

```
1. Create Issue: "Login fails on Safari"
2. Include details: browser version, error message, steps to reproduce
3. Comment: "@claude debug and fix the Safari login issue"
4. Claude analyzes and fixes
5. You test on Safari
6. Merge if fixed
```

### Pattern 3: Code Review Collaboration

```
1. You create a PR with your own code
2. Teammate leaves comments
3. You comment: "@claude address the review feedback in PR #45"
4. Claude reads comments and updates code
5. Teammate approves
6. Merge
```

### Pattern 4: Refactoring Request

```
1. Create Issue: "Refactor authentication module"
2. Comment: "@claude refactor auth.js to be more maintainable

Current problems:
- Function is 200 lines long
- No error handling
- Hard to test

Target:
- Break into smaller functions
- Add try-catch blocks
- Make testable with dependency injection"
3. Claude refactors
4. Review changes
5. Merge
```

---

## Best Practices

### Before You Ask Claude

1. **Create an Issue First**
   - Describe the problem or feature
   - This gives Claude context
   - Link to the issue in your request

2. **Verify It's Actually a Bug**
   - Is it really broken or expected behavior?
   - Can you reproduce it?
   - Is it a recent change?

3. **Have a Plan**
   - Know what you want before asking
   - Rough idea of solution is helpful
   - Share that context

### In Your Request

1. **Be Professional Yet Clear**
   - Clear language is important for AI
   - Technical terminology is fine
   - Include links to related issues

2. **Include Examples**
   ```
   @claude add validation to form fields

   Example of desired behavior:
   - Email field: should accept user@example.com format
   - Password: should require 8+ characters
   - Phone: should accept (123) 456-7890 format
   ```

3. **State Constraints**
   ```
   @claude optimize the database query

   Constraints:
   - Must complete in under 100ms
   - Cannot add new database tables
   - Must be backwards compatible
   ```

### After Claude Finishes

1. **Test Thoroughly**
   - Local testing is essential
   - Run the test suite
   - Try edge cases

2. **Request Changes if Needed**
   - Don't settle for "good enough"
   - Ask for improvements
   - Claude can iterate

3. **Provide Feedback**
   - Comment on what worked well
   - Note what to improve
   - This helps Claude learn your preferences

4. **Review Git History**
   ```bash
   git log --oneline -5
   # See what Claude committed

   git show commit-id
   # Review the actual changes
   ```

---

## Common Use Cases

### Use Case 1: Adding New Features

```
@claude implement user profile page

Requirements:
- Show user information (name, email, avatar)
- Allow editing profile information
- Show last login time
- Display user's posts/activities

Design: Use the existing ProfileCard component
File location: src/pages/Profile.js
```

### Use Case 2: Bug Fixes

```
@claude fix the memory leak in the chat component

The chat component uses more memory each time you send a message.
I've identified it's in the message event listener.
It's probably not unsubscribing properly.

See PR #42 for failed attempt.
```

### Use Case 3: Performance Optimization

```
@claude optimize the product list page load time

Currently takes 3 seconds to load.
Should load in under 500ms.

Current approach:
- Loads all products at once
- Renders in single component

Suggested approach:
- Implement pagination or infinite scroll
- Lazy load product images
- Optimize database query
```

### Use Case 4: Testing

```
@claude write unit tests for the payment module

Current coverage: 20%
Target coverage: 80%+

Test the following functions:
- validateCardNumber()
- processPayment()
- handleRefund()
- validateExpiry()
```

### Use Case 5: Documentation

```
@claude write API documentation

Add to docs/api.md:
- All endpoints in src/routes/api.js
- Include request/response examples
- Document error codes
- Add authentication requirements
```

---

## Limitations to Know

Claude Code can:
- ✅ Read and modify existing code
- ✅ Create new files
- ✅ Run Git commands
- ✅ Understand context from repository
- ✅ Write tests
- ✅ Refactor code
- ✅ Fix bugs
- ✅ Add features

Claude Code cannot:
- ❌ Deploy to production
- ❌ Access databases directly
- ❌ Make external API calls
- ❌ Access secrets (except for committing)
- ❌ Run long background processes
- ❌ Install system packages
- ❌ Access your local computer files

---

## Troubleshooting Claude Code

### Problem: Claude Doesn't Respond

**Possible Causes**:
- Workflow not configured correctly
- API key is invalid
- GitHub App not installed on repository

**Solution**:
```bash
# Verify workflow file exists
cat .github/workflows/claude.yml

# Verify GitHub App is installed
# Go to: Settings → Installed GitHub Apps → should see "Claude"
```

### Problem: Claude's Changes Are Wrong

**Possible Causes**:
- Request wasn't clear enough
- Claude misunderstood the codebase
- Request was too complex

**Solution**:
- Leave a comment with clearer instructions
- Provide more context
- Break into smaller requests

### Problem: Merge Conflicts After Claude's Changes

**Cause**: Someone else pushed changes while Claude was working

**Solution**:
```bash
git pull
git status  # See conflicts
# Resolve conflicts manually
git add .
git commit -m "Resolve merge conflicts"
git push
```

---

## Advanced Usage

### Using Claude for Code Reviews

```
@claude review this PR and suggest improvements

PR #45 adds authentication to the admin panel.
Please check for:
- Security issues
- Performance problems
- Code style violations
- Test coverage
```

### Iterative Development

```
Iteration 1:
@claude create basic form for user registration

Iteration 2:
@claude add validation and error messages

Iteration 3:
@claude add loading states and success notifications

Iteration 4:
@claude test on mobile and fix responsive design
```

### Documentation Generation

```
@claude generate documentation for the database module

Include:
- Function signatures
- Parameter descriptions
- Return types
- Usage examples
- Error conditions
```

---

## Tips for Success

1. **Keep Requests Focused** - One feature per request
2. **Be Descriptive** - More context = better results
3. **Review Everything** - Never merge without reviewing
4. **Test Thoroughly** - Run tests and manual testing
5. **Provide Feedback** - Tell Claude what worked or didn't
6. **Use Issues for Planning** - Organize requests in issues
7. **Link Related Items** - Reference issues and PRs
8. **Be Patient** - Complex requests take time
9. **Iterate** - Ask for improvements if needed
10. **Learn from Results** - Notice patterns in what works well
