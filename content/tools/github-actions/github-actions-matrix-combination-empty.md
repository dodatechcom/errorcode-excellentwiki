---
title: "[Solution] GitHub Actions Matrix Combination Empty"
description: "Fix GitHub Actions matrix empty combination errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Empty combination errors occur when the matrix generates no valid combinations:

```
Error: Matrix produced zero combinations
```

## Common Causes

- All matrix combinations are excluded.
- Matrix values are empty lists.

## How to Fix

**Verify matrix combinations:**

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
    exclude:
      - node-version: 16
        os: windows-latest
```

## Examples

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
    exclude:
      - node-version: 16
        os: windows-latest
```
