---
title: "[Solution] CircleCI Docker Compose Service Startup"
description: "Fix CircleCI docker-compose service startup failures when services defined in docker-compose.yml fail to become healthy."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Docker Compose Service Startup

Docker Compose service startup failures occur when services defined in `docker-compose.yml` start but do not become healthy before the job script runs.

## Common Causes

- Service requires more time to initialize than the default timeout
- Health check configuration is too aggressive
- Service depends on another service that has not started
- Insufficient resources for the service to start

## How to Fix

### Solution 1: Add a wait-for-service step

```yaml
steps:
  - run:
      name: Start services
      command: docker-compose up -d
  - run:
      name: Wait for database
      command: |
        until docker-compose exec db pg_isready -U postgres; do
          echo "Waiting for database..."
          sleep 2
        done
```

### Solution 2: Use Docker health checks in compose

```yaml
version: "3.8"
services:
  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
```

### Solution 3: Increase machine resources

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
ERROR: Service 'db' failed to start within timeout
WARNING: Container health check failed
```

## Prevent It

- Configure health checks for all services
- Add explicit wait steps before dependent jobs
- Increase resource class for service-heavy jobs
