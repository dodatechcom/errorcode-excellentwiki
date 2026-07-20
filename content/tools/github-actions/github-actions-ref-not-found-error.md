---
title: "[Solution] GitHub Actions Ref Not Found Error"
description: "Fix GitHub Actions ref not found errors when the specified branch or tag does not exist."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ref not found errors occur when the specified branch, tag, or commit does not exist:

```
Error: fatal: Remote branch release/v2 not found in upstream origin
```

## Common Causes

- Branch or tag was deleted.
- Typo in the ref name.

## How to Fix

**Use fallback ref:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      ref: ${{ github.head_ref || github.ref_name }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      ref: main
      fetch-depth: 0
```
