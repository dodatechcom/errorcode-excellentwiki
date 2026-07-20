---
title: "[Solution] Git fatal: Cannot update paths and switch to branch"
description: "Fix 'Cannot update paths and switch to branch' error. Resolve Git checkout failures when paths and branch switching are mixed."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Cannot update paths and switch to branch

fatal: Cannot update paths and switch to branch 'branch' at the same time.

This error occurs when you mix file paths with a branch name in `git checkout`. You need to separate path updates from branch switching.

## Common Causes

- Running `git checkout <branch> <file>` when you meant to switch branches
- Confusing `git checkout` syntax between branch switching and file restoration
- Path argument matches a branch name
- Incorrect command structure

## How to Fix

### Switch to Branch Only

```bash
git checkout <branch>
```

### Restore File Only

```bash
git checkout -- <file>
```

### Use Modern Commands

```bash
git switch <branch>        # switch branch
git restore <file>         # restore file
```

### Use Double Dash to Disambiguate

```bash
git checkout <branch> --
```

## Examples

```bash
# Example 1: Mixed arguments
git checkout main src/index.js
# fatal: Cannot update paths and switch to branch 'main' at the same time.
# Fix: git checkout main && git checkout -- src/index.js

# Example 2: Using modern commands
git switch main
git restore src/index.js

# Example 3: File named same as branch
git checkout login
# fatal: Cannot update paths and switch to branch 'login'
# Fix: git checkout login --
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
