---
title: "[Solution] Docker Compose network driver incompatible"
description: "Fix 'network driver incompatible' error in Docker Compose. Resolve compose network driver compatibility issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose network driver incompatible

Error: network driver '<driver>' is not supported

This error occurs when the compose file specifies a network driver that is not available on the current Docker host.

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
