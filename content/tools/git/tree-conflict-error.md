---
title: "[Solution] Git Tree Conflict Error"
description: "Fix Git tree conflicts when file type changes cause merge or rebase conflicts."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Tree Conflict Error

Git encounters tree-level conflicts where file type or directory structure conflicts.

```
CONFLICT (modify/delete): file.txt deleted in HEAD and modified in branch
```

## Common Causes

- File deleted in one branch and modified in another
- File replaced with directory or vice versa
- Symlink conflicts
- File mode changes conflicting
- Binary file conflicts

## How to Fix

### View Tree Conflicts

```bash
# See all conflicts
git status

# Show tree conflicts specifically
git diff --name-status --diff-filter=U
```

### Resolve Delete/Modify Conflicts

```bash
# Keep the file
git add file.txt

# Remove the file
git rm file.txt

# After resolution
git commit
```

### Resolve File/Directory Conflicts

```bash
# If file became directory
git rm conflicting-file
git add new-directory/
git commit
```

### Use Merge Strategy

```bash
# Prefer current branch changes
git merge -X ours branch

# Prefer incoming changes
git merge -X theirs branch
```

### Reset Conflicted Files

```bash
# Reset specific file to HEAD
git checkout --theirs conflicting-file
git add conflicting-file

# Or keep ours
git checkout --ours conflicting-file
git add conflicting-file
```

## Examples

```bash
# Resolve delete/modify
git status  # Shows file deleted in HEAD, modified in branch
git rm file.txt  # or git add file.txt to keep
git commit -m "Resolve tree conflict"

# Check for remaining conflicts
git diff --check
```
