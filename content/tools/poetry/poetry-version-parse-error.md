---
title: "[Solution] Poetry Version Parse Error -- Fix Invalid Version String"
description: "Fix Poetry version parse errors when a package version string in pyproject.toml or lock file cannot be parsed. Correct the version format."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry encountered a version string that does not follow PEP 440 or Poetry's version constraint syntax. The parser rejected the string.

## Common Causes

- Version string contains invalid characters
- Using npm-style version ranges in wrong context
- Version string has leading or trailing whitespace
- Missing version constraint after package name

## How to Fix

### 1. Check the Version String

```bash
poetry show --top-level
```

### 2. Use Valid Poetry Version Syntax

```toml
[tool.poetry.dependencies]
requests = "^2.28"      # Compatible release
flask = ">=2.0,<3.0"    # Range
django = "4.2.*"         # Wildcard
pillow = "==10.0.0"      # Exact
```

### 3. Fix Trailing Whitespace

```bash
sed -i 's/[[:space:]]*$//' pyproject.toml
poetry check
```

### 4. Validate the pyproject.toml

```bash
poetry check
```

## Examples

```bash
$ poetry install
InvalidVersion: Invalid version: '2.28..0'

# Fix in pyproject.toml:
requests = "^2.28"  # was "2.28..0"

$ poetry check
All checks passed!
```
