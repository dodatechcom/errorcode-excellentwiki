---
title: "[Solution] GitHub Actions HEAD Detached Error"
description: "Fix GitHub Actions HEAD detached errors during workflow checkout."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

HEAD detached errors occur when the checkout results in a detached HEAD state:

```
Warning: You are in 'detached HEAD' state
```

## Common Causes

- Checking out a specific commit SHA instead of a branch.
- Fetch-depth too shallow for the target ref.

## How to Fix

**Checkout the branch explicitly:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      ref: ${{ github.head_ref }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      ref: ${{ github.event.pull_request.head.ref }}
      fetch-depth: 0
```
