---
title: "[Solution] Docker Container Error — container not running"
description: "Fix Docker 'container not running' error. Diagnose why containers stop and restart them reliably."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "docker"
tags: ["docker", "containers", "containers", "restart", "daemon"]
severity: "error"
weight: 5
---

# ERROR: container not running

## Error Message

```
Error: container myapp is not running

Error response from daemon: Container abc123def456 is not running
```

This error occurs when you try to interact with a container that has exited or been stopped. Commands like `docker exec`, `docker logs`, and `docker cp` require the target container to be in a running state.

## Common Causes

- The container exited because its main process completed or crashed
- The container was manually stopped with `docker stop`
- The container hit an OOM (Out of Memory) limit and was killed
- A health check failure triggered an automatic restart that also failed
- The container depends on another service that is not running

## Solutions

### Solution 1: Start the Container

The simplest fix is to restart the stopped container. Check its status first to understand why it stopped.

```bash
docker ps -a
docker start myapp
docker ps
```

### Solution 2: Check Logs for the Crash Reason

Examine container logs to find the root cause of the crash. The exit code can narrow down whether it was an OOM kill or application error.

```bash
docker logs myapp --tail 50
docker inspect myapp --format '{{.State.ExitCode}}'
# Exit code 137 = OOM killed
# Exit code 1 = application error
```

### Solution 3: Recreate the Container with Resource Limits

If OOM is the cause, increase the memory limit or optimize the application. Running with `--restart unless-stopped` ensures the container recovers from transient failures.

```bash
docker rm myapp
docker run -d --name myapp --memory 512m --restart unless-stopped myimage
```

### Solution 4: Use a Dependency-Aware Startup

If the container depends on a database or other service, use `depends_on` in Compose or a wait script to ensure dependencies are ready before the application starts.

```yaml
services:
  api:
    image: myapp:latest
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
      interval: 5s
```

```bash
docker compose up -d
```

## Prevention Tips

- Set `restart: unless-stopped` on critical services in your Compose file
- Configure memory limits and health checks for all production containers
- Monitor container exit codes with a logging stack like `docker events`
- Use `depends_on` with health conditions instead of simple ordering

## Related Errors

- [Container Exited]({{< relref "/tools/docker/container-exited" >}}) — container exit code errors
- [Docker Out of Memory]({{< relref "/tools/docker/docker-out-of-memory" >}}) — OOM kill events
