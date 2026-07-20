---
title: "[Solution] Workflow Runs-On Invalid Value Error"
description: "Fix GitHub Actions runs-on invalid value errors when the runner label is not recognized."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The `runs-on` value must be a valid runner label or group:

```
Error: .github/workflows/ci.yml: runs-on 'ubnutu-latest' is not a valid runner
```

## Common Causes

- Typo in the runner label (e.g., `ubnutu-latest`).
- Using a self-hosted runner label that is not registered.
- Using a deprecated runner image.

## How to Fix

**Use valid runner labels:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong
runs-on: ubnutu-latest

# Correct
runs-on: ubuntu-latest

# Self-hosted with labels
runs-on: [self-hosted, linux, x64]
```
