---
title: "[Solution] Git Push Rejected — Updates were rejected"
description: "Fix Git push rejected error. Resolve Updates were rejected when pushing to remote repository."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["push-rejected", "rejected", "updates", "git"]
weight: 5
---

# Git Push Rejected — Updates were rejected

This error occurs when your local branch has diverged from the remote branch. The remote contains work that you don't have locally, so Git rejects the push to prevent overwriting remote changes.

## Common Causes

- Remote branch has commits you haven't pulled yet
- Someone else pushed changes to the same branch
- You're pushing to a protected branch without permission
- Force push was required but not used

## How to Fix

### Pull Remote Changes First

```bash
git pull origin <branch>
```

### Pull with Rebase

```bash
git pull --rebase origin <branch>
```

### Force Push (use with caution)

```bash
git push --force-with-lease origin <branch>
```

### Set Upstream Branch

```bash
git push -u origin <branch>
```

### Check Remote Status

```bash
git fetch origin
git log --oneline HEAD..origin/<branch>
```

## Examples

```bash
# Example 1: Push rejected due to remote changes
git push origin main
# ! [rejected] main -> main (non-fast-forward)
# Fix: git pull origin main && git push origin main

# Example 2: Force push after rebase
git pull --rebase origin main
git push --force-with-lease origin main

# Example 3: New branch without upstream
git push origin feature/new-api
# Fix: git push -u origin feature/new-api
```

## Related Errors

- [Detached HEAD]({{< relref "/tools/git/detached-head" >}}) — working on a commit not attached to a branch
- [Branch Not Found]({{< relref "/tools/git/branch-not-found" >}}) — branch does not exist
