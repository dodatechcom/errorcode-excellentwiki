---
title: "[Solution] GitHub Actions Cache Size Limit Exceeded"
description: "Fix GitHub Actions cache size limit exceeded errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cache size limit errors occur when the total cached data exceeds GitHub's limit:

```
Error: Cache size of 11.5 GB exceeds the maximum cache size of 10 GB
```

## Common Causes

- Large node_modules directory.
- Multiple large cache entries across workflows.

## How to Fix

**Prune unnecessary files before caching:**

```yaml
steps:
  - name: Clean before cache
    run: |
      rm -rf node_modules/.cache
      rm -rf .next/cache
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```yaml
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```
