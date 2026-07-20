---
title: "[Solution] GitHub Actions Cache Key Not Matching"
description: "Fix GitHub Actions cache key mismatch issues."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cache key not matching errors occur when the computed key does not match any stored cache:

```
Cache key mismatch: expected 'Linux-npm-abc123', found none
```

## Common Causes

- Hash of lock file changed.
- Operating system label changed.
- Cache key format inconsistent across runs.

## How to Fix

**Use a stable cache key format:**

```yaml
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```yaml
key: ${{ runner.os }}-node-${{ matrix.node-version }}-${{ hashFiles('**/package-lock.json') }}
```
