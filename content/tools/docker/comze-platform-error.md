---
title: "[Solution] Docker Compose platform error"
description: "Fix 'platform error' in Docker Compose. Resolve compose multi-platform build and run issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose platform error

Error: image with platform <platform> not found

This error occurs when a compose file specifies a platform that is not available for the image.

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
