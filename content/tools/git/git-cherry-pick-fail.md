---
title: "[Solution] Git Cherry-Pick Failed — could not apply X"
description: "Fix Git cherry-pick failures. Resolve conflicts when cherry-picking commits between branches."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["cherry-pick", "conflict", "apply", "git"]
weight: 5
---

A cherry-pick fails when Git cannot cleanly apply a commit from one branch to another. This typically happens when the same file has been modified in both branches.

## Common Causes

- The commit being cherry-picked conflicts with changes in the current branch
- The file was modified in both the source and target branches
- The commit depends on earlier commits that are not in the target branch
- A file was deleted in the target branch but modified in the source commit

## How to Fix

### Check Cherry-Pick Status

```bash
git status
# interactive rebase in progress; onto <commit>
```

### Resolve Conflicts and Continue

```bash
# edit conflicted files, remove conflict markers
git add <resolved-file>
git cherry-pick --continue
```

### Skip the Cherry-Pick

```bash
git cherry-pick --skip
```

### Abort the Cherry-Pick

```bash
git cherry-pick --abort
```

### Cherry-Pick Multiple Commits

```bash
git cherry-pick <commit1>..<commit2>
```

## Examples

```bash
# Example 1: Cherry-pick a bugfix commit
git cherry-pick abc1234
# CONFLICT (content): Merge conflict in src/api.js

# Resolve and continue
git add src/api.js
git cherry-pick --continue

# Example 2: Cherry-pick a range of commits
git cherry-pick abc1234..def5678
```

## Related Errors

- [Git Merge Conflict]({{< relref "/tools/git/git-merge-conflict" >}}) — merge conflict resolution
- [Git Rebase Abort]({{< relref "/tools/git/git-rebase-abort" >}}) — rebase conflict handling
