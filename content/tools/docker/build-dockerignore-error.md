---
title: "[Solution] Docker build .dockerignore error"
description: "Fix '.dockerignore error' in Docker build. Resolve issues where .dockerignore patterns exclude required files."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build .dockerignore error

COPY failed: file not found in build context

This error occurs when .dockerignore patterns exclude files needed for the build.

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
