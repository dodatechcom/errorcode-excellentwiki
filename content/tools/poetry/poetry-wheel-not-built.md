---
title: "[Solution] Poetry Wheel Not Built -- Fix Wheel Build Failure"
description: "Fix Poetry wheel not built errors when poetry build fails to create a wheel distribution. Check build system and dependencies."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry could not build a wheel for your package. The build process failed during compilation or packaging.

## Common Causes

- Missing build system in `pyproject.toml`
- C extension compilation fails without required compilers
- setup.py has errors
- Package metadata is incomplete

## How to Fix

### 1. Add Build System

```toml
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### 2. Install Build Dependencies

```bash
# Debian/Ubuntu
sudo apt install build-essential python3-dev

# macOS
xcode-select --install
```

### 3. Test Build with Verbose Output

```bash
poetry build -vvv
```

### 4. Check for setup.py Issues

```bash
python setup.py check
```

## Examples

```bash
$ poetry build
error: command 'gcc' failed

$ sudo apt install python3-dev build-essential
$ poetry build
Building myproject (1.0.0)
  - Building sdist
  - Building wheel
```
