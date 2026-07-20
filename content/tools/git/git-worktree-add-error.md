---
title: "[Solution] Git worktree add error"
description: "Fix 'git worktree add' error. Resolve issues when adding a new working tree linked to the repository."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git worktree add error

fatal: '<path>' already exists

This error occurs when you try to add a Git worktree at a path that already has files or is an existing directory.

## Common Causes

- Target directory already exists and is not empty
- Branch is already checked out in another worktree
- Worktree path is already in use
- Invalid path specified

## How to Fix

### Use a Different Path

```bash
git worktree add ../repo-feature feature-branch
```

### Remove Existing Directory

```bash
rm -rf <path>
git worktree add <path> <branch>
```

### List Existing Worktrees

```bash
git worktree list
```

### Prune Stale Worktrees

```bash
git worktree prune
```

## Examples

```bash
# Example 1: Path already exists
git worktree add ./hotfix hotfix-branch
# fatal: './hotfix' already exists
# Fix: git worktree add ../hotfix hotfix-branch

# Example 2: Check branch usage
git worktree list
# /main-repo          abc1234 [main]
# /feature-worktree   def5678 [feature/login]
# Fix: use different branch for new worktree

# Example 3: Prune stale worktrees
git worktree prune
git worktree add ../new-feature feature/new
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
