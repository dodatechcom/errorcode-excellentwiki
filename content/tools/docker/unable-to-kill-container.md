---
title: "[Solution] Docker unable to kill container"
description: "Fix 'unable to kill container' error. Resolve Docker container kill failures for unresponsive processes."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker unable to kill container

Error response from daemon: Cannot kill container <name>

This error occurs when Docker cannot send a kill signal to the container. The container process may be in an uninterruptible state.

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
