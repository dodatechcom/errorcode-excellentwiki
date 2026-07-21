---
title: "[Solution] Poetry Export Dev Dependencies -- Fix Missing Dev Deps in Export"
description: "Fix poetry export dev dependencies missing when dev dependencies are excluded from requirements.txt output. Include dev group in export."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry export` produced a requirements.txt that is missing development dependencies. The export only included production deps.

## Common Causes

- The --without dev flag was used (intentionally or by default)
- Dev dependencies are in an optional group
- The --only flag restricted the export

## How to Fix

### 1. Include Dev Dependencies

```bash
poetry export -f requirements.txt --with dev -o requirements.txt
```

### 2. Include All Groups

```bash
poetry export -f requirements.txt --with dev,test -o requirements.txt
```

### 3. Check Which Groups Exist

```bash
grep '\[tool.poetry.group' pyproject.toml
```

### 4. Export All Dependencies

```bash
poetry export -f requirements.txt --all-extras -o requirements.txt
```

## Examples

```bash
$ poetry export -f requirements.txt -o requirements.txt
$ cat requirements.txt
requests==2.31.0

# Missing dev deps -- include them:
$ poetry export -f requirements.txt --with dev -o requirements.txt
$ cat requirements.txt
requests==2.31.0
pytest==7.4.3
mypy==1.7.1
```
