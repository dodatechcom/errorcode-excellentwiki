---
title: "[Solution] GitHub Actions Restore Key Failed"
description: "Fix GitHub Actions restore-keys fallback failures."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Restore key failures occur when no fallback keys match any cached data:

```
Warning: Failed to restore cache for key: Linux-npm-
```

## Common Causes

- No cache exists for any matching prefix.
- Cache was evicted due to storage limits.

## How to Fix

**Use broader restore keys:**

```yaml
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-
      ${{ runner.os }}-
```

## Examples

```yaml
restore-keys: |
  Linux-npm-1.2.3
  Linux-npm-
  Linux-
```
