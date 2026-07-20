---
title: "[Solution] GitHub Actions Cache Upload Rejected"
description: "Fix GitHub Actions cache upload rejected errors during save."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cache upload rejected errors occur when the cache service rejects the upload:

```
Error: Cache upload failed: 413 Request Entity Too Large
```

## Common Causes

- Individual cache entry too large.
- Rate limiting from cache service.

## How to Fix

**Split large caches into smaller entries:**

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}

- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

## Examples

```yaml
- uses: actions/cache@v4
  continue-on-error: true
  with:
    path: ~/.cache
    key: build-${{ github.sha }}
```
