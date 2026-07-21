---
title: "[Solution] Poetry Constraint Parse Error -- Fix Invalid Version Constraint"
description: "Fix Poetry constraint parse error when a version constraint in pyproject.toml is syntactically invalid. Correct the constraint syntax."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry could not parse a version constraint string. The constraint uses invalid syntax for Poetry's resolver.

## Common Causes

- Using npm-style tilde ranges incorrectly
- Mixing operators in invalid ways
- Extra whitespace in the constraint
- Using `||` instead of Poetry's comma syntax

## How to Fix

### 1. Use Poetry Version Syntax

```toml
[tool.poetry.dependencies]
# Compatible release
requests = "^2.28"

# Range
flask = ">=2.0,<3.0"

# Exact
django = "==4.2.0"

# Wildcard
pillow = "10.*"
```

### 2. Fix Invalid Constraints

```bash
poetry check
```

### 3. Replace npm-style Ranges

Poetry supports `~` for minor version pinning but not `||`.

### 4. Validate After Changes

```bash
poetry check
poetry lock --dry-run
```

## Examples

```bash
$ poetry add requests@">=2.0 || >=3.0"
InvalidVersion: Invalid constraint '>=2.0 || >=3.0'

$ poetry add "requests>=2.0,<4.0"
Resolving dependencies...
```
