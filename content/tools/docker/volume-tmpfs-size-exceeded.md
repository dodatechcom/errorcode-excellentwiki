---
title: "[Solution] Docker tmpfs size exceeded"
description: "Fix 'tmpfs size exceeded' error. Resolve Docker tmpfs mount size limit issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker tmpfs size exceeded

Error: tmpfs: size limit exceeded

This error occurs when a tmpfs mount in a container exceeds the configured size limit.

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
