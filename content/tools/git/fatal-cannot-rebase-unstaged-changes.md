---
title: "[Solution] Git fatal: Cannot rebase with unstaged changes"
description: "Fix 'cannot rebase: You have unstaged changes' error. Resolve Git rebase failures when working directory is not clean."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Cannot rebase with unstaged changes

Cannot rebase: You have unstaged changes.

This error occurs when you try to rebase with uncommitted or unstaged changes in your working directory. Git requires a clean working tree for rebasing.

## Common Causes

- Uncommitted file modifications
- Untracked files present
- Staged but uncommitted changes
- In-progress work not yet saved

## How to Fix

### Commit Your Changes

```bash
git add .
git commit -m "WIP: save progress before rebase"
git rebase <branch>
```

### Stash Your Changes

```bash
git stash
git rebase <branch>
git stash pop
```

### Discard Changes (careful)

```bash
git reset --hard HEAD
git rebase <branch>
```

## Examples

```bash
# Example 1: Stash and rebase
git stash
git rebase main
git stash pop

# Example 2: Commit and rebase
git add -A
git commit -m "Save before rebase"
git rebase main

# Example 3: Interactive rebase with changes
git stash
git rebase -i HEAD~3
git stash pop
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
