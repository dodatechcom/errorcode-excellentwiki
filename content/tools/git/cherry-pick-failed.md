---
title: "[Solution] Git Cherry-Pick Failed — could not apply X"
description: "Fix Git cherry-pick failed error. Resolve conflicts or issues when cherry-picking commits."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git Cherry-Pick Failed — could not apply X

Cherry-pick fails when Git cannot cleanly apply a commit to the current branch. This usually happens due to conflicts with the existing code or when the commit has already been applied.

## Common Causes

- Conflicts between the cherry-picked commit and current branch
- The commit was already applied (duplicate)
- The commit depends on other commits not present in the current branch
- The commit modifies files that have been significantly changed

## How to Fix

### Check the Conflict

```bash
git status
```

### Resolve Conflicts Manually

Edit the conflicted files, remove conflict markers, and save.

### Mark as Resolved and Continue

```bash
git add <resolved-file>
git cherry-pick --continue
```

### Abort the Cherry-Pick

```bash
git cherry-pick --abort
```

### Cherry-Pick a Range of Commits

```bash
git cherry-pick <start-commit>..<end-commit>
```

## Examples

```bash
# Example 1: Cherry-pick a single commit
git cherry-pick abc1234
# CONFLICT (content): Merge conflict in src/utils.js

# Example 2: Resolve and continue
# Edit src/utils.js, remove conflict markers
git add src/utils.js
git cherry-pick --continue

# Example 3: Cherry-pick multiple commits
git cherry-pick abc1234..def5678
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — conflict when merging branches
- [Rebase Abort]({{< relref "/tools/git/rebase-abort" >}}) — rebase operation interrupted
