---
title: "[Solution] Docker unable to unpause container"
description: "Fix 'unable to unpause container' error. Resolve Docker container unpause failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker unable to unpause container

Error response from daemon: Cannot unpause container <name>

This error occurs when Docker cannot resume a paused container. The container may have been in an unexpected state when paused.

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
