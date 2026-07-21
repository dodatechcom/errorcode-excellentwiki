---
title: "[Solution] Poetry Build No Setup.py -- Fix Missing Build Script"
description: "Fix Poetry build fails when no setup.py or pyproject.toml build configuration exists. Configure the build backend for your Poetry project."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry tried to build a distribution but found no valid build configuration. The project is missing required build metadata.

## Common Causes

- `pyproject.toml` is missing the `[build-system]` section
- The project was created with `poetry init` but never configured for building
- setup.py was deleted
- The build backend is misconfigured

## How to Fix

### 1. Add Build System to pyproject.toml

```toml
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### 2. Use Poetry's Built-in Builder

```bash
poetry build
```

### 3. Initialize Build Configuration

```bash
poetry init --build-backend poetry
```

### 4. Check the Build System Section

```bash
poetry check
```

## Examples

```bash
$ poetry build
ModuleNotFoundError: No module named 'poetry.core.masonry.api'

# Fix pyproject.toml build-system section:
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

$ poetry build
Building myproject (1.0.0)
  - Building sdist
  - Building wheel
```
