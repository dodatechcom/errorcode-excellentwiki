---
title: "[Solution] Docker unable to restart container"
description: "Fix 'unable to restart container' error. Resolve Docker container restart failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker unable to restart container

Error response from daemon: Cannot restart container <name>

This error occurs when Docker cannot restart a container. This may be due to configuration issues, resource constraints, or runtime problems.

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
