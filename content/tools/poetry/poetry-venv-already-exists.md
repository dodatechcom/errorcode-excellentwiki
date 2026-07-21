---
title: "[Solution] Poetry Virtualenv Already Exists -- Fix Overlapping Environments"
description: "Fix Poetry virtualenv already exists errors when Poetry finds an existing venv at the target path. Remove or recreate the virtual environment."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry tried to create a virtual environment but a directory already exists at the expected location. Poetry refuses to overwrite an existing venv.

## Common Causes

- A previous `poetry install` was interrupted mid-creation
- You manually created a `.venv` directory in the project
- Another tool created a virtualenv at the same path
- A stale `.venv` from a deleted environment

## How to Fix

### 1. Remove the Existing Virtualenv

```bash
poetry env remove python
```

### 2. Remove by Path

```bash
poetry env info --path
rm -rf $(poetry env info --path)
poetry install
```

### 3. Force Recreate

```bash
poetry env remove --all
poetry install
```

### 4. Use an In-Project Venv

```bash
poetry config virtualenvs.in-project true
poetry install
```

## Examples

```bash
$ poetry install
Virtualenv already exists at: /home/user/.cache/pypoetry/virtualenvs/myproject-abc123

$ poetry env remove python
Deleted virtualenv: /home/user/.cache/pypoetry/virtualenvs/myproject-abc123

$ poetry install
Installing dependencies from lock file...
```
