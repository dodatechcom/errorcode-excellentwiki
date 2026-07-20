---
title: "[Solution] Docker import image failed"
description: "Fix 'docker import failed' error. Resolve Docker image import failures from tarballs."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker import image failed

Error: cannot import from archive

This error occurs when Docker cannot import an image from a tarball. The archive may be corrupted.

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
