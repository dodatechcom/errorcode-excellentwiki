---
title: "[Solution] Docker build SSH forwarding error"
description: "Fix 'SSH forwarding error' in Docker build. Resolve Docker BuildKit SSH agent forwarding issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build SSH forwarding error

ERROR: failed to solve: ssh key not found

This error occurs when a Dockerfile references an SSH mount but the SSH agent does not have the required key.

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
