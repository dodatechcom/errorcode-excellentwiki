---
title: "[Solution] GitHub Actions Strategy Fallback"
description: "Fix GitHub Actions strategy fallback errors when matrix strategy has issues."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Strategy fallback errors occur when the matrix strategy cannot be resolved:

```
Error: Strategy matrix could not be resolved
```

## Common Causes

- Matrix values reference undefined variables.
- Expression in matrix value is invalid.

## How to Fix

**Use static matrix values:**

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
```

## Examples

```yaml
# Static matrix
strategy:
  matrix:
    node: [16, 18, 20]

# Dynamic matrix
strategy:
  matrix: ${{ fromJSON(needs.set-matrix.outputs.matrix) }}
```
