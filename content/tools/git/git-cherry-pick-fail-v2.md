---
title: "[Solution] Git Cherry-pick Conflict"
description: "Fix Git cherry-pick merge conflict. Resolve conflicts when cherry-picking commits between branches."
tools: ["git"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A cherry-pick conflict occurs when Git cannot cleanly apply a specific commit from one branch to another. The changes in the commit overlap with existing changes on the target branch, creating a merge conflict.

## Common Causes

- The commit being cherry-picked conflicts with current branch state
- The commit touches files that were modified differently on the target branch
- Cherry-picking a merge commit without specifying a parent
- The commit was already partially applied
- Cherry-picking onto a branch with unrelated history

## How to Fix

### Abort the Cherry-pick

```bash
git cherry-pick --abort
```

### Resolve the Conflict

```bash
# Edit the conflicted file, remove conflict markers
git add <resolved-file>
git cherry-pick --continue
```

### Cherry-pick Without Committing

```bash
git cherry-pick --no-commit abc1234
# Review changes, then commit manually
git commit -m "Cherry-pick with adjustments"
```

### Cherry-pick Multiple Commits

```bash
git cherry-pick abc1234..def5678
```

## Examples

```bash
# Example 1: Cherry-pick a single commit
git cherry-pick abc1234
# CONFLICT (content): Merge conflict in src/api.js

# Resolve conflict
git add src/api.js
git cherry-pick --continue

# Example 2: Cherry-pick a merge commit
git cherry-pick -m 1 abc1234
# -m 1 specifies the first parent as the mainline

# Example 3: Cherry-pick and resolve
git cherry-pick abc1234
# CONFLICT in config.yml

git checkout --theirs config.yml
git add config.yml
git cherry-pick --continue
```

## Related Errors

- [Git Merge Conflict]({{< relref "/tools/git/git-merge-conflict-v2" >}}) — merge conflict in file
- [Git Rebase Abort]({{< relref "/tools/git/git-rebase-abort-v2" >}}) — rebase conflict handling
- [Git Push Error]({{< relref "/tools/git/git-push-error-v2" >}}) — push rejected
