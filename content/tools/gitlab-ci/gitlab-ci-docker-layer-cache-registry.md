---
title: "[Solution] GitLab CI Docker Layer Cache Registry"
description: "Fix GitLab CI Docker layer cache registry errors when the Docker build cache cannot be stored or retrieved from a registry."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Docker Layer Cache Registry

Docker layer cache registry errors occur when the CI pipeline cannot use the registry-based cache for Docker builds due to authentication or connectivity issues.

## Common Causes

- Registry authentication token expired during build
- Registry rate limiting prevents layer pulls
- Cache image tag was deleted or garbage collected
- Registry TLS certificate is invalid or self-signed

## How to Fix

### Solution 1: Configure registry-based caching

```yaml
build_image:
  image: docker:24.0
  services:
    - docker:24.0-dind
  variables:
    DOCKER_BUILDKIT: "1"
    REGISTRY_CACHE: "$CI_REGISTRY_IMAGE/cache"
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build
      --cache-from $REGISTRY_CACHE:latest
      --cache-to $REGISTRY_CACHE:latest
      -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA .
```

### Solution 2: Set cache expiration

Preserve cache layers with appropriate expiration:

```yaml
build_image:
  script:
    - docker build
      --build-arg BUILDKIT_INLINE_CACHE=1
      --cache-from $CI_REGISTRY_IMAGE/cache:latest
      -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
    - docker tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA $CI_REGISTRY_IMAGE/cache:latest
    - docker push $CI_REGISTRY_IMAGE/cache:latest
```

### Solution 3: Use local cache fallback

```yaml
build_image:
  cache:
    key: docker-layers
    paths:
      - .docker-cache/
```

## Examples

```
ERROR: pull access denied for my-project/cache
WARNING: failed to pull cache image from registry
```

## Prevent It

- Use BuildKit with `BUILDKIT_INLINE_CACHE=1`
- Set up dedicated cache images with long expiration
- Monitor registry storage and rate limits
