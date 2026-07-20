---
title: "[Solution] GitHub Actions Cache Not Found"
description: "Fix GitHub Actions cache not found warnings during restore."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cache not found warnings occur when no existing cache matches the key:

```
Warning: Cache not found for key: Linux-npm-abc123
```

## Common Causes

- First run of the workflow (no cache exists yet).
- Cache key changed due to lock file update.
- Cache expired (90-day retention limit).

## How to Fix

**Use restore-keys for fallback:**

```yaml
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

## Examples

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.cache/pip
      node_modules
    key: ${{ runner.os }}-${{ hashFiles('**/requirements.txt') }}-${{ hashFiles('**/package-lock.json') }}
```
