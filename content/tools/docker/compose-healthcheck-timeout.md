---
title: "[Solution] Docker Compose healthcheck timeout"
description: "Fix 'healthcheck timeout' error in Docker Compose. Resolve compose health check timeout failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose healthcheck timeout

Error: Health check exceeded timeout of <n> seconds

This error occurs when a container's health check command takes longer than the configured timeout.

## How to Fix

### Check Docker Status

```bash
docker info
docker system df
```

### View Logs

```bash
docker logs <container>
docker events --since 5m
```

### Restart Docker

```bash
sudo systemctl restart docker
```

## Related Errors

- [Container Not Running]({{< relref "/tools/docker/container-is-not-running" >}}) — container stopped
- [Image Not Found]({{< relref "/tools/docker/docker-image-not-found" >}}) — image missing
