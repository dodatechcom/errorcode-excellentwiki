---
title: "[Solution] Docker NFS volume mount failed"
description: "Fix 'NFS volume mount failed' error. Resolve Docker NFS volume mounting issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker NFS volume mount failed

Error: mount.NFS: connection timed out

This error occurs when Docker cannot mount an NFS volume. The NFS server may be unreachable or the export path may be incorrect.

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
