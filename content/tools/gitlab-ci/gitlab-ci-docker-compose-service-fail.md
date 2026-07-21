---
title: "[Solution] GitLab CI Docker Compose Service Fail"
description: "Resolve GitLab CI docker-compose service failures when services defined in docker-compose.yml cannot start in the pipeline."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Docker Compose Service Fail

Docker Compose service failures occur when services defined for a GitLab CI job cannot be started due to configuration or resource constraints.

## Common Causes

- Docker Compose file references images that cannot be pulled
- Port conflicts between services and the runner host
- Insufficient runner resources (CPU, memory, disk)
- Docker-in-Docker (DinD) is not configured or accessible
- Service health checks fail before the job script starts

## How to Fix

### Solution 1: Use GitLab services instead of Compose

Replace docker-compose with native GitLab CI services:

```yaml
test_job:
  services:
    - name: postgres:15
      alias: db
    - name: redis:7
      alias: cache
  variables:
    POSTGRES_DB: testdb
    POSTGRES_PASSWORD: secret
```

### Solution 2: Configure DinD properly

Ensure Docker-in-Docker is available and uses the correct TLS settings:

```yaml
test_job:
  image: docker:24.0
  services:
    - docker:24.0-dind
  variables:
    DOCKER_HOST: tcp://docker:2376
    DOCKER_TLS_CERTDIR: "/certs"
```

### Solution 3: Increase runner resource limits

Adjust executor resources in `config.toml`:

```toml
[[runners]]
  [runners.docker]
    memory = "4g"
    cpus = "2"
```

## Examples

```
ERROR: Failed to start docker-compose services
ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock
```

## Prevent It

- Use native CI services when possible instead of docker-compose
- Verify DinD is running before job execution
- Set resource limits appropriate for your workloads
