---
title: "[Solution] Poetry Script Not Found -- Fix poetry run Script Missing"
description: "Fix Poetry script not found errors when poetry run cannot locate the specified script or command in the virtual environment. Check script registration."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry run` was invoked with a script name that does not exist in the current virtual environment. The entry point is not registered.

## Common Causes

- The package was not installed with `poetry install`
- The script is defined in a dependency, not your project
- The virtual environment is stale and missing scripts
- The script name is misspelled

## How to Fix

### 1. Reinstall to Register Scripts

```bash
poetry install
```

### 2. Check Available Scripts

```bash
ls $(poetry env info --path)/bin/
```

### 3. Use the Module Directly

```bash
poetry run python -m <module_name>
```

### 4. Verify pyproject.toml Scripts Section

```toml
[tool.poetry.scripts]
my-script = "myproject.cli:main"
```

## Examples

```bash
$ poetry run my-script
Command 'my-script' not found

$ poetry install
Installing myproject (1.0.0)

$ poetry run my-script
Hello from my-project!
```
