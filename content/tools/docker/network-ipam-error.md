---
title: "[Solution] Docker network IPAM error"
description: "Fix 'IPAM error' in Docker networks. Resolve Docker IP address management issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker network IPAM error

Error: pool <subnet> is too small

This error occurs when the IP address pool for a Docker network is too small for the required endpoints.

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
