---
title: "[Solution] Git log follow rename error"
description: "Fix 'git log --follow' error. Resolve issues when tracking file history across renames with Git log."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git log follow rename error

fatal: --follow requires exactly one path

This error occurs when you use `--follow` with multiple file paths. The `--follow` option only works with a single file path.

## Common Causes

- Passing multiple file paths to `git log --follow`
- Using a directory path instead of a single file
- Glob pattern expands to multiple files
- Misunderstanding of `--follow` limitations

## How to Fix

### Use Single File Path

```bash
git log --follow src/main.js
```

### Find Renames Manually

```bash
git log --name-only --diff-filter=R
```

### Search All History for Content

```bash
git log --all -S <search-term>
```

### Use Rename Detection

```bash
git log --find-renames -- <path>
```

## Examples

```bash
# Example 1: Multiple paths
git log --follow src/*.js
# fatal: --follow requires exactly one path
# Fix: git log --follow src/app.js

# Example 2: Track renames manually
git log --name-status --follow src/app.js
# R100 src/old.js src/app.js  (shows rename)

# Example 3: Search by content
git log --all -S "functionName" -- "*.js"
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
