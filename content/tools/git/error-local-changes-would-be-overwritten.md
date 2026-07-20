---
title: "[Solution] Git error: Your local changes would be overwritten"
description: "Fix 'Your local changes would be overwritten' error. Resolve Git checkout, merge, or pull failures due to unstaged changes."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git error: Your local changes would be overwritten

error: Your local changes to the following files would be overwritten by checkout/merge/pull

This error occurs when Git operations would overwrite files that have uncommitted changes. Git protects your work by refusing to proceed.

## Common Causes

- Uncommitted changes in files that the merge/pull modifies
- Trying to checkout a branch that changes tracked files
- Stashing before switching branches
- Pulling changes that conflict with local modifications

## How to Fix

### Commit Your Changes

```bash
git add .
git commit -m "Save progress"
git pull
```

### Stash Your Changes

```bash
git stash
git pull
git stash pop
```

### Discard Local Changes (careful)

```bash
git checkout -- <file>
```

### Force Checkout (discard all local changes)

```bash
git checkout --force <branch>
```

## Examples

```bash
# Example 1: Pull with local changes
git pull origin main
# error: Your local changes to 'config.js' would be overwritten by merge.
# Fix: git stash && git pull && git stash pop

# Example 2: Switch branches with changes
git checkout feature/login
# error: Your local changes would be overwritten by checkout.
# Fix: git stash && git checkout feature/login

# Example 3: Discard and pull
git checkout -- config.js
git pull origin main
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
