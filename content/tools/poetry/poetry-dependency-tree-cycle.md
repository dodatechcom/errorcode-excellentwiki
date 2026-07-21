---
title: "[Solution] Poetry Dependency Tree Cycle -- Fix Circular Dependencies"
description: "Fix Poetry dependency tree cycle errors when circular dependencies are detected between packages. Break the cycle by removing or restructuring deps."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry detected a circular dependency chain where package A depends on B which depends on A. This is logically impossible to resolve.

## Common Causes

- Two packages have been configured to depend on each other
- A development dependency creates a cycle
- A path dependency references a parent project
- Git dependencies create a loop

## How to Fix

### 1. Show the Dependency Tree

```bash
poetry show --tree
```

### 2. Identify the Cycle

```bash
poetry show --tree <package>
```

### 3. Remove the Circular Dependency

Edit `pyproject.toml` to remove one direction of the cycle.

### 4. Use a Monorepo Approach

For self-referencing projects, use path dependencies with `[tool.poetry.group.dev.dependencies]`.

## Examples

```bash
$ poetry lock
SolverProblemError

Because myproject depends on package-a (^1.0) which depends on
myproject (^0.1), version solving failed.

# Remove the cycle in pyproject.toml
$ poetry lock
Resolving dependencies...
```
