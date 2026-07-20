---
title: "[Solution] Docker port mapping failed"
description: "Fix 'port mapping failed' error. Resolve Docker network port mapping and publishing issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker port mapping failed

Error response from daemon: driver failed programming external connectivity

This error occurs when Docker cannot set up port forwarding between the host and container.

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
