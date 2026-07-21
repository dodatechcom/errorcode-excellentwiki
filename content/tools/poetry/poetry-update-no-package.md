---
title: "[Solution] Poetry Update No Package -- Fix Nothing to Update"
description: "Fix poetry update no package found when Poetry reports no packages need updating. Check dependency constraints and lock file state."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry update` found no packages that can be updated within the constraints defined in `pyproject.toml`.

## Common Causes

- All packages are already at the latest compatible version
- Version constraints prevent any updates
- The lock file is already up to date

## How to Fix

### 1. Widen Version Constraints

```toml
[tool.poetry.dependencies]
requests = "^2.28"  # Widen to allow newer versions
```

### 2. Update All to Latest

```bash
poetry add requests@latest
```

### 3. Check What Would Change

```bash
poetry update --dry-run
```

### 4. Remove Lock and Regenerate

```bash
rm poetry.lock
poetry lock
```

## Examples

```bash
$ poetry update
No updates available

$ poetry add requests@latest
$ poetry update
Updating requests (2.28.0 -> 2.31.0)
```
