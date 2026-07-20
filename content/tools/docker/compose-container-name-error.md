---
title: "[Solution] Docker Compose container name conflict"
description: "Fix 'container name conflict' error in Docker Compose. Resolve compose naming collisions."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose container name conflict

Error: container name already in use

This error occurs when a compose service's `container_name` conflicts with an existing container.

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
