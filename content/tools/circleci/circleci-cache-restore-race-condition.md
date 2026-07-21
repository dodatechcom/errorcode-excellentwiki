---
title: "[Solution] CircleCI Cache Restore Race Condition"
description: "Fix CircleCI cache restore race conditions when concurrent jobs restore the same cache simultaneously, causing corruption or stale data."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Cache Restore Race Condition

Cache restore race conditions occur when multiple parallel or concurrent jobs attempt to restore and use the same cache simultaneously, potentially reading incomplete or stale data.

## Common Causes

- Multiple jobs use the same cache key without coordination
- Parallel containers restore cache while another is writing
- Cache key does not include job-specific identifiers
- `save_cache` from one job interferes with `restore_cache` of another

## How to Fix

### Solution 1: Use job-specific cache keys

```yaml
jobs:
  build:
    steps:
      - restore_cache:
          keys:
            - build-v1-{{ checksum "package-lock.json" }}
      - run: npm ci
      - save_cache:
          key: build-v1-{{ checksum "package-lock.json" }}
          paths:
            - node_modules
```

### Solution 2: Use read-only cache for test jobs

```yaml
jobs:
  test:
    steps:
      - restore_cache:
          keys:
            - build-v1-{{ checksum "package-lock.json" }}
      # Do not save cache in test jobs
      - run: npm test
```

### Solution 3: Use workspaces instead of caches for shared state

```yaml
jobs:
  build:
    steps:
      - run: npm ci
      - persist_to_workspace:
          root: .
          paths:
            - node_modules
```

## Examples

```
Warning: Cache was modified while being read
ERROR: Cache restore produced inconsistent state
```

## Prevent It

- Use unique cache keys per job and branch
- Prefer workspaces for inter-job dependencies
- Avoid writing to shared cache keys from parallel jobs
