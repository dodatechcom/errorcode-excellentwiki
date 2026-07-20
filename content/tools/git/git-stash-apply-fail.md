---
title: "[Solution] Git stash apply failed"
description: "Fix 'git stash apply failed' error. Resolve issues when applying a stash to the current working directory."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git stash apply failed

Auto-merging <file>
CONFLICT (content): Merge conflict in <file>

This error occurs when `git stash apply` cannot cleanly apply stashed changes to the current working tree because of conflicts.

## Common Causes

- Current branch differs from where stash was created
- Files modified after stash was made
- Uncommitted changes conflict with stash
- Stash was created long ago and code changed significantly

## How to Fix

### Resolve Conflicts

```bash
git status
# Edit conflicted files
git add <file>
git stash drop  # if satisfied
```

### Create Branch from Stash

```bash
git stash branch <new-branch>
```

### Apply to Different Branch

```bash
git checkout <original-branch>
git stash apply
```

### List and Choose Stash

```bash
git stash list
git stash show -p stash@{n}
```

## Examples

```bash
# Example 1: Resolve conflicts
git stash apply
# Auto-merging src/config.js - CONFLICT
git add src/config.js
git stash drop

# Example 2: Create branch from stash
git stash branch recovery-branch
# Applies stash on new branch at original commit

# Example 3: Apply specific stash
git stash apply stash@{2}
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
