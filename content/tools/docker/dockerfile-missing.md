---
title: "[Solution] Docker Dockerfile missing error"
description: "Fix 'Dockerfile missing' error. Resolve Docker build failures when the Dockerfile is not found."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Dockerfile missing error

docker: Error response from daemon: Dockerfile not found

This error occurs when `docker build` cannot find a Dockerfile in the build context.

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
