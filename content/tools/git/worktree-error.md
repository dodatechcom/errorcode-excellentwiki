---
title: "[Solution] Git Worktree Error"
description: "Fix Git worktree errors when creating or managing multiple working trees fails."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Worktree Error

Git worktree operations fail when managing multiple working directories.

```
fatal: 'worktree' is not a working tree
error: pathspec 'worktree' did not match
```

## Common Causes

- Worktree directory already exists
- Branch already checked out in another worktree
- Worktree not properly removed
- Path does not exist
- Insufficient permissions

## How to Fix

### Create Worktree

```bash
# Create worktree for new branch
git worktree add ../project-feature feature-branch

# Create worktree for existing branch
git worktree add ../project-main main

# Create worktree at specific commit
git worktree add --detach ../project-abc abc123
```

### List Worktrees

```bash
# List all worktrees
git worktree list

# Show worktree details
git worktree list -v
```

### Remove Worktree

```bash
# Remove worktree
git worktree remove ../project-feature

# Force remove
git worktree remove --force ../project-feature

# Prune stale worktree references
git worktree prune
```

### Fix Branch Already Checked Out

```bash
# Check which worktree has the branch
git worktree list

# Use different branch
git worktree add ../project-new new-branch

# Or detach HEAD in worktree
git worktree add --detach ../project-temp main
```

### Move Worktree

```bash
# Move worktree location
git worktree move ../project-old ../project-new
```

## Examples

```bash
# Full worktree workflow
git worktree add ../hotfix-branch hotfix-1.0
cd ../hotfix-branch
# Make fixes
git add .
git commit -m "Hotfix"
cd ../main-project
git merge hotfix-1.0
git worktree remove ../hotfix-branch
```
