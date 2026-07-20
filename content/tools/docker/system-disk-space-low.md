---
title: "[Solution] Docker system disk space low"
description: "Fix 'disk space low' error. Resolve Docker storage exhaustion issues impacting container operations."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker system disk space low

Error: write /var/lib/docker/overlay2/<id>: no space left on device

This error occurs when the Docker storage directory runs out of disk space. Containers cannot write data.

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
