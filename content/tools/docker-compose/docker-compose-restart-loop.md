---
title: "[Solution] Docker Compose Restart Loop — Fix Container Crash Loop"
description: "Fix Docker Compose container restart loops when services keep crashing and restarting. Debug application errors, check healthcheck configuration, and inspect logs."
---

## What This Error Means

Docker Compose restart loops occur when a container exits immediately after starting and the restart policy brings it back repeatedly. The container cycles between starting, crashing, and restarting.

A typical error:

```
Container is restarting
```

Or from docker compose ps:

```
STATUS: Restarting (1) 2 seconds ago
```

## Why It Happens

Restart loops happen when:

- **Application crashes on startup**: The application throws an error immediately after launch.
- **Missing configuration**: Required environment variables or config files are not present.
- **Port conflict**: The port the container needs is already in use on the host.
- **Dependency not ready**: The service requires a database or upstream service that is not available.
- **Incorrect restart policy**: `always` or `unless-stopped` keeps restarting a crashing container.
- **Healthcheck fails**: The service starts but is immediately marked unhealthy.

## How to Fix It

**Step 1: Remove the restart policy temporarily**

```yaml
services:
  app:
    image: my-app
    restart: "no"
```

Then run:

```bash
docker compose up
```

**Step 2: Check the container logs**

```bash
docker compose logs <service>
docker compose logs --tail=100 <service>
```

**Step 3: Verify environment variables**

```bash
docker compose config
docker compose run --rm <service> env
```

**Step 4: Fix dependency ordering**

```yaml
services:
  app:
    image: my-app
    depends_on:
      db:
        condition: service_healthy
    restart: on-failure
```

**Step 5: Increase start period**

```yaml
services:
  app:
    image: my-app
    healthcheck:
      start_period: 60s
    restart: on-failure:5
```

**Step 6: Use on-failure with max retries**

```yaml
services:
  app:
    image: my-app
    restart: on-failure:5
```

## Common Mistakes

- **Using `restart: always` during development**: Use `on-failure` or `no` for debugging.
- **Not checking logs before assuming the cause**: Always check `docker compose logs` first.
- **Setting depends_on without healthchecks**: depends_on by default only waits for container start, not readiness.
- **Ignoring the exit code**: Different exit codes indicate different problems (137 = OOM, 1 = app error, 139 = segfault).

## Related Pages

- [Docker Compose Healthcheck Error](/tools/docker-compose/docker-compose-healthcheck-error/) -- Healthcheck failures
- [Docker Compose OOM Error](/tools/docker-compose/docker-compose-oom/) -- Memory issues
- [Docker Compose Build Error](/tools/docker-compose/docker-compose-build-error/) -- Build failures
