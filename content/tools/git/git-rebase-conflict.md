---
title: "[Solution] Git rebase conflict error"
description: "Fix Git rebase conflict error. Resolve merge conflicts that occur during a rebase operation."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git rebase conflict error

CONFLICT (content): Merge conflict in <file>
error: could not apply <hash> <commit-message>

This error occurs when Git encounters conflicts while applying commits during a rebase. The rebase pauses to let you resolve the conflicts.

## Common Causes

- Changes in the rebased branch conflict with the target branch
- Multiple commits in the branch each have different conflicts
- Same file modified in both branches
- Renamed file in one branch modified in the other

## How to Fix

### Resolve Conflicts

```bash
git status
# Edit conflicted files
git add <resolved-file>
git rebase --continue
```

### Skip Problematic Commit

```bash
git rebase --skip
```

### Abort the Rebase

```bash
git rebase --abort
```

### Use Git Mergetool

```bash
git mergetool
git rebase --continue
```

## Examples

```bash
# Example 1: Resolve and continue
git rebase main
# CONFLICT in src/app.js
# Fix: edit src/app.js, git add src/app.js, git rebase --continue

# Example 2: Skip commit
git rebase --skip

# Example 3: Abort rebase
git rebase --abort
# Back to pre-rebase state
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
