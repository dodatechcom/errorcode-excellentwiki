---
title: "[Solution] GitHub Actions Sparse Checkout Error"
description: "Fix GitHub Actions sparse checkout configuration errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Sparse checkout errors occur when the sparse-checkout configuration is invalid:

```
Error: fatal: invalid path 'src/index.ts' from sparse checkout
```

## Common Causes

- Incorrect path patterns in sparse-checkout.
- Trying to checkout a path that does not exist.

## How to Fix

**Configure sparse checkout properly:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      sparse-checkout: |
        src/
        package.json
      sparse-checkout-cone-mode: false
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      sparse-checkout: |
        packages/core
        packages/utils
      sparse-checkout-cone-mode: true
```
