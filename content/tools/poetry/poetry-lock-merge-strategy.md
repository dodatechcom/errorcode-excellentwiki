---
title: "[Solution] Poetry Lock Merge Strategy -- Fix Git Merge Strategy for Lock"
description: "Fix Poetry lock merge strategy errors when Git auto-merges poetry.lock incorrectly. Configure merge drivers for lock files."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Git's auto-merge of `poetry.lock` produced an invalid file. Poetry cannot parse the merge result.

## Common Causes

- Git auto-merged conflicting `poetry.lock` entries
- No custom merge driver is configured for `.lock` files
- The merge was not tested after resolution

## How to Fix

### 1. Accept One Side and Regenerate

```bash
git checkout --ours poetry.lock
poetry lock
```

### 2. Configure a Custom Merge Driver

```gitattributes
# .gitattributes
poetry.lock merge=binary
```

### 3. Use Poetry's Merge

```bash
# After merging, always regenerate:
poetry lock
git add poetry.lock
```

### 4. Prevent Lock File Conflicts

Use long-lived branches or feature flags instead of concurrent lock edits.

## Examples

```bash
$ git merge feature-branch
Auto-merging poetry.lock
CONFLICT (content): Merge conflict in poetry.lock

$ git checkout --ours poetry.lock
$ poetry lock
$ git add poetry.lock
$ git commit -m "Merge feature-branch, regenerated lock"
```
