---
title: "[Solution] Git branch delete error"
description: "Fix 'git branch -d' error. Resolve failures when trying to delete a Git branch that has unmerged changes."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git branch delete error

error: The branch '<branch>' is not fully merged.

This error occurs when you try to delete a branch that has commits not merged into the current branch or its upstream.

## Common Causes

- Branch has unmerged commits
- Wrong branch name specified
- Current branch is the one you're trying to delete
- Merged to a different branch but not current

## How to Fix

### Force Delete Branch

```bash
git branch -D <branch>
```

### Merge Before Deleting

```bash
git merge <branch>
git branch -d <branch>
```

### Check Merge Status

```bash
git branch --merged
git branch --no-merged
```

### Delete Remote Branch

```bash
git push origin --delete <branch>
```

## Examples

```bash
# Example 1: Unmerged branch
git branch -d feature/old
# error: The branch 'feature/old' is not fully merged.
# Fix: git branch -D feature/old

# Example 2: Delete after merge
git checkout main
git merge feature/done
git branch -d feature/done

# Example 3: Check which branches are safe to delete
git branch --merged
# Shows branches that can be deleted with -d
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
