---
title: "[Solution] GitLab CI Service Container DNS"
description: "Fix GitLab CI service container DNS resolution errors when jobs cannot reach services by their alias hostname."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Service Container DNS

Service container DNS resolution errors occur when a job container cannot resolve or connect to a service container using its configured alias hostname.

## Common Causes

- Service alias is misspelled or does not match the variable reference
- Service container is still starting when the job runs
- Network namespace mismatch between job and service containers
- Docker network mode prevents DNS resolution

## How to Fix

### Solution 1: Verify service alias in variables

```yaml
test_job:
  services:
    - name: postgres:15
      alias: db
  variables:
    POSTGRES_HOST: db  # Must match the alias
    POSTGRES_DB: testdb
    POSTGRES_PASSWORD: secret
  script:
    - pg_isready -h $POSTGRES_HOST
```

### Solution 2: Add a wait-for-service step

```yaml
test_job:
  services:
    - name: redis:7
      alias: redis
  script:
    - until redis-cli -h redis ping; do sleep 1; done
    - npm test
```

### Solution 3: Check DNS resolution manually

```yaml
test_job:
  before_script:
    - nslookup db || getent hosts db || echo "DNS resolution failed"
    - ping -c 2 db
```

## Examples

```
Error: getaddrinfo: Name or service not known for 'db'
FATAL: connection refused to db:5432
```

## Prevent It

- Always use the exact alias name in connection strings
- Add health checks or wait scripts for services
- Use `services:alias` consistently across jobs
