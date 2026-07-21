---
title: "[Solution] CircleCI Build Caching Strategy Conflict"
description: "Fix CircleCI build caching strategy conflicts when multiple cache configurations overlap and produce unexpected results."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Build Caching Strategy Conflict

Build caching strategy conflicts occur when multiple `restore_cache` and `save_cache` steps use overlapping keys, causing unexpected cache hits or misses.

## Common Causes

- Multiple `save_cache` steps with the same key prefix
- `restore_cache` matches an outdated cache instead of the latest
- Cache keys include dynamic values that change unpredictably
- Fallback keys match stale caches from previous branches

## How to Fix

### Solution 1: Use unique cache key prefixes

```yaml
steps:
  - restore_cache:
      keys:
        - npm-v1-{{ checksum "package-lock.json" }}
        - npm-v1-
  - run: npm ci
  - save_cache:
      key: npm-v1-{{ checksum "package-lock.json" }}
      paths:
        - node_modules
```

### Solution 2: Separate cache layers

```yaml
steps:
  - restore_cache:
      keys:
        - pip-v1-{{ checksum "requirements.txt" }}
  - run: pip install -r requirements.txt
  - save_cache:
      key: pip-v1-{{ checksum "requirements.txt" }}
      paths:
        - ~/.cache/pip
```

### Solution 3: Use partial key matching carefully

```yaml
restore_cache:
  keys:
    - v2-deps-{{ checksum "lock.json" }}  # Exact match first
    - v2-deps-  # Partial match fallback
    - v1-deps-  # Older version fallback
```

## Examples

```
Warning: Cache restored with outdated key
Error: Multiple caches match the same key pattern
```

## Prevent It

- Use versioned cache key prefixes (v1, v2)
- Include checksum files for exact matching
- Limit fallback key depth to 2-3 levels
