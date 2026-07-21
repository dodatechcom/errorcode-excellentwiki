---
title: "[Solution] CircleCI Docker Layer Cache Registry Auth"
description: "Fix CircleCI Docker layer cache registry authentication errors when the cache cannot be stored or retrieved from a private registry."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Docker Layer Cache Registry Auth

Docker layer cache registry authentication errors occur when the pipeline cannot authenticate with the registry to store or retrieve Docker build cache layers.

## Common Causes

- Docker Hub rate limiting blocks anonymous pulls
- Registry credentials not passed to the machine executor
- Cache image was deleted or garbage collected
- Registry token expired during a long-running build

## How to Fix

### Solution 1: Use authenticated Docker Hub pulls

```yaml
jobs:
  build:
    machine:
      image: ubuntu-2204:2023.10.1
    steps:
      - run:
          name: Login to Docker Hub
          command: echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin
      - run:
          name: Build with cache
          command: |
            docker build \
              --cache-from myorg/app:latest \
              --build-arg BUILDKIT_INLINE_CACHE=1 \
              -t myorg/app:$CIRCLE_SHA1 .
```

### Solution 2: Use private registry for cache

```yaml
jobs:
  build:
    machine:
      image: ubuntu-2204:2023.10.1
    steps:
      - run:
          name: Login to private registry
          command: echo "$REGISTRY_PASSWORD" | docker login registry.example.com -u "$REGISTRY_USER" --password-stdin
      - run:
          name: Build with registry cache
          command: |
            docker build \
              --cache-from registry.example.com/myorg/cache:latest \
              -t registry.example.com/myorg/app:$CIRCLE_SHA1 .
```

### Solution 3: Use CircleCI Docker layer caching

```yaml
jobs:
  build:
    machine:
      image: ubuntu-2204:2023.10.1
    docker_layer_caching: true
    steps:
      - checkout
      - run: docker build .
```

## Examples

```
Error: toomanyrequests: You have reached your pull rate limit
ERROR: cache-from: authentication required
```

## Prevent It

- Authenticate with Docker Hub before builds
- Use `docker_layer_caching: true` for machine executor
- Pin cache image tags to prevent garbage collection
