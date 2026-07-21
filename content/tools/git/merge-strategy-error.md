---
title: "[Solution] Git Merge Strategy Error"
description: "Fix Git merge strategy errors when choosing the wrong merge strategy causes conflicts."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Merge Strategy Error

Git merge fails or produces unexpected results due to incorrect merge strategy.

```
error: Merging is not possible because of untracked files
fatal: refusing to merge unrelated histories
```

## Common Causes

- Different merge strategies produce different results
- Untracked files blocking merge
- Unrelated histories being merged
- Conflicting files not resolved
- Wrong branch checked out

## How to Fix

### Choose Correct Merge Strategy

```bash
# Default recursive merge
git merge feature-branch

# Use ours strategy to keep current branch
git merge -X ours feature-branch

# Use theirs strategy to take incoming changes
git merge -X theirs feature-branch

# Union merge for non-overlapping changes
git merge -s union feature-branch
```

### Merge Unrelated Histories

```bash
# Allow merging unrelated histories
git merge --allow-unrelated-histories feature-branch
```

### Handle Untracked Files

```bash
# Stash untracked files
git stash -u

# Merge
git merge feature-branch

# Restore stash
git stash pop
```

### Use Merge Tools

```bash
# Use configured merge tool
git mergetool

# Configure merge tool
git config merge.tool vimdiff
git config mergetool.keepBackup false
```

## Examples

```bash
# Merge with specific strategy
git merge -s ours --no-commit feature-branch

# Preview merge without committing
git merge --no-commit --no-ff feature-branch
git diff --staged
git merge --abort  # or git merge --continue
```
