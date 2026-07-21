---
title: "[Solution] Poetry Install Without Lock File -- Fix Missing poetry.lock"
description: "Fix Poetry install fails when poetry.lock is missing. Regenerate the lock file to resolve dependencies before installation."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry install` was run but no `poetry.lock` file exists in the project. Poetry needs the lock file to know which exact versions to install.

## Common Causes

- The project was freshly cloned and `poetry.lock` was not committed
- You deleted `poetry.lock` accidentally
- The `.gitignore` excludes `poetry.lock`
- You ran `poetry new` or `poetry init` without installing

## How to Fix

### 1. Generate the Lock File

```bash
poetry lock
```

### 2. Lock and Install Together

```bash
poetry install --lock
```

### 3. Verify poetry.lock is Committed

```bash
git status poetry.lock
# Add to version control
git add poetry.lock
```

### 4. Fix .gitignore

Ensure `poetry.lock` is NOT in your `.gitignore`:

```bash
grep -n "poetry.lock" .gitignore
```

## Examples

```bash
$ poetry install
pyproject.toml changed significantly since poetry.lock was last generated. Run `poetry lock [--no-update]` to fix it.

$ poetry lock
Resolving dependencies... (12.3s)

$ poetry install
Installing dependencies from lock file...
```
