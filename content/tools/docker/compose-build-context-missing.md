---
title: "[Solution] Docker Compose build context missing"
description: "Fix 'build context missing' error in Docker Compose. Resolve compose build failures when the build directory does not exist."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose build context missing

ERROR: build context directory '<path>' does not exist

This error occurs when the `build` context path in a compose service does not exist on the filesystem.

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
