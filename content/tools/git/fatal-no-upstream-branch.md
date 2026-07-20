---
title: "[Solution] Git fatal: No upstream branch configured"
description: "Fix 'no upstream branch configured' error. Resolve Git push failures when the current branch has no remote tracking branch set."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: No upstream branch configured

fatal: The current branch <branch> has no upstream branch.

This error occurs when you try to push a branch that has no remote tracking branch configured. Git does not know where to push your changes.

## Common Causes

- Created a new local branch without pushing
- Removed the remote tracking branch
- Cloned without checking out a branch
- Switched to a branch without a remote counterpart

## How to Fix

### Push with Upstream

```bash
git push -u origin <branch>
```

### Set Upstream for Current Branch

```bash
git branch --set-upstream-to=origin/<branch> <branch>
```

### Push to Current Branch Automatically

```bash
git config --global push.default current
```

## Examples

```bash
# Example 1: New local branch
git checkout -b feature/new-api
git push
# fatal: The current branch feature/new-api has no upstream branch.
# Fix: git push -u origin feature/new-api

# Example 2: Set upstream after the fact
git branch --set-upstream-to=origin/feature/new-api feature/new-api

# Example 3: Configure automatic upstream
git push -u origin main
# Next time: git push (works without arguments)
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
