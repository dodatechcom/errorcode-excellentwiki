---
title: "[Solution] Docker Compose Healthcheck Error — Fix Service Unhealthy"
description: "Fix Docker Compose healthcheck errors when services are marked unhealthy. Debug healthcheck commands, tune intervals, and resolve application startup issues."
---

## What This Error Means

Docker Compose healthcheck errors occur when a container's health check command exits with a non-zero status. The service is marked as unhealthy and dependent services may refuse to start.

A typical error:

```
ERROR: Service 'db' is unhealthy
```

Or from docker ps:

```
CONTAINER STATUS: unhealthy
```

## Why It Happens

Healthcheck failures happen when:

- **Healthcheck command fails**: The command inside the container returns a non-zero exit code.
- **Application not ready**: The service needs more time to start than the healthcheck permits.
- **Wrong healthcheck command**: The command does not accurately reflect service readiness.
- **Start interval too short**: The check fires before the application has finished booting.
- **Resource constraints**: The container lacks CPU or memory to respond to health checks.
- **Port not listening**: The application port is not yet open when the check runs.

## How to Fix It

**Step 1: Check the container health status**

```bash
docker ps --filter "health=unhealthy"
docker inspect --format='{{json .State.Health}}' <container>
```

**Step 2: View healthcheck logs**

```bash
docker inspect --format='{{range .State.Health.Log}}{{.Output}}{{end}}' <container>
```

**Step 3: Adjust healthcheck parameters**

```yaml
services:
  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
```

**Step 4: Use a custom healthcheck script**

```yaml
services:
  app:
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:3000/health || exit 1"]
      interval: 15s
      timeout: 5s
      retries: 3
      start_period: 60s
```

**Step 5: Test the healthcheck command manually**

```bash
docker compose exec <service> pg_isready -U postgres
docker compose exec <service> curl -f http://localhost:3000/health
```

**Step 6: Increase start_period for slow-starting services**

```yaml
services:
  app:
    healthcheck:
      start_period: 120s
```

## Common Mistakes

- **Setting start_period too low**: The healthcheck fires during the start_period and causes premature failures.
- **Using curl without -f flag**: curl exits with 0 even for 404 responses without -f.
- **Not checking if the healthcheck tool exists in the container**: Use `CMD-SHELL` and verify tools are installed.
- **Ignoring the healthcheck log output**: The log shows exactly why the check failed.

## Related Pages

- [Docker Compose Build Error](/tools/docker-compose/docker-compose-build-error/) -- Image build failures
- [Docker Compose Restart Loop](/tools/docker-compose/docker-compose-restart-loop/) -- Container crash loops
- [Kubectl Pod Pending](/tools/kubectl/kubectl-pod-pending/) -- Pod scheduling issues
