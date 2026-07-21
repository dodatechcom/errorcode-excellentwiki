---
title: "[Solution] CircleCI Cache Key Pattern Error"
description: "Fix CircleCI cache key pattern errors when the restore_cache key does not match any previously saved cache."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Cache Key Pattern Error

Cache key pattern errors occur when `restore_cache` cannot find a matching cache because the key pattern does not match the key used in `save_cache`.

## Common Causes

- Cache key includes variable that was not set during save
- Glob pattern in cache key does not match the lock file
- Cache key format changed between pipeline runs
- Dependency file name is different from the key pattern

## How to Fix

### Solution 1: Use fallback keys

```yaml
steps:
  - restore_cache:
      keys:
        - deps-v1-{{ checksum "package-lock.json" }}
        - deps-v1-
        - deps-
  - run: npm ci
  - save_cache:
      key: deps-v1-{{ checksum "package-lock.json" }}
      paths:
        - node_modules
```

### Solution 2: Verify checksum file exists

```yaml
steps:
  - run:
      name: Check lock file
      command: ls -la package-lock.json
  - restore_cache:
      keys:
        - deps-{{ checksum "package-lock.json" }}
```

### Solution 3: Use consistent key naming

```yaml
# Always use the same prefix and version
save_cache:
  key: v1-deps-{{ checksum "package-lock.json" }}
  paths:
    - node_modules

restore_cache:
  keys:
    - v1-deps-{{ checksum "package-lock.json" }}
    - v1-deps-
```

## Examples

```
No cache found for key: deps-v2-abc123...
WARNING: Cache miss for restore_cache
```

## Prevent It

- Include fallback keys in `restore_cache`
- Use consistent version prefixes in cache keys
- Verify lock file exists before using in cache key
