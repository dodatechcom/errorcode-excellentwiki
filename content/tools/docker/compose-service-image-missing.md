---
title: "[Solution] Docker Compose service image missing"
description: "Fix 'image missing' error in Docker Compose. Resolve compose service failures when the specified image cannot be pulled."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose service image missing

Error: image <name> not found

This error occurs when a compose service specifies an image that does not exist or cannot be pulled.

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
