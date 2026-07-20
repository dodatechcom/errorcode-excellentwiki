---
title: "[Solution] GitHub Actions Submodule Not Found Error"
description: "Fix GitHub Actions submodule not found errors during checkout."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Submodule errors occur when submodules are not initialized during checkout:

```
Error: warning: failed to load submodule 'vendor/lib'
fatal: could not find remote ref refs/heads/main
```

## Common Causes

- Submodules not configured in the checkout step.
- Submodule URL uses SSH and no SSH key is available.

## How to Fix

**Checkout with submodules:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      submodules: recursive
      token: ${{ secrets.GITHUB_TOKEN }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      submodules: true
      fetch-depth: 0
```
