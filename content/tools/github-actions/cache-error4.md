---
title: "[Solution] GitHub Actions Cache Restore Error"
description: "Fix GitHub Actions cache restore errors. Resolve cache miss and cache key issues."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "cache", "restore", "key", "dependency"]
weight: 5
---

# GitHub Actions Cache Restore Error

A cache restore error occurs when the `actions/cache` action cannot restore a previously saved cache. This results in a full re-download of dependencies, slowing down the workflow.

## Common Causes

- The cache key does not match any previously saved cache
- The cache was evicted due to storage limits (10 GB per repository)
- The `path` specified does not match what was cached
- The cache key changes on every run due to non-deterministic input

## How to Fix

### Use a Stable Cache Key

```yaml
steps:
  - uses: actions/cache@v4
    with:
      path: ~/.npm
      key: npm-${{ runner.os }}-${{ hashFiles('package-lock.json') }}
      restore-keys: |
        npm-${{ runner.os }}-
```

### Cache the Correct Path

```yaml
steps:
  - uses: actions/cache@v4
    with:
      path: |
        ~/.gradle/caches
        ~/.gradle/wrapper
      key: gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}
```

### Use the Cache Action with setup-node

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'  # automatically caches ~/.npm
```

### Verify Cache Hit in Logs

```yaml
steps:
  - uses: actions/cache@v4
    id: cache
    with:
      path: node_modules
      key: deps-${{ hashFiles('package-lock.json') }}
  - run: echo "Cache hit: ${{ steps.cache.outputs.cache-hit }}"
```

## Examples

```yaml
# Key changes every run due to github.run_id
key: deps-${{ github.run_id }}  # always misses — wrong
# Fix: use hashFiles('package-lock.json') for stable key

# Wrong path cached
path: node_modules  # workspace-specific, not cached
# Fix: use ~/.npm for npm cache
```

## Related Errors

- [Secret Error]({{< relref "/tools/github-actions/secret-error" >}}) — secret not found
- [Step Failed]({{< relref "/tools/github-actions/step-failed" >}}) — step execution failure
