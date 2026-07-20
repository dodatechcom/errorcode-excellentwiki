---
title: "[Solution] Git switch branch error"
description: "Fix 'git switch' errors. Resolve issues when using the modern 'git switch' command to change branches."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git switch branch error

fatal: 'branch' is not a branch

This error occurs when you try to switch to a remote-tracking reference or commit hash using `git switch` without creating a new branch.

## Common Causes

- Trying to switch to a remote branch without creating local
- Using `git switch` with a commit hash
- Branch name doesn't exist
- Using `git switch` for detached HEAD state

## How to Fix

### Create Branch from Remote

```bash
git switch -c <branch> origin/<branch>
```

### Switch to Existing Branch

```bash
git switch <existing-branch>
```

### Create New Branch

```bash
git switch -c <new-branch>
```

### Use Detach for Commits

```bash
git switch --detach <commit>
```

## Examples

```bash
# Example 1: Switch to remote branch
git switch feature/login
# fatal: 'feature/login' is not a branch
# Fix: git switch -c feature/login origin/feature/login

# Example 2: Create and switch
git switch -c new-feature

# Example 3: Switch to commit (detached)
git switch --detach HEAD~3
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
