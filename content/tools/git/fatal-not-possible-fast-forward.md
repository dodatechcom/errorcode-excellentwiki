---
title: "[Solution] Git fatal: Not possible to fast-forward"
description: "Fix 'not possible to fast-forward' error. Resolve Git merge failures when a fast-forward merge is required but not possible."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Not possible to fast-forward

fatal: Not possible to fast-forward, aborting.

This error occurs when you attempt a merge with `--ff-only` flag but the branches have diverged and cannot be merged with a fast-forward.

## Common Causes

- Branches have diverged with different commits
- `git merge --ff-only` is configured as default
- Remote branch has commits not in local branch
- Local branch has commits not in remote branch

## How to Fix

### Allow a Merge Commit

```bash
git merge --no-ff <branch>
```

### Rebase Instead

```bash
git checkout <branch>
git rebase main
git checkout main
git merge <branch>
```

### Pull with Rebase

```bash
git pull --rebase origin main
```

## Examples

```bash
# Example 1: ff-only merge fails
git merge --ff-only feature/branch
# fatal: Not possible to fast-forward, aborting.
# Fix: git merge --no-ff feature/branch

# Example 2: Rebase before merge
git checkout feature/login
git rebase main
git checkout main
git merge feature/login

# Example 3: Pull with rebase to avoid merge commits
git pull --rebase origin main
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
