---
title: "[Solution] Git Follow Rename Error"
description: "Fix Git log --follow errors when tracking file history through renames fails."
tools: ["git"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Git Follow Rename Error

Git log --follow cannot track file history across renames.

```
fatal: --follow is incompatible with --all
```

## Common Causes

- Using --follow with --all flag
- File was not renamed but replaced
- Diff.renameLimit too low
- File history exceeds rename detection
- Using --follow with pathspec

## How to Fix

### Correct Usage of --follow

```bash
# Wrong - --follow incompatible with --all
git log --follow --all -- file.txt

# Correct - use without --all
git log --follow -- file.txt
```

### Increase Rename Limit

```bash
# Increase diff rename limit
git config diff.renameLimit 10000

# Or use no limit
git config diff.renames true
```

### Track History Through Renames

```bash
# Follow file through renames
git log --follow --diff-filter=R --summary -- file.txt

# Show rename commits
git log --follow --name-status -- file.txt
```

### Use pickaxe for Content Changes

```bash
# Find commits that changed specific string
git log -S "function_name" --follow -- file.txt

# Regex search
git log -G "pattern.*here" -- file.txt
```

## Examples

```bash
# Full history with renames
git log --follow --diff-filter=ADRC --summary -- src/main.py

# See what happened to a file
git log --follow --name-status --pretty=format:"%h %s" -- file.txt
```
