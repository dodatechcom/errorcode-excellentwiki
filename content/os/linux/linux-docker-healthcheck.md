---
title: "[Solution] Docker Healthcheck Failed — Container Unhealthy"
description: "Fix Docker container healthcheck failed errors on Linux. Resolve unhealthy container status, health probe failures, and container restart loops."
platforms: ["linux"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 5
---

# Docker Healthcheck Failed — Container Unhealthy

A Docker healthcheck failed error occurs when a container's configured health check fails repeatedly, causing the container to be marked as "unhealthy." The status shows:

> "unhealthy" in `docker ps` HEALTH column

Or:

> "Health: unhealthy" in `docker inspect`

## What This Error Means

Docker health checks periodically run a command inside or against the container to verify it is functioning correctly. If the check fails a configured number of times (`retries`), Docker marks the container as "unhealthy." This is informational by default — Docker does not restart unhealthy containers unless you use `depends_on` with `condition: service_healthy` or a restart policy.

## Common Causes

- Application inside container is not responding (deadlock, crash, resource exhaustion)
- Health check command is incorrect (wrong path, wrong binary)
- Health check interval too short for slow-starting applications
- Network issue preventing health check from reaching the container
- Container running out of memory or CPU
- Health check endpoint (e.g., `/health`) returning non-200 status

## How to Fix

### Check Container Health Status

```bash
# View health details
docker inspect --format='{{json .State.Health}}' <container> | jq

# View recent health check logs
docker inspect --format='{{range .State.Health.Log}}{{.Output}}{{end}}' <container>
```

### Fix Health Check Command

```dockerfile
# Example: correct health check for a web server
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Example: for a database
HEALTHCHECK --interval=10s --timeout=5s --start-period=60s --retries=5 \
  CMD pg_isready -U postgres || exit 1
```

### Increase Start Period

Slow-starting applications need a longer `start-period`:

```bash
# Start period allows container to initialize before health checks begin
docker run --health-cmd="curl -f http://localhost/health || exit 1" \
  --health-interval=30s \
  --health-timeout=10s \
  --health-start-period=60s \
  --health-retries=5 \
  myimage
```

### Check Container Logs

```bash
docker logs --tail 50 <container>

# Check for OOM kills
docker inspect <container> | grep -i oom

# Check resource usage
docker stats --no-stream <container>
```

### Disable Health Check Temporarily

```bash
# Remove health check
docker update --no-healthcheck <container>
```

## Related Errors

- [Docker Container OOM Killed]({{< relref "/os/linux/linux-docker-out-of-memory" >}}) — Container memory issues
- [Docker Exec Error]({{< relref "/os/linux/linux-docker-exec-error" >}}) — Container exec failures
- [k8s CrashLoopBackOff]({{< relref "/os/linux/linux-k8s-crashloop" >}}) — Kubernetes pod crash loops
