---
title: "[Solution] GitHub Actions Usage Limit Exceeded"
description: "Fix GitHub Actions usage limit exceeded errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Usage limit exceeded errors occur when workflow limits are hit:

```
Error: Maximum workflow run limit exceeded (1000 per day)
```

## Common Causes

- Too many workflow runs triggered.
- Workflow run trigger loop.
- Scheduled workflows running too frequently.

## How to Fix

**Limit scheduled workflows:**

```yaml
on:
  schedule:
    - cron: '0 0 * * 1'
```

## Examples

```yaml
on:
  push:
    paths-ignore:
      - '**.md'
      - 'docs/**'
```
