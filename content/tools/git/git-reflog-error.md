---
title: "[Solution] Git reflog error"
description: "Fix 'git reflog' errors. Resolve issues when Git reflog is missing, corrupted, or has expired entries."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git reflog error

fatal: your current branch appears to be broken

This error occurs when the reflog is corrupted or the HEAD reference points to a non-existent branch.

## Common Causes

- Reflog was manually deleted or corrupted
- Branch was deleted that HEAD pointed to
- Repository was partially restored from backup
- Reflog expiration cleaned all entries
- Garbage collection cleaned reflog

## How to Fix

### Check HEAD Reference

```bash
cat .git/HEAD
```

### Create Reflog

```bash
git reflog expire --expire=now --all
git reflog
```

### Restore from ORIG_HEAD

```bash
git reset --hard ORIG_HEAD
```

### Recover Lost Commits

```bash
git fsck --lost-found
ls -la .git/lost-found/
```

## Examples

```bash
# Example 1: View reflog
git reflog show HEAD
# abc1234 HEAD@{0}: commit: Fix bug
# def5678 HEAD@{1}: commit: Add feature

# Example 2: Recover lost commit
git reflog expire --expire=now --all
git fsck --lost-found
git show .git/lost-found/commit/abc1234

# Example 3: Check HEAD
cat .git/HEAD
# ref: refs/heads/main
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
