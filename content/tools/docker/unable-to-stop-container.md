---
title: "[Solution] Docker unable to stop container"
description: "Fix 'unable to stop container' error. Resolve Docker container stop failures for unresponsive or stuck containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker unable to stop container

Error response from daemon: cannot stop container: <name>

This error occurs when Docker cannot stop a container. The container process may be stuck or the container runtime may be in an inconsistent state.

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
