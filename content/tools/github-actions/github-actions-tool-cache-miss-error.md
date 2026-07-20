---
title: "[Solution] GitHub Actions Tool Cache Miss Error"
description: "Fix GitHub Actions tool cache miss errors when required tools are not cached."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Tool cache miss errors occur when a required tool is not available in the runner's tool cache:

```
Error: Unable to find any version of node matching: 21.x
```

## Common Causes

- Requested tool version is not pre-installed on the runner.
- Tool version was recently released and not yet added to the runner image.

## How to Fix

**Use setup actions that handle caching:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
```

## Examples

```yaml
# Use a version that is available
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: '20'
```
