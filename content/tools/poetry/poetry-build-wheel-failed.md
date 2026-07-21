---
title: "[Solution] Poetry Build Wheel Failed -- Fix Wheel Compilation Error"
description: "Fix Poetry build wheel failed errors when the wheel build process encounters compilation or packaging errors. Install build tools and dependencies."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry failed to build a wheel for your package during `poetry build`. The build process stopped with an error.

## Common Causes

- C extension cannot compile without system libraries
- `pyproject.toml` has invalid metadata
- Package includes files not compatible with wheel format
- Build scripts have errors

## How to Fix

### 1. Install System Build Dependencies

```bash
sudo apt install build-essential python3-dev libssl-dev libffi-dev
```

### 2. Build with Verbose Output

```bash
poetry build -vvv 2>&1 | tail -50
```

### 3. Check for setup.py Errors

```bash
python setup.py check
```

### 4. Fix Metadata in pyproject.toml

```toml
[tool.poetry]
name = "myproject"
version = "1.0.0"
description = "A valid description"
authors = ["Author <email@example.com>"]
```

## Examples

```bash
$ poetry build
error: command 'gcc' failed: No such file or directory

$ sudo apt install build-essential
$ poetry build
Building myproject (1.0.0)
  - Building sdist
  - Building wheel
```
