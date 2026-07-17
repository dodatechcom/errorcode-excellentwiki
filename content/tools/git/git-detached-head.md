---
title: "[Solution] Git Detached HEAD — HEAD detached at commit X"
description: "Fix Git detached HEAD state. Understand and recover from HEAD detached at commit."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A detached HEAD means you have checked out a specific commit rather than a branch. Any new commits made in this state will not belong to any branch and can be lost.

## Common Causes

- Checking out a specific commit hash (`git checkout <commit>`)
- Checking out a remote branch without creating a local tracking branch
- Checking out a tag (`git checkout v1.0.0`)
- Using `git checkout origin/main` instead of `git checkout main`

## How to Fix

### Check Current State

```bash
git status
# HEAD detached at <commit-hash>
```

### Create a Branch from Current Position

```bash
git checkout -b new-branch-name
```

### Return to Original Branch

```bash
git checkout main
```

### Rescue Commits Made While Detached

```bash
git branch rescue-branch <commit-hash>
git checkout main
git merge rescue-branch
```

## Examples

```bash
# Example 1: Detached HEAD from tag checkout
git checkout v2.0.0
# HEAD detached at v2.0.0
# Fix: create branch from this point
git checkout -b fix-v2.0.0

# Example 2: Detached HEAD from commit checkout
git checkout abc1234
# HEAD detached at abc1234
# Fix: attach to a new branch
git switch -c hotfix-branch
```

## Related Errors

- [Git Merge Conflict]({{< relref "/tools/git/git-merge-conflict" >}}) — conflict when merging branches
- [Git Cherry-Pick Fail]({{< relref "/tools/git/git-cherry-pick-fail" >}}) — cherry-pick failed
