---
title: "[Solution] Docker unable to rename container"
description: "Fix 'unable to rename container' error. Resolve Docker container rename failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker unable to rename container

Error response from daemon: Cannot rename container <name>

This error occurs when Docker cannot rename a container. The new name may already be in use or the container may be in a state that prevents renaming.

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
