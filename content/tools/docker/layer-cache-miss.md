---
title: "[Solution] Docker build layer cache miss"
description: "Fix Docker build cache miss issues. Optimize Docker layer caching for faster builds."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build layer cache miss

CACHED [n/n] RUN <command> (cache miss, skipping)

This warning occurs when Docker cannot use cached layers because the build context or Dockerfile instructions have changed.

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
