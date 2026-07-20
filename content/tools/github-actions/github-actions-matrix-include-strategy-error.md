---
title: "[Solution] GitHub Actions Matrix Include Strategy Error"
description: "Fix GitHub Actions matrix include strategy errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Matrix include strategy errors occur when `include` adds invalid combinations:

```
Error: Invalid matrix include: unknown key 'node-verion'
```

## Common Causes

- Typo in include keys (must match matrix keys).
- Include adds values not in the matrix.

## How to Fix

**Use include correctly:**

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
    include:
      - node-version: 20
        os: ubuntu-latest
        experimental: true
```

## Examples

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    include:
      - node-version: 20
        npm-version: 'latest'
```
