---
title: "[Solution] Git merge abort error"
description: "Fix 'git merge --abort' error when aborting a failed merge operation in Git."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git merge abort error

fatal: There is no merge to abort (MERGE_HEAD missing).

This error occurs when you run `git merge --abort` but there is no in-progress merge to abort.

## Common Causes

- No merge was started
- Merge already completed or was already aborted
- MERGE_HEAD file was manually deleted
- Conflict was resolved and committed already
- Wrong repository

## How to Fix

### Check Merge Status

```bash
git status
```

### Check for MERGE_HEAD

```bash
ls -la .git/MERGE_HEAD
```

### Reset to Pre-Merge State

```bash
git reset --hard ORIG_HEAD
```

### Verify Repository State

```bash
git log --oneline -1
```

## Examples

```bash
# Example 1: No merge in progress
git merge --abort
# fatal: There is no merge to abort (MERGE_HEAD missing).
# Fix: check git status first

# Example 2: Reset to ORIG_HEAD
git reset --hard ORIG_HEAD

# Example 3: Merge was already committed
# Check latest commit is the merge
git log --oneline -3
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
