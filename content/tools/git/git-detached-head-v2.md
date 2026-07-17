---
title: "[Solution] Git Detached HEAD After Checkout"
description: "Fix Git detached HEAD state. Restore or create a branch when HEAD is not attached to any branch."
tools: ["git"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["detached-head", "checkout", "branch", "HEAD", "git"]
weight: 5
---

## What This Error Means

A detached HEAD state means your working directory is checked out to a specific commit rather than a branch tip. Any new commits you make will not belong to any branch and can be lost when you check out a different branch or tag.

## Common Causes

- Checked out a specific commit hash directly (`git checkout abc1234`)
- Checked out a tag (`git checkout v1.0.0`)
- Ran `git checkout` from a CI/CD pipeline referencing a SHA
- Cloned with `--depth` and detached from the shallow history
- Rebased onto a commit that was then overwritten

## How to Fix

### Check Current State

```bash
git status
# HEAD detached at abc1234
```

### Create a Branch from Detached HEAD

```bash
git switch -c my-new-branch
```

### Go Back to the Original Branch

```bash
git switch main
```

### Save Detached Work Before Switching

```bash
git switch -c temp-branch
# OR
git stash
git switch main
git stash pop
```

### Recover Lost Commits

```bash
git reflog
# Find the commit hash you were on
git switch -c recovered-branch abc1234
```

## Examples

```bash
# Example 1: Detached by checking out a tag
git checkout v2.1.0
# You are in 'detached HEAD' state...

# Fix: create a branch
git switch -c hotfix-branch

# Example 2: Detached after checking out a commit
git checkout a1b2c3d
# HEAD detached at a1b2c3d

# Make changes and commit
git add .
git commit -m "Fix bug"
# Commit is orphaned!

# Fix: attach to a branch
git switch -c bugfix

# Example 3: Return to a branch
git switch main
```

## Related Errors

- [Git Merge Conflict]({{< relref "/tools/git/git-merge-conflict-v2" >}}) — merge conflict in file
- [Git Rebase Abort]({{< relref "/tools/git/git-rebase-abort-v2" >}}) — rebase conflict handling
- [Git Branch Error]({{< relref "/tools/git/git-branch-error" >}}) — branch operation error
