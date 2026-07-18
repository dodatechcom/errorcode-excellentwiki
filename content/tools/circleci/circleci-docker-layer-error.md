---
title: "[Solution] CircleCI Docker Layer Caching Error"
description: "Fix CircleCI docker layer caching errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Docker Layer Caching Error

CircleCI Docker layer caching errors occur when DLC fails to speed up builds.

## Why This Happens

- DLC not available
- Cache not found
- DLC exhausted
- Image rebuild required

## Common Error Messages

- `dlc_not_available_error`
- `dlc_cache_error`
- `dlc_exhausted_error`
- `dlc_rebuild_error`

## How to Fix It

### Solution 1: Enable DLC

Enable Docker layer caching:

```yaml
jobs:
  build:
    docker:
      - image: cimg/base:current
        docker_layer_caching: true
```

### Solution 2: Check DLC availability

Verify DLC is available for your plan.

### Solution 3: Optimize Dockerfile

Use multi-stage builds for better caching.


## Common Scenarios

- **DLC not available:** Check your plan supports DLC.
- **Cache not found:** DLC may have been cleared.

## Prevent It

- Enable DLC for builds
- Optimize Dockerfiles
- Monitor cache hit rate
