---
title: "[Solution] Git update-index error"
description: "Fix 'git update-index' error. Resolve issues when manually updating the Git index for file permissions, assume-unchanged, or skip-worktree."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git update-index error

fatal: Unable to mark file <file>

This error occurs when `git update-index` fails to update the index entry for a specified file.

## Common Causes

- File does not exist in the index
- File is not tracked by Git
- Permission denied when writing to index
- File path is invalid
- Index is locked by another process

## How to Fix

### Check File in Index

```bash
git ls-files <file>
```

### Mark File as Assume-unchanged

```bash
git update-index --assume-unchanged <file>
```

### Remove Assume-unchanged Flag

```bash
git update-index --no-assume-unchanged <file>
```

### List Files with Flags

```bash
git ls-files -v | grep ^[a-z]
```

## Examples

```bash
# Example 1: File not in index
git update-index --assume-unchanged untracked.js
# fatal: Unable to mark file untracked.js
# Fix: git add untracked.js first

# Example 2: Mark config file unchanged
git update-index --assume-unchanged config/local.js
git status  # ignores changes to this file

# Example 3: Remove assume-unchanged
git update-index --no-assume-unchanged config/local.js
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
