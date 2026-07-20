---
title: "[Solution] GitHub Actions Matrix Not Defined"
description: "Fix GitHub Actions matrix not defined errors when matrix strategy is referenced but missing."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Matrix not defined errors occur when a matrix variable is referenced but not defined:

```
Error: Matrix variable 'node-version' is not defined
```

## Common Causes

- Variable referenced as `${{ matrix.node-version }}` but `strategy.matrix` is missing.
- Typo in the matrix variable name.

## How to Fix

**Define matrix in the job:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18, 20]
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
```

## Examples

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
```
