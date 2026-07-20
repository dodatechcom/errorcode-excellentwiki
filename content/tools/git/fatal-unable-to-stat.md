---
title: "[Solution] Git fatal: Unable to stat file"
description: "Fix 'Unable to stat' error. Resolve Git failures when it cannot read file attributes from the filesystem."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Unable to stat file

fatal: Unable to stat '<path>': No such file or directory

This error occurs when Git tries to read file metadata but the file does not exist or the path is invalid.

## Common Causes

- File was deleted after being staged
- Symlink target does not exist
- File path contains special characters
- Network filesystem disconnected
- File moved while Git was processing

## How to Fix

### Reset the File in Index

```bash
git reset HEAD <file>
```

### Remove and Re-add

```bash
git rm --cached <file>
git add <file>
```

### Check File Existence

```bash
ls -la <file>
```

### Clean Working Tree

```bash
git clean -fd
git checkout -- .
```

## Examples

```bash
# Example 1: Deleted staged file
rm src/temp.js
git status
# Changes not staged for delete: src/temp.js
# Fix: git checkout -- src/temp.js or git rm src/temp.js

# Example 2: Broken symlink
ls -la link-to-config
# lrwxrwxrwx  link-to-config -> /nonexistent/path
# Fix: remove symlink git rm link-to-config

# Example 3: Reset and re-add
git reset HEAD src/generated.js
rm src/generated.js
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
