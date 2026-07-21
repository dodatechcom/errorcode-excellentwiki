---
title: "[Solution] CircleCI Custom Docker Image Registry Auth"
description: "Fix CircleCI custom Docker image registry authentication errors when the executor cannot pull images from private registries."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Custom Docker Image Registry Auth

Custom Docker image registry authentication errors occur when the CircleCI executor cannot authenticate with a private registry to pull the specified Docker image.

## Common Causes

- Registry credentials are not configured in CircleCI
- Docker Hub credentials expired or were revoked
- Registry requires specific authentication mechanism
- Credentials are scoped to a different namespace

## How to Fix

### Solution 1: Add registry credentials in project settings

Navigate to **Project Settings > Docker Hub** or **Project Settings > Registries** and add credentials.

```yaml
jobs:
  build:
    docker:
      - image: myorg/custom-image:latest
        auth:
          username: $DOCKERHUB_USERNAME
          password: $DOCKERHUB_PASSWORD
```

### Solution 2: Use a custom registry in config

```yaml
jobs:
  build:
    docker:
      - image: registry.example.com/myorg/image:latest
        auth:
          username: $REGISTRY_USER
          password: $REGISTRY_PASS
```

### Solution 3: Use pre-auth in a setup step

```yaml
jobs:
  build:
    docker:
      - image: cimg/base:current
    steps:
      - run:
          name: Pull private image
          command: |
            echo "$REGISTRY_PASS" | docker login registry.example.com -u "$REGISTRY_USER" --password-stdin
            docker pull registry.example.com/myorg/image:latest
```

## Examples

```
Error: Unable to pull Docker image 'myorg/custom:latest': unauthorized
ERROR: login attempt to registry failed
```

## Prevent It

- Configure Docker Hub credentials in project settings
- Use long-lived tokens for CI/CD authentication
- Test image pulls locally before adding to CI config
