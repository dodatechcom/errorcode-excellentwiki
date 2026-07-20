---
title: "[Solution] Docker mount denied error"
description: "Fix 'mount denied' error. Resolve Docker volume mount failures due to permission or path issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker mount denied error

docker: Error response from daemon: Mount denied: The source path does not exist.

This error occurs when Docker cannot mount a host directory into a container. The source path may not exist or permissions are insufficient.

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
