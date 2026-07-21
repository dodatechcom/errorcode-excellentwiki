---
title: "[Solution] Git Pull Error"
description: "Fix Git pull errors when fetching and merging from remote fails."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Pull Error

Git pull fails to fetch and integrate changes from the remote repository.

```
error: Your local changes to the following files would be overwritten
```

## Common Causes

- Local changes conflicting with remote
- Branch tracking not configured
- Unrelated histories being pulled
- Remote branch was force-pushed
- Submodule changes not handled

## How to Fix

### Stash Local Changes

```bash
# Stash before pull
git stash
git pull
git stash pop

# Or discard changes
git checkout -- .
git pull
```

### Use Rebase Instead of Merge

```bash
# Pull with rebase
git pull --rebase

# Set as default
git config --global pull.rebase true
```

### Configure Upstream Branch

```bash
# Set upstream for current branch
git branch --set-upstream-to=origin/main main

# Pull with explicit branch
git pull origin main
```

### Handle Force-Pushed Remote

```bash
# Fetch and reset to remote
git fetch origin
git reset --hard origin/main
```

### Pull with Tags

```bash
# Pull and fetch tags
git pull --tags

# Fetch tags only
git fetch --tags
```

## Examples

```bash
# Safe pull workflow
git stash -u  # Include untracked files
git pull --rebase
git stash pop

# Check before pulling
git fetch origin
git log --oneline HEAD..origin/main
git merge origin/main
```
