---
title: "[Solution] Git error: Untracked working tree file would be overwritten"
description: "Fix 'Untracked working tree file would be overwritten' error. Resolve Git checkout and merge failures from untracked file conflicts."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git error: Untracked working tree file would be overwritten

error: Untracked working tree file '<file>' would be overwritten by merge/checkout.

This error occurs when an untracked file in your working directory has the same path as a file that a Git operation (checkout or merge) needs to create.

## Common Causes

- Untracked file exists at the same path as a tracked file in the target branch
- Generated or build artifacts not in .gitignore
- Temporary files left in the working tree
- IDE or editor files not properly ignored

## How to Fix

### Remove the Untracked File

```bash
rm <file>
```

### Move the File to a Safe Location

```bash
mv <file> <file>.bak
```

### Check What Will Be Overwritten

```bash
git checkout --overlay <branch>
```

### Stash Untracked Files

```bash
git stash --include-untracked
git checkout <branch>
```

## Examples

```bash
# Example 1: Untracked file blocking checkout
git checkout feature/login
# error: Untracked working tree file 'config.js' would be overwritten
# Fix: mv config.js config.js.bak && git checkout feature/login

# Example 2: Merge with untracked files
git merge feature/login
# error: Untracked working tree file 'dist/bundle.js' would be overwritten
# Fix: rm dist/bundle.js && git merge feature/login

# Example 3: Stash untracked files
git stash --include-untracked
git pull origin main
git stash pop
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
