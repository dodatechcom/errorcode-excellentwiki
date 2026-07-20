---
title: "[Solution] GitHub Actions Dependencies Hash Mismatch"
description: "Fix GitHub Actions cache hash mismatch issues in dependency caching."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Hash mismatch errors occur when the lock file hash changes unexpectedly:

```
Warning: Cache key hash mismatch - expected abc123, got def456
```

## Common Causes

- Lock file regenerated between cache save and restore.
- Different package manager versions producing different hashes.

## How to Fix

**Ensure consistent lock file generation:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
```

## Examples

```yaml
key: ${{ runner.os }}-npm-${{ hashFiles('package-lock.json') }}
```
