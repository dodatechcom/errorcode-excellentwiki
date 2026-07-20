---
title: "[Solution] Docker volume driver not available"
description: "Fix 'volume driver not available' error. Resolve Docker volume driver plugin issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker volume driver not available

Error: driver <driver> not available

This error occurs when the volume driver plugin specified for a volume is not installed or not responding.

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
