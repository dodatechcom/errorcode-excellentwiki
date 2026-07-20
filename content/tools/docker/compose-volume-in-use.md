---
title: "[Solution] Docker Compose volume already in use"
description: "Fix 'volume already in use' error in Docker Compose. Resolve volume conflicts between compose services."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose volume already in use

Error: error while mounting volume: volume is in use

This error occurs when a Docker volume specified in the compose file is already mounted by another container.

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
