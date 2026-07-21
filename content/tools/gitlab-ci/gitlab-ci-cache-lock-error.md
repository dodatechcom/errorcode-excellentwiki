---
title: "[Solution] GitLab CI Cache Lock Error"
description: "Resolve GitLab CI cache lock errors when multiple jobs compete for the same cache key simultaneously."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Cache Lock Error

Cache lock errors occur when multiple concurrent jobs attempt to read and write to the same cache key at the same time, causing corruption or lock timeouts.

## Common Causes

- Multiple jobs share the same cache key without proper locking
- Parallel jobs in the same stage write to the same cache path
- Cache backend (S3 or GCS) has connectivity issues
- Default local cache shared across runners without isolation

## How to Fix

### Solution 1: Use unique cache keys per job

Add job-specific suffixes to prevent collisions:

```yaml
build_job:
  cache:
    key:
      files:
        - package-lock.json
      prefix: build-$CI_JOB_NAME
    paths:
      - node_modules/
```

### Solution 2: Use pull-push policy

Separate read and write operations to reduce lock contention:

```yaml
test_job:
  cache:
    key: deps-$CI_COMMIT_REF_SLUG
    paths:
      - node_modules/
    policy: pull
```

### Solution 3: Use artifact passing instead of cache

For critical build outputs, prefer artifacts over cache:

```yaml
build_job:
  artifacts:
    paths:
      - node_modules/
    expire_in: 1 hour
```

## Examples

```
WARNING: Retrying cache recovery... x3
error: could not read from cache
cache lock: unable to acquire lock
```

## Prevent It

- Use `pull-push` and `pull` policies appropriately
- Scope cache keys to branch and job name
- Consider using artifacts for inter-stage dependencies
