---
title: "[Solution] Git Stash Pop Conflict — UU merge conflict in X"
description: "Fix Git stash pop conflict. Resolve merge conflicts when applying stashed changes."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["stash", "pop", "conflict", "merge", "git"]
weight: 5
---

# Git Stash Pop Conflict — UU merge conflict in X

When running `git stash pop`, conflicts can occur if the stashed changes overlap with current changes in the working directory. Git cannot automatically merge both sets of changes.

## Common Causes

- Stashed changes modify the same files as current working changes
- Working directory has uncommitted changes that conflict with stash
- Stash contains changes from a different branch state
- File was deleted or renamed since the stash was created

## How to Fix

### Check Stash Status

```bash
git status
```

### Resolve Conflicts Manually

Edit the conflicted files, remove conflict markers, and save.

### Mark Conflicts as Resolved

```bash
git add <resolved-file>
```

### Drop the Stash (if pop failed)

```bash
git stash drop
```

### Apply Stash Without Auto-Merge

```bash
git stash show -p | git apply --3way
```

### View Stash Contents Before Applying

```bash
git stash show -p stash@{0}
```

## Examples

```bash
# Example 1: Stash pop causes conflict
git stash pop
# UU src/config.js
# Fix: edit src/config.js, resolve conflict, then git add src/config.js

# Example 2: View stash before applying
git stash show -p stash@{0} | head -50

# Example 3: Apply stash with 3-way merge
git stash show -p | git apply --3way
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — conflict when merging branches
- [Cherry-Pick Failed]({{< relref "/tools/git/cherry-pick-failed" >}}) — cherry-pick operation failed
