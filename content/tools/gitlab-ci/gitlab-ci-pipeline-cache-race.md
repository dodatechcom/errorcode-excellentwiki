---
title: "[Solution] GitLab CI Pipeline Caching Race Condition"
description: "Fix GitLab CI pipeline caching race conditions when concurrent pipelines overwrite or corrupt shared cache data."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Pipeline Caching Race Condition

Caching race conditions occur when multiple pipeline instances write to the same cache key simultaneously, causing partial or corrupted cache data.

## Common Causes

- Multiple pipelines for the same branch write to the same cache key
- Scheduled and branch pipelines run concurrently with shared keys
- Cache key does not include unique pipeline identifiers
- Pull-push policy used by parallel jobs in different pipelines

## How to Fix

### Solution 1: Use unique cache keys per branch

Include branch and commit information in cache keys:

```yaml
test_job:
  cache:
    key:
      files:
        - package-lock.json
      prefix: $CI_COMMIT_REF_SLUG
    paths:
      - node_modules/
```

### Solution 2: Use pull-only policy for read-heavy jobs

Prevent write contention by limiting cache writes:

```yaml
test_job:
  cache:
    key: deps-$CI_COMMIT_REF_SLUG
    paths:
      - node_modules/
    policy: pull
```

### Solution 3: Use artifacts for cross-pipeline isolation

Artifacts are scoped to specific pipelines, avoiding race conditions:

```yaml
build_job:
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour
```

## Examples

```
WARNING: Cache corrupted, discarding
WARNING: Unexpected cache miss for key deps-main
```

## Prevent It

- Include `$CI_COMMIT_REF_SLUG` or `$CI_COMMIT_SHA` in cache keys
- Use `policy: pull` on jobs that only read cache
- Prefer artifacts for critical build outputs
