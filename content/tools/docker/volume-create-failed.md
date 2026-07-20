---
title: "[Solution] Docker volume create failed"
description: "Fix 'volume create failed' error. Resolve Docker volume creation failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker volume create failed

Error: create <volume>: volume create failed

This error occurs when Docker cannot create a volume. The driver may not be available or the filesystem may have issues.

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
