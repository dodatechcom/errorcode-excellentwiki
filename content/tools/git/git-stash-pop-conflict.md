---
title: "[Solution] Git stash pop conflict"
description: "Fix Git stash pop conflict error. Resolve merge conflicts when applying stashed changes back to the working directory."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git stash pop conflict

CONFLICT (content): Merge conflict in <file>
Auto-merging <file> failed

This error occurs when you run `git stash pop` and your stashed changes conflict with the current state of the working directory.

## Common Causes

- Working directory changed since the stash was created
- Different branch than where stash was created
- Same file modified before and after the stash
- Stash was created long ago and codebase diverged
- Stash applied after pulling remote changes

## How to Fix

### Resolve Conflicts Manually

```bash
git status
# Edit conflicted files
git add <resolved-file>
git stash drop
```

### Skip Conflict Resolution (Drop Stash)

```bash
git stash drop
```

### Apply Stash as a Branch

```bash
git stash branch <new-branch>
```

### Use Stash Apply (Keep Stash)

```bash
git stash apply
# Resolve conflicts, don't drop stash
```

## Examples

```bash
# Example 1: Resolve conflicts
git stash pop
# CONFLICT (content): Merge conflict in src/main.js
# Fix: edit src/main.js, remove markers, git add src/main.js, git stash drop

# Example 2: Create branch from stash
git stash branch fix-conflicts
# Creates branch, applies stash, drops stash

# Example 3: Apply without dropping
git stash apply
# Resolve conflicts
git stash drop  # only when resolved
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
