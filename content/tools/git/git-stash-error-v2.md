---
title: "[Solution] Git Stash Pop Conflict"
description: "Fix Git stash pop conflicts. Resolve merge conflicts when applying stashed changes."
tools: ["git"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stash", "pop", "conflict", "apply", "git"]
weight: 5
---

## What This Error Means

A stash pop conflict occurs when `git stash pop` cannot cleanly apply the stashed changes because the current working directory has conflicting modifications. The stash remains in the stash list to prevent data loss.

## Common Causes

- The working directory has changes to the same files as the stash
- The branch has been modified since the stash was created
- Files were deleted or renamed after stashing
- The stash conflicts with uncommitted staged changes

## How to Fix

### Check Stash Status

```bash
git stash list
git status
```

### Resolve the Conflict

```bash
# Edit conflicted files, remove markers
git add <resolved-file>
# The stash is still in the list; drop it manually
git stash drop
```

### Apply Without Auto-Merging

```bash
git stash apply
# Manually resolve conflicts
```

### Use a Specific Stash

```bash
git stash pop stash@{2}
```

### Drop the Stash After Resolution

```bash
git stash drop
# Or drop all stashes
git stash clear
```

## Examples

```bash
# Example 1: Stash pop conflict
git stash pop
# CONFLICT (content): Merge conflict in src/utils.js
# The stash entry is kept in case you need it again.

# Resolve
git add src/utils.js
git stash drop

# Example 2: Apply specific stash
git stash list
# stash@{0}: WIP on feature: abc1234 Add login
# stash@{1}: WIP on main: def5678 Update API

git stash apply stash@{1}

# Example 3: Stash untracked files
git stash -u
git stash pop
```

## Related Errors

- [Git Merge Conflict]({{< relref "/tools/git/git-merge-conflict-v2" >}}) — merge conflict in file
- [Git Detached HEAD]({{< relref "/tools/git/git-detached-head-v2" >}}) — HEAD not on a branch
- [Git Fetch Error]({{< relref "/tools/git/git-fetch-error" >}}) — fetch failed
