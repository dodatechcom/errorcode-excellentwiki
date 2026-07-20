---
title: "[Solution] GitHub Actions Restore Keys Pattern Error"
description: "Fix GitHub Actions restore-keys pattern matching errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Restore keys pattern errors occur when restore-keys patterns do not match correctly:

```
Warning: No cache found for restore-keys: ['Linux-npm-', 'Linux-']
```

## Common Causes

- restore-keys prefix does not match actual cache key format.
- Case sensitivity in key names.

## How to Fix

**Verify cache key structure:**

```yaml
- uses: actions/cache@v4
  id: cache
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-
```

## Examples

```yaml
key: Linux-npm-abc123
restore-keys: |
  Linux-npm-
  Linux-
```
