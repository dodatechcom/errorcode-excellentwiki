---
title: "[Solution] Poetry Group Not Defined -- Fix Missing Dependency Group"
description: "Fix Poetry group not defined errors when installing or updating a dependency group that does not exist in pyproject.toml. Define the group correctly."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means you referenced a dependency group in `poetry install --with` or `poetry update --with` that is not defined in `pyproject.toml`.

## Common Causes

- Typo in the group name
- The group was removed from `pyproject.toml` but commands still reference it
- The group definition has a syntax error
- You forgot to add `[tool.poetry.group.<name>.dependencies]`

## How to Fix

### 1. Check Existing Groups

```bash
poetry show --with dev,test
```

### 2. Define the Group in pyproject.toml

```toml
[tool.poetry.group.test]
optional = true

[tool.poetry.group.test.dependencies]
pytest = "^7.0"
```

### 3. Verify the Group Name

```bash
grep -A5 '\[tool.poetry.group' pyproject.toml
```

### 4. Install Without the Missing Group

```bash
poetry install --without nonexistent-group
```

## Examples

```bash
$ poetry install --with test
ValueError: Group "test" is not defined in pyproject.toml

# Add to pyproject.toml:
[tool.poetry.group.test]
optional = true

[tool.poetry.group.test.dependencies]
pytest = "^7.0"

$ poetry install --with test
Installing dependencies from lock file...
```
