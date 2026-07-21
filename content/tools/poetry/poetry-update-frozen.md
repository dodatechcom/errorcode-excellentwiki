---
title: "[Solution] Poetry Update Frozen -- Fix Cannot Update Frozen Dependencies"
description: "Fix Poetry update frozen errors when Poetry refuses to update packages that are pinned in pyproject.toml. Unfreeze constraints to allow updates."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry cannot update certain packages because their version constraints in `pyproject.toml` are pinned with exact versions rather than ranges.

## Common Causes

- Using `==` instead of `^` or `>=` in version constraints
- Lock file was generated with frozen constraints
- A dependency group has strict version pins

## How to Fix

### 1. Check Current Constraints

```bash
poetry show --top-level
```

### 2. Relax Pinned Versions

```toml
[tool.poetry.dependencies]
requests = "2.31.0"  # Change to "^2.31" for flexible pinning
```

### 3. Update Specific Package

```bash
poetry update requests
```

### 4. Regenerate Lock File

```bash
poetry lock --no-update
poetry update
```

## Examples

```bash
$ poetry update
SolverProblemError

The update would require changing the pinned version of requests (==2.31.0).

$ poetry add requests@^2.31
Resolving dependencies...
```
