---
title: "[Solution] GitHub Actions Checkout Action Failed"
description: "Fix GitHub Actions actions/checkout failures during workflow execution."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Checkout failures occur when the `actions/checkout` step fails:

```
Error: fatal: could not create leading directories: No such file or directory
```

## Common Causes

- Repository is large and checkout times out.
- Permissions insufficient for the repository.
- Submodules or LFS are not configured.

## How to Fix

**Shallow clone for faster checkout:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 1
```

**Fetch all branches and tags:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
      fetch-tags: true
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 1
      lfs: true
      submodules: recursive
```
