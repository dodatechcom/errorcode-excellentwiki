---
title: "[Solution] GitHub Actions Hosted Runner Deprecation Error"
description: "Fix GitHub Actions hosted runner deprecation warnings and errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Deprecation errors occur when a workflow uses a runner image version that is being deprecated:

```
Warning: The ubuntu-18.04 runner image is being deprecated.
Please switch to ubuntu-latest or ubuntu-22.04
```

## Common Causes

- Workflow references an older runner image (e.g., `ubuntu-18.04`).
- Runner image reached end-of-life.

## How to Fix

**Update to the latest runner image:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong - deprecated
runs-on: ubuntu-18.04

# Correct - latest
runs-on: ubuntu-latest
```
