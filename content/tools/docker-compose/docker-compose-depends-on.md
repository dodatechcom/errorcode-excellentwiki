---
title: "[Solution] Docker Compose Depends On Error — Fix Service Depends on Service That Failed"
description: "Fix Docker Compose depends_on errors when required services fail to start. Configure dependency conditions, healthchecks, and startup ordering correctly."
---

## What This Error Means

Docker Compose depends_on errors occur when a service starts but a service it depends on has failed. The dependent service cannot function without its prerequisites.

A typical error:

```
ERROR: Service 'app' depends on service 'db' which is unhealthy.
```

Or:

```
ERROR: Container db exited, cannot start app
```

## Why It Happens

Depends_on errors happen when:

- **Dependency fails to start**: The required service exits or becomes unhealthy before the dependent service starts.
- **Missing healthcheck**: depends_on without a healthcheck condition only waits for container start, not readiness.
- **Circular dependency**: Two services depend on each other, creating a deadlock.
- **Incorrect service name**: The service name in depends_on does not match any service definition.
- **Dependency configuration error**: The dependency's configuration is invalid and it cannot start.
- **Startup timeout**: The dependency takes longer to start than the configured timeout.

## How to Fix It

**Step 1: Check dependency status**

```bash
docker compose ps
docker compose logs <dependency>
```

**Step 2: Use healthcheck-based dependency conditions**

```yaml
services:
  app:
    image: my-app
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
      start_period: 30s
```

**Step 3: Use service_started condition**

```yaml
services:
  app:
    image: my-app
    depends_on:
      redis:
        condition: service_started
```

**Step 4: Break circular dependencies**

Re-architect services to avoid circular dependencies. Use a message queue or service registry pattern.

**Step 5: Add restart policy to dependencies**

```yaml
services:
  db:
    image: postgres:15
    restart: always
```

**Step 6: Use a wait script in the entrypoint**

```bash
#!/bin/bash
while ! nc -z db 5432; do sleep 1; done
exec "$@"
```

## Common Mistakes

- **Using depends_on without healthcheck**: depends_on by default only checks container creation, not readiness.
- **Creating circular dependencies**: Service A depends on B and B depends on A is not resolvable.
- **Not adding restart policies to dependencies**: A single failure of a dependency blocks all dependents forever.
- **Assuming depends_on waits for the service to be ready**: It only waits for the container to start by default.

## Related Pages

- [Docker Compose Healthcheck Error](/tools/docker-compose/docker-compose-healthcheck-error/) -- Healthcheck issues
- [Docker Compose Restart Loop](/tools/docker-compose/docker-compose-restart-loop/) -- Restart loops
- [Docker Compose Network Error](/tools/docker-compose/docker-compose-network-error/) -- Network issues
