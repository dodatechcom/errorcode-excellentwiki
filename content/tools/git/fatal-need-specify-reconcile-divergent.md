---
title: "[Solution] Git fatal: Need to specify how to reconcile divergent branches"
description: "Fix 'need to specify how to reconcile divergent branches' error. Resolve Git pull failures when branches have diverged and pull strategy is not set."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Need to specify how to reconcile divergent branches

fatal: Need to specify how to reconcile divergent branches.

This error occurs in Git 2.27+ when `pull.rebase` is not configured and you try to pull changes from a divergent branch. Git requires you to choose a merge strategy.

## Common Causes

- Git version 2.27 or newer with default configuration
- Local and remote branches have diverged
- `pull.rebase` or `pull.ff` not configured
- No explicit merge strategy specified

## How to Fix

### Configure Pull to Use Rebase

```bash
git config --global pull.rebase true
```

### Configure Pull to Use Merge

```bash
git config --global pull.rebase false
```

### Configure Fast-Forward Only

```bash
git config --global pull.ff only
```

### Specify Strategy Per Command

```bash
git pull --rebase origin main
git pull --no-rebase origin main
```

## Examples

```bash
# Example 1: Git 2.27+ pull fails
git pull origin main
# fatal: Need to specify how to reconcile divergent branches.
# Fix: git config --global pull.rebase true

# Example 2: Pull with explicit strategy
git pull --rebase origin main

# Example 3: Fast-forward only
git config --global pull.ff only
git pull origin main
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
