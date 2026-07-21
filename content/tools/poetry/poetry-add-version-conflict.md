---
title: "[Solution] Poetry Add Version Conflict -- Fix Dependency Version Clash"
description: "Fix Poetry add version conflict errors when adding a package creates incompatible version constraints with existing dependencies in pyproject.toml."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means adding a new package introduced version constraints that clash with existing dependencies in your `pyproject.toml`. Poetry refuses to add the package.

## Common Causes

- The new package requires a different version of a shared transitive dependency
- Your existing constraints are too narrow
- The package has strict minimum version requirements
- You pinned a dependency that conflicts with the new package's range

## How to Fix

### 1. Relax Existing Constraints

Edit `pyproject.toml` to widen version ranges:

```toml
[tool.poetry.dependencies]
requests = "^2.28"  # was ^2.30
```

### 2. Use --dry-run First

```bash
poetry add requests --dry-run
```

### 3. Update All Packages Together

```bash
poetry add requests@latest httpx@latest
```

### 4. Force the Addition

```bash
poetry add requests --lock
```

## Examples

```bash
$ poetry add httpx
SolverProblemError

Because myproject depends on requests (^2.30) and httpx (^0.25) depends on
httpcore (>=1.0.0,<2.0.0), version solving failed.

$ poetry add httpx requests@^2.28
Resolving dependencies...
```
