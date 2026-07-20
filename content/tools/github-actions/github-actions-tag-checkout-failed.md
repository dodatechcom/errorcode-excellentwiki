---
title: "[Solution] GitHub Actions Tag Checkout Failed"
description: "Fix GitHub Actions tag checkout failures during workflow execution."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Tag checkout failures occur when the workflow cannot checkout a specific tag:

```
error: pathspec 'v1.0.0' did not match any(s) known to git
```

## Common Causes

- Tag does not exist in the repository.
- Tags were not fetched (shallow clone).

## How to Fix

**Fetch tags explicitly:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
      fetch-tags: true
      ref: v1.0.0
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
  - name: Checkout tag
    run: |
      git tag -l | head -20
      git checkout v1.0.0
```
