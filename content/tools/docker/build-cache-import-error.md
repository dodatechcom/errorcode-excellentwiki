---
title: "[Solution] Docker build cache import error"
description: "Fix 'cache import error' in Docker build. Resolve BuildKit cache import failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build cache import error

ERROR: failed to solve: cache import from <ref> failed

This error occurs when Docker BuildKit cannot import a cache from an external source.

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
