---
title: "[Solution] Poetry Lock Out of Date -- Fix Stale Lock File"
description: "Fix Poetry lock out of date errors when poetry.lock does not match pyproject.toml. Regenerate the lock file to sync dependencies."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry.lock` is inconsistent with the current `pyproject.toml`. Dependencies were changed without regenerating the lock.

## Common Causes

- `pyproject.toml` was edited without running `poetry lock`
- A merge left conflicting dependency versions
- A CI pipeline edits `pyproject.toml` dynamically

## How to Fix

### 1. Regenerate the Lock File

```bash
poetry lock
```

### 2. Lock Without Updating

```bash
poetry lock --no-update
```

### 3. Update Everything

```bash
poetry update
```

### 4. Check for Differences

```bash
poetry check
```

## Examples

```bash
$ poetry install
pyproject.toml changed significantly since poetry.lock was last generated.
Run `poetry lock [--no-update]` to fix it.

$ poetry lock
Resolving dependencies... (6.3s)

$ poetry install
Installing dependencies from lock file...
```
