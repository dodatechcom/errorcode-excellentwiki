---
title: "[Solution] Git Detached HEAD — You are in 'detached HEAD' state"
description: "Fix Git detached HEAD state. Learn what detached HEAD means, how to fix it, and how to preserve your work."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git Detached HEAD — You are in 'detached HEAD' state

A detached HEAD means you have checked out a specific commit rather than a branch. Any new commits you make in this state will not belong to any branch and will be lost once you checkout a different branch unless you save them first.

## Common Causes

- Checking out a specific commit hash directly (`git checkout abc123`)
- Checking out a remote branch without creating a local branch (`git checkout origin/main`)
- Checking out a tag (`git checkout v1.0`)
- Using `git checkout` with a SHA reference

## How to Fix

### Create a Branch from Detached HEAD

```bash
git checkout -b new-branch-name
```

### Preserve Work Before Switching

```bash
git stash
git checkout main
git stash pop
```

### Return to a Branch

```bash
git checkout main
```

### Check Current Status

```bash
git status
git branch
```

## Examples

```bash
# Example 1: Accidentally detached HEAD
git checkout abc1234
# HEAD detached at abc1234
# Fix: create a branch to save work
git checkout -b my-fix

# Example 2: Checking out a remote branch
git checkout origin/feature-x
# HEAD detached at def5678
# Fix: create local tracking branch
git checkout -b feature-x origin/feature-x
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — conflicts when merging branches back
- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crashloopbackoff" >}}) — deployment issues after pushing broken commits
