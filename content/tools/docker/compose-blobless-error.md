---
title: "[Solution] Docker Compose blobless build error"
description: "Fix 'blobless build error' in Docker Compose. Resolve compose build issues in CI environments."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose blobless build error

Error: failed to solve: blob mounted from <image> not found

This error occurs when BuildKit tries to mount a blob from an image that is not available.

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
