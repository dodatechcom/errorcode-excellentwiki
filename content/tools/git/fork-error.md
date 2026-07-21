---
title: "[Solution] Git Fork Error"
description: "Fix Git fork errors when forking repositories or syncing forks with upstream fails."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Fork Error

Git operations fail when working with forks and upstream repositories.

```
fatal: remote upstream already exists
```

## Common Causes

- Upstream remote already configured
- Fork is behind upstream
- Permission denied on fork
- Diverged history causing conflicts
- Wrong branch tracking setup

## How to Fix

### Add Upstream Remote

```bash
# Add upstream to fork
git remote add upstream https://github.com/original/repo.git

# Verify remotes
git remote -v
```

### Sync Fork with Upstream

```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream main
git checkout main
git merge upstream/main

# Or rebase
git rebase upstream/main

# Push changes
git push origin main
```

### Remove Upstream Remote

```bash
# Remove upstream
git remote remove upstream

# Re-add with correct URL
git remote add upstream https://github.com/correct/repo.git
```

### Fix Remote Tracking

```bash
# Set upstream branch for fork
git branch --set-upstream-to=origin/main main

# Check tracking branches
git branch -vv
```

## Examples

```bash
# Complete fork sync workflow
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# Clean up merged branches
git branch --merged main | grep -v main | xargs -r git branch -d
```
