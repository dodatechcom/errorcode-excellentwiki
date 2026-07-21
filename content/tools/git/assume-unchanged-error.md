---
title: "[Solution] Git Assume Unchanged Error"
description: "Fix Git assume-unchanged errors when git update-index --assume-unchanged fails or misbehaves."
tools: ["git"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Git Assume Unchanged Error

Git assume-unchanged flag causes confusion when tracking changes on files.

```
fatal: Unable to mark file
```

## Common Causes

- File not in the index yet
- Insufficient permissions
- Assume-unset used on file that was never tracked
- Trying to use on submodule
- Stale index after manual changes

## How to Fix

### Check Assume-Unchanged Files

```bash
# List files with assume-unchanged
git ls-files -v | grep ^h

# First character 'h' means assume-unchanged
```

### Remove Assume-Unchanged Flag

```bash
# Remove assume-unchanged for a file
git update-index --no-assume-unchanged path/to/file

# Remove for all assume-unchanged files
git ls-files -v | grep '^h' | awk '{print $2}' | while read f; do
    git update-index --no-assume-unchanged "$f"
done
```

### Set Assume-Unchanged

```bash
# Mark a file as assume-unchanged
git update-index --assume-unchanged path/to/file
```

### Difference from Skip-Worktree

```bash
# Assume-unchanged: local changes not shown in git status
# Skip-worktree: prefer local version, more persistent
git update-index --skip-worktree path/to/file

# List skip-worktree files
git ls-files -v | grep ^S
```

## Examples

```bash
# Common use case: ignore local config files
git update-index --assume-unchanged config/database.yml
git update-index --assume-unchanged config/secrets.yml

# Restore tracking
git update-index --no-assume-unchanged config/database.yml
git update-index --no-assume-unchanged config/secrets.yml

# Bulk restore
git ls-files -v | grep '^h' | cut -c3- | while read -r f; do
    git update-index --no-assume-unchanged "$f"
done
```
