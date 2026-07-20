---
title: "[Solution] Docker volume remove failed"
description: "Fix 'volume remove failed' error. Resolve Docker volume removal failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker volume remove failed

Error: remove <volume>: volume is in use

This error occurs when trying to remove a Docker volume that is still in use by one or more containers.

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
