---
title: "[Solution] Poetry Remove Active Dependency -- Fix Removing Required Package"
description: "Fix Poetry remove active dependency errors when removing a package that other packages still depend on. Update dependent packages first."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means you tried to remove a package that is still required by another dependency in your project. Poetry refuses to create an inconsistent state.

## Common Causes

- Another dependency in `pyproject.toml` depends on the package
- The package is imported directly in your code
- A transitive dependency requires it

## How to Fix

### 1. Check What Depends on It

```bash
poetry show --tree <package>
```

### 2. Remove Dependent Packages First

```bash
poetry remove dependent-package
poetry remove <package>
```

### 3. Force Remove (Careful)

```bash
poetry remove <package> --sync
```

### 4. Move to Optional Dependency

```toml
[tool.poetry.group.testing.dependencies]
pytest = "^7.0"
```

## Examples

```bash
$ poetry remove requests
SolverProblemError

Because myproject depends on httpx (^0.25) which depends on
requests (>=2.20), removing requests would break httpx.

$ poetry remove httpx
$ poetry remove requests
```
