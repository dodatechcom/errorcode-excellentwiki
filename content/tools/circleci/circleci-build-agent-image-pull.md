---
title: "[Solution] CircleCI Build Agent Image Pull Fail"
description: "Fix CircleCI build agent image pull failures when the executor Docker image cannot be pulled from the registry."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Build Agent Image Pull Fail

Build agent image pull failures occur when CircleCI cannot pull the Docker image specified in the executor configuration to start the build environment.

## Common Causes

- Image tag does not exist in the registry
- Docker Hub rate limiting blocks the pull
- Private registry requires authentication
- Network connectivity issues with the image registry
- Image was removed or deprecated

## How to Fix

### Solution 1: Use official CircleCI convenience images

```yaml
jobs:
  build:
    docker:
      - image: cimg/node:18.0  # Official CircleCI image
```

### Solution 2: Authenticate for private images

```yaml
jobs:
  build:
    docker:
      - image: myprivate-registry.com/my-app:latest
        auth:
          username: $REGISTRY_USERNAME
          password: $REGISTRY_PASSWORD
```

### Solution 3: Use a cached or mirrored image

```yaml
jobs:
  build:
    docker:
      - image: mirror.example.com/cimg/node:18.0
```

## Examples

```
Error: Unable to pull Docker image 'myorg/custom-image:latest'
ERROR: You have reached your pull rate limit
```

## Prevent It

- Use official `cimg/` images when possible
- Authenticate with registries before pulling
- Pin specific image tags for reproducibility
