---
title: "[Solution] Docker unable to pause container"
description: "Fix 'unable to pause container' error. Resolve Docker container pause failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker unable to pause container

Error response from daemon: Cannot pause container <name>

This error occurs when Docker cannot pause the container processes. Not all container runtimes support the pause feature.

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
