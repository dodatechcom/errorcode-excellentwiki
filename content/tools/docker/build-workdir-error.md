---
title: "[Solution] Docker build WORKDIR error"
description: "Fix 'WORKDIR error' in Docker build. Resolve Dockerfile WORKDIR instruction failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build WORKDIR error

Error: WORKDIR cannot be empty

This error occurs when the WORKDIR instruction in the Dockerfile has an empty or invalid path.

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
