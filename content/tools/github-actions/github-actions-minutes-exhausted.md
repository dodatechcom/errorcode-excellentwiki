---
title: "[Solution] GitHub Actions Minutes Exhausted"
description: "Fix GitHub Actions minutes exhausted errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Minutes exhausted errors occur when the billing minutes limit is reached:

```
Error: GitHub Actions: usage quota has been exceeded
```

## Common Causes

- Monthly minutes limit reached.
- Large matrix builds consuming many minutes.

## How to Fix

**Optimize workflow to use fewer minutes:**

```yaml
steps:
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

**Use concurrency to avoid duplicate runs:**

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

## Examples

```yaml
# Check billing at
# https://github.com/settings/billing
```
