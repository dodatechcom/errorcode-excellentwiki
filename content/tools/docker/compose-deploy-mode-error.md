---
title: "[Solution] Docker Compose deploy mode error"
description: "Fix 'deploy mode error' in Docker Compose. Resolve compose deploy section configuration issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose deploy mode error

Error: deploy mode <mode> is not supported

This error occurs when the deploy mode in a compose file is not supported by the current Docker version.

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
