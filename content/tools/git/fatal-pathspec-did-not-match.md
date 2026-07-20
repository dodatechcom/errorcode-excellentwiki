---
title: "[Solution] Git fatal: Pathspec did not match any files"
description: "Fix 'pathspec did not match any files' error. Resolve Git command failures when a specified file path does not exist in the repository."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Pathspec did not match any files

fatal: pathspec '<file>' did not match any files

This error occurs when you reference a file path in a Git command that does not exist in the working tree or index. Git cannot find the specified path in the current repository state.

## Common Causes

- Typo in the file name or path
- File was deleted or never committed
- File exists but in a different directory
- File is untracked and not staged
- Case sensitivity mismatch on Linux

## How to Fix

### List Files in Directory

```bash
ls -la
git ls-files
```

### Check if File is Tracked

```bash
git ls-files <file>
```

### Use Tab Completion

```bash
git add <tab><tab>
```

### Check for Whitespace or Special Characters

```bash
git status --short
```

## Examples

```bash
# Example 1: Typo in filename
git add src/myflie.js
# fatal: pathspec 'src/myflie.js' did not match any files
# Fix: git add src/myfile.js

# Example 2: File not committed yet
git checkout -- index.html
# fatal: pathspec 'index.html' did not match any files
# Fix: git add index.html first, or verify the file exists

# Example 3: Case sensitivity (Linux vs macOS)
git add Src/App.js
# fatal: pathspec 'Src/App.js' did not match any files
# Fix: git add src/App.js
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
