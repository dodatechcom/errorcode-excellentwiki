---
title: "[Solution] Git revert merge commit error"
description: "Fix 'revert a merge' error. Resolve Git revert failures when reverting a merge commit requires specifying the parent number."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git revert merge commit error

fatal: Commit <hash> is a merge but no -m option was given.

This error occurs when you try to revert a merge commit without specifying which parent to follow with the `-m` flag.

## Common Causes

- Running `git revert <merge-commit>` without `-m`
- Merge commit has multiple parents
- Unclear which parent represents the mainline

## How to Fix

### Revert with Parent 1 (Main Branch)

```bash
git revert -m 1 <merge-commit>
```

### Revert with Parent 2 (Feature Branch)

```bash
git revert -m 2 <merge-commit>
```

### View Merge Parents

```bash
git log --oneline --graph <merge-commit>
git cat-file -p <merge-commit> | grep parent
```

## Examples

```bash
# Example 1: Revert a merge
git log --oneline -5
# abc1234 Merge branch 'feature/login' into main
git revert -m 1 abc1234
# Reverts the merge, keeping main's changes

# Example 2: Check parents
git cat-file -p abc1234 | grep parent
# parent def1234... (main)
# parent 789abcd... (feature/login)
# Fix: git revert -m 1 abc1234

# Example 3: Revert merge with commit message
git revert -m 1 abc1234 -n
git commit -m "Revert: feature login merge"
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
