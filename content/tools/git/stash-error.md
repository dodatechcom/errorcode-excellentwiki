---
title: "[Solution] Git Stash Error"
description: "Fix Git stash errors when saving, applying, or popping stashed changes fails."
tools: ["git"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Git Stash Error

Git stash operations fail during save, apply, or pop.

```
error: cannot apply stash
The stash entry is kept
```

## Common Causes

- Stashed changes conflict with current work
- Stash is empty
- Stash entry was dropped
- Merge conflict during stash pop
- Stash created in wrong directory

## How to Fix

### Save Stash

```bash
# Save current changes
git stash

# Save with message
git stash push -m "Work in progress"

# Include untracked files
git stash -u

# Include ignored files
git stash -a
```

### Apply or Pop Stash

```bash
# Apply stash without removing
git stash apply

# Pop stash (apply and remove)
git stash pop

# Apply specific stash
git stash apply stash@{2}
```

### Handle Stash Conflicts

```bash
# When pop creates conflicts
git stash pop
# If conflict occurs:
# Resolve conflicts
git add .
git stash drop  # Remove the stash manually
```

### List and Manage Stashes

```bash
# List all stashes
git stash list

# Show stash content
git stash show -p stash@{0}

# Drop specific stash
git stash drop stash@{2}

# Clear all stashes
git stash clear
```

### Create Branch from Stash

```bash
# Create branch from stash
git stash branch new-branch stash@{0}
```

## Examples

```bash
# Save specific files only
git stash push -m "Config changes" -- config/

# Restore specific file from stash
git checkout stash@{0} -- path/to/file

# Show all stash contents
git stash list --stat
```
