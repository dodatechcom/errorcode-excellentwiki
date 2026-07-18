---
title: "[Solution] GitLab CI Cache Error"
description: "Fix GitLab CI cache errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Cache Error

Cache errors occur when dependency caches fail to save or restore between pipeline runs, causing slower builds.

## Why This Happens

- Cache key mismatch
- Cache corruption
- Cache too large
- Incorrect cache policy

## Common Error Messages

- `cache_save_failed`
- `cache_restore_failed`
- `cache_corrupted`
- `cache_key_conflict`

## How to Fix It

### Solution 1: Use file-based keys

Key on dependency lock files for better cache hit rates:

```yaml
cache:
  key:
    files:
      - package-lock.json
      - requirements.txt
```

### Solution 2: Separate push and pull policies

Use separate policies for saving and restoring:

```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
  policy: pull-push
```

### Solution 3: Clear corrupted caches

Manually clear caches via CI/CD > Caches or use the API.


## Common Scenarios

- **Cache not restored:** Verify keys match between save and restore jobs.
- **Cache too slow:** Consider using artifacts for more reliable file passing between jobs.

## Prevent It

- Use key: files
- Separate push/pull policies
- Monitor cache size
