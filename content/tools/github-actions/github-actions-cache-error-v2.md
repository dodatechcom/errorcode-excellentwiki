---
title: "GitHub Actions Cache Restore Failed"
description: "GitHub Actions cache action fails to restore cached dependencies."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "cache", "restore", "dependencies", "performance"]
weight: 5
---

# GitHub Actions — Cache Restore Failed

This error occurs when the `actions/cache` action fails to restore a cached dependency. The cache key may not match, or the cache may have been evicted.

## Common Causes

- Cache key does not match any existing cache
- Cache was evicted due to size or age
- Cache scope mismatch (repo vs org)
- Cache corrupted during save

## How to Fix

### Use Cache with Restore Keys

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: npm-${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      npm-${{ runner.os }}-
```

### Check Cache Hit

```yaml
- uses: actions/cache@v4
  id: cache
  with:
    path: ~/.npm
    key: npm-${{ hashFiles('**/package-lock.json') }}

- run: npm ci
  if: steps.cache.outputs.cache-hit != 'true'
```

### Cache Node Modules

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      node_modules
    key: deps-${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}
```

### Limit Cache Size

```bash
# Only cache necessary files
path: |
  ~/.gradle/caches
  ~/.gradle/wrapper
  !~/.gradle/caches/build-cache-*
```

### Verify Cache Permissions

```yaml
permissions:
  actions: write
```

## Examples

```text
Warning: Cache not found for key: npm-Linux-abc123def456.
Fallen back to partial restore.
```

## Related Errors

- [GitHub Actions Artifact Error]({{< relref "/tools/github-actions/github-actions-artifact-error" >}}) — artifact upload failure
- [GitHub Actions Permission Error]({{< relref "/tools/github-actions/github-actions-permission-error" >}}) — permission issues
- [GitHub Actions Runner Error]({{< relref "/tools/github-actions/github-actions-runner-error" >}}) — runner issues
