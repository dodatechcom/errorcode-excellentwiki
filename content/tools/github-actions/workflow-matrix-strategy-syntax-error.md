---
title: "[Solution] Workflow Matrix Strategy Syntax Error"
description: "Fix GitHub Actions matrix strategy syntax errors in workflow YAML."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Matrix strategy syntax errors occur when the `strategy.matrix` block is malformed:

```
Error: Invalid matrix configuration
```

## Common Causes

- Matrix values are not lists.
- Nested matrix definitions are incorrect.
- `include` or `exclude` are used incorrectly.

## How to Fix

**Use proper matrix syntax:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18, 20]
        os: [ubuntu-latest, windows-latest]
```

## Examples

```yaml
# Wrong - matrix values not lists
strategy:
  matrix:
    node-version: 18

# Correct
strategy:
  matrix:
    node-version: [16, 18, 20]
```
