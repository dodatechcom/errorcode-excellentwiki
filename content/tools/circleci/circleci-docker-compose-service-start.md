---
title: "[Solution] CircleCI Docker Compose Service Start Fail"
description: "Fix CircleCI docker-compose service start failures when services defined in docker-compose.yml fail to start in the pipeline."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Docker Compose Service Start Fail

Docker Compose service start failures occur when services defined in a `docker-compose.yml` cannot be started during a CircleCI build due to image, network, or resource issues.

## Common Causes

- Service image not available in the Docker registry
- Port conflicts between services and the executor
- Insufficient memory or CPU for the machine executor
- Docker Compose version mismatch with the executor image
- Network connectivity lost during image pull

## How to Fix

### Solution 1: Use CircleCI services instead

Replace docker-compose with native services:

```yaml
jobs:
  test:
    docker:
      - image: cimg/node:18.0
      - image: cimg/postgres:15.0
        environment:
          POSTGRES_DB: testdb
          POSTGRES_PASSWORD: secret
```

### Solution 2: Pin Docker Compose version

```yaml
jobs:
  test:
    machine:
      image: ubuntu-2204:2023.10.1
    steps:
      - run:
          name: Install specific Docker Compose
          command: |
            sudo curl -L "https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
            sudo chmod +x /usr/local/bin/docker-compose
      - run:
          name: Start services
          command: docker-compose up -d
```

### Solution 3: Increase machine executor resources

```yaml
jobs:
  test:
    machine:
      image: ubuntu-2204:2023.10.1
    resource_class: large
    steps:
      - checkout
      - run: docker-compose up -d
```

## Examples

```
ERROR: Could not pull image for service 'db'
ERROR: Cannot start container: port is already allocated
```

## Prevent It

- Use CircleCI native services when possible
- Pin docker-compose version for reproducibility
- Set resource_class appropriately for service-heavy jobs
