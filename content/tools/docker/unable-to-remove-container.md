---
title: "[Solution] Docker unable to remove container"
description: "Fix 'unable to remove container' error. Resolve Docker container removal failures for running or stuck containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker unable to remove container

docker: Error response from daemon: You cannot remove a running container.

This error occurs when you try to remove a container that is currently running. Stop the container first before removing it.

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
