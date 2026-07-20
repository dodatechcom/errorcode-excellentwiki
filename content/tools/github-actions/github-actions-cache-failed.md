---
title: "[Solution] GitHub Actions Cache Failed"
description: "Fix GitHub Actions actions/cache failures in workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cache action failures occur when `actions/cache` cannot save or restore:

```
Error: Cache not found for key: Linux-npm-abc123
```

## Common Causes

- Cache key does not match any existing cache.
- Cache size exceeds the 10GB limit.
- Network issues during cache upload.

## How to Fix

**Use setup actions with built-in caching:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
```

**Add cache with fallback:**

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-
```

## Examples

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```
