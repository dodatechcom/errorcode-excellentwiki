---
title: "[Solution] GitHub Actions Matrix Axis Unsupported"
description: "Fix GitHub Actions unsupported matrix axis errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Unsupported matrix axis errors occur when a matrix key is not valid:

```
Error: Invalid matrix key 'os-name': must not contain hyphens
```

## Common Causes

- Matrix key contains invalid characters.
- Matrix key conflicts with built-in variables.

## How to Fix

**Use valid matrix key names:**

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [16, 18, 20]
    include:
      - os: ubuntu-latest
        node: 20
        experimental: false
```

## Examples

```yaml
matrix:
  os: [ubuntu-latest, windows-latest]
  node-version: [16, 18, 20]
  python-version: ['3.9', '3.10', '3.11']
```
