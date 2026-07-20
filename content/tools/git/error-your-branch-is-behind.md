---
title: "[Solution] Git error: Your branch is behind"
description: "Fix 'Your branch is behind' error. Resolve Git push failures when the local branch is outdated compared to the remote branch."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git error: Your branch is behind

Updates were rejected because the remote contains work that you do not have locally.

This error occurs when your local branch has fallen behind the remote branch. You need to integrate the remote changes before pushing.

## Common Causes

- Someone else pushed to the same branch
- You worked on a different machine
- Branch was force-pushed by another contributor
- You forgot to pull before making changes

## How to Fix

### Pull Remote Changes

```bash
git pull origin <branch>
```

### Pull with Rebase

```bash
git pull --rebase origin <branch>
```

### Check Status

```bash
git status
git log --oneline HEAD..origin/<branch>
```

### Force Push (use with caution)

```bash
git push --force-with-lease origin <branch>
```

## Examples

```bash
# Example 1: Behind remote
git push origin main
# ! [rejected] main -> main (fetch first)
# Fix: git pull origin main && git push origin main

# Example 2: Rebase to keep history clean
git pull --rebase origin main
git push origin main

# Example 3: Check divergence
git log --oneline -5 HEAD..origin/main
# Shows commits you're missing
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
