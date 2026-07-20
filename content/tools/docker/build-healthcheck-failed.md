---
title: "[Solution] Docker build HEALTHCHECK instruction error"
description: "Fix 'HEALTHCHECK instruction error' in Docker build. Resolve Dockerfile HEALTHCHECK configuration issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build HEALTHCHECK instruction error

Error: HEALTHCHECK requires at least one argument

This error occurs when the HEALTHCHECK instruction is missing required arguments like the test command.

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
