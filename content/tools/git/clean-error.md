---
title: "[Solution] Git Clean Error"
description: "Fix Git clean errors when removing untracked files or directories fails."
tools: ["git"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Git Clean Error

Git clean fails to remove untracked files or directories.

```
fatal: failed to clean the working tree
```

## Common Causes

- Files have write protection
- Directory not empty with nested files
- dry-run mode showing what would happen
- Files ignored by .gitignore not being cleaned
- Permission denied on some files

## How to Fix

### Dry Run First

```bash
# See what would be removed
git clean -n

# With force and including ignored files
git clean -ndx
```

### Force Remove Untracked Files

```bash
# Remove untracked files
git clean -f

# Remove untracked files and directories
git clean -fd

# Remove ignored files too
git clean -fdx

# Remove ignored and non-ignored
git clean -fdX  # Only ignored
git clean -fdx  # Everything
```

### Remove Specific Patterns

```bash
# Remove only .o files
git clean -f -e '*.o'

# Remove only build directories
git clean -f -e 'build/' -e 'dist/'
```

### Handle Permission Issues

```bash
# Force with permission changes
git clean -f -d

# Or fix permissions first
chmod -R u+w .
git clean -fd
```

## Examples

```bash
# Safe clean workflow
git status --short
git clean -n  # Preview
git clean -fd  # Execute

# Clean only specific file types
git clean -f -e '*.pyc' -e '__pycache__/' -e 'node_modules/'
```
