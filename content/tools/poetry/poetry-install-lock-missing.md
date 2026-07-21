---
title: "[Solution] Poetry Install Lock Missing -- Fix poetry.lock Not Found"
description: "Fix poetry install lock missing error when poetry.lock file is absent. Generate the lock file before installing."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry install` cannot find `poetry.lock` in the project directory. Without the lock file, Poetry cannot determine exact versions.

## Common Causes

- `poetry.lock` was deleted or never generated
- `.gitignore` excludes `poetry.lock`
- You are in the wrong directory
- The project was freshly cloned without the lock file

## How to Fix

### 1. Generate the Lock File

```bash
poetry lock
```

### 2. Lock and Install

```bash
poetry install --lock
```

### 3. Check .gitignore

```bash
grep "poetry.lock" .gitignore
# Remove poetry.lock from .gitignore if present
```

### 4. Verify Project Root

```bash
ls pyproject.toml poetry.lock
```

## Examples

```bash
$ poetry install
pyproject.toml changed significantly since poetry.lock was last generated.

$ poetry lock
Resolving dependencies... (8.2s)

$ poetry install
Installing dependencies from lock file...
```
