---
title: "[Solution] GitHub Actions Cache Path Not Found"
description: "Fix GitHub Actions cache path not found errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cache path not found errors occur when the specified cache path does not exist:

```
Warning: Path to cache does not exist: ./node_modules
```

## Common Causes

- Dependencies not installed before caching.
- Incorrect path in the cache configuration.

## How to Fix

**Ensure path exists before caching:**

```yaml
steps:
  - uses: actions/checkout@v4
  - run: npm ci
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```yaml
- run: ls -la node_modules || echo "node_modules not found"
```
