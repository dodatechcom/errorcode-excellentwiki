---
title: "[Solution] Git Worktree Operation Error"
description: "Fix Git worktree errors. Resolve worktree add, remove, and list failures."
tools: ["git"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Git worktree error occurs when creating, removing, or managing linked working trees fails. Worktrees allow you to check out multiple branches simultaneously in separate directories, but they require the branch to not be already checked out elsewhere.

## Common Causes

- The branch is already checked out in another worktree
- The worktree directory already exists or has conflicts
- The worktree path is inside the main repository
- Trying to add a worktree for a branch that is checked out in the main working directory
- Worktree directory was manually deleted without using `git worktree remove`

## How to Fix

### List Existing Worktrees

```bash
git worktree list
```

### Add a New Worktree

```bash
git worktree add ../feature-branch feature/login
```

### Remove a Worktree

```bash
git worktree remove ../feature-branch
```

### Prune Stale Worktrees

```bash
git worktree prune
```

### Force Remove a Worktree

```bash
git worktree remove --force ../feature-branch
```

## Examples

```bash
# Example 1: Branch already checked out
git worktree add ../hotfix hotfix/bug
# fatal: 'hotfix/bug' is already checked out at '../other-dir'

# Fix: use a different branch or remove the other worktree
git worktree remove ../other-dir

# Example 2: Create worktree for new branch
git worktree add -b feature/new-api ../new-api main

# Example 3: Clean up after manual deletion
git worktree prune
git worktree list
```

## Related Errors

- [Git Branch Error]({{< relref "/tools/git/git-branch-error" >}}) — branch operation error
- [Git Detached HEAD]({{< relref "/tools/git/git-detached-head-v2" >}}) — HEAD not on a branch
- [Git Fetch Error]({{< relref "/tools/git/git-fetch-error" >}}) — fetch failed
