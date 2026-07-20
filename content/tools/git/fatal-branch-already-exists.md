---
title: "[Solution] Git fatal: A branch named already exists"
description: "Fix 'a branch named already exists' error. Resolve Git branch creation failures when a branch with the name already exists."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: A branch named already exists

fatal: A branch named '<branch>' already exists.

This error occurs when you try to create a branch with a name that already exists in your local repository. Branch names must be unique.

## Common Causes

- Branch already exists locally
- Case-insensitive branch name collision
- Trying to recreate a deleted branch without cleaning up
- Remote-tracking branch has same name

## How to Fix

### List Existing Branches

```bash
git branch -a
```

### Check Out Existing Branch

```bash
git checkout <branch>
```

### Delete Local Branch

```bash
git branch -d <branch>
```

### Use a Different Name

```bash
git checkout -b <branch>-v2
```

## Examples

```bash
# Example 1: Branch exists
git branch feature/login
# fatal: A branch named 'feature/login' already exists.
# Fix: git checkout feature/login

# Example 2: Delete and recreate
git branch -d feature/login
git branch feature/login

# Example 3: Case sensitivity
git branch Feature/Login
# fatal: A branch named 'Feature/Login' already exists.
# (if 'feature/login' was created on a case-insensitive filesystem)
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
