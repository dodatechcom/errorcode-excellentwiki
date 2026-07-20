---
title: "[Solution] GitHub Actions Save Cache Failed"
description: "Fix GitHub Actions save cache failures after job completion."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Save cache failures occur when the cache action cannot write the cache:

```
Warning: Failed to save cache: unable to create cache
```

## Common Causes

- Cache size exceeds the 10 GB limit.
- Network issues during upload.

## How to Fix

**Reduce cache size:**

```yaml
steps:
  - name: Prune before caching
    run: |
      rm -rf node_modules/.cache
      npm prune
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```yaml
# Cache only the npm global store
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```
