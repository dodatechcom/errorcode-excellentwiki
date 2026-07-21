---
title: "[Solution] Poetry Lock Merge Conflict -- Fix Git Merge in poetry.lock"
description: "Fix Poetry lock merge conflict errors when poetry.lock has Git merge conflict markers. Regenerate the lock file after resolving conflicts."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry.lock` contains Git merge conflict markers. Poetry cannot parse the corrupted lock file.

## Common Causes

- Two branches modified `poetry.lock` and Git auto-merge failed
- `poetry.lock` was merged manually without resolving conflicts
- The merge was not tested after resolution

## How to Fix

### 1. Accept One Side and Regenerate

```bash
git checkout --theirs poetry.lock
poetry lock
```

### 2. Or Resolve Manually

```bash
# Edit poetry.lock to remove conflict markers
vim poetry.lock
poetry check
```

### 3. Regenerate from Scratch

```bash
git checkout main -- poetry.lock
poetry lock
```

### 4. Prevent Future Conflicts

```bash
# .gitattributes
poetry.lock merge=ours
```

## Examples

```bash
$ poetry install
Invalid TOML document: ...<<<<<<< HEAD ...

$ git checkout --theirs poetry.lock
$ poetry lock
Resolving dependencies... (8.5s)

$ poetry install
Installing dependencies from lock file...
```
