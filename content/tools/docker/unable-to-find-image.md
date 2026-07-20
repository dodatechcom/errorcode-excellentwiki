---
title: "[Solution] Docker unable to find image"
description: "Fix 'Unable to find image' error. Resolve Docker image pull failures when an image is not found locally or on the registry."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker unable to find image

Unable to find image '<image>:<tag>' locally

This error occurs when Docker cannot find the specified image locally and tries to pull it from the registry. If the pull also fails, the image does not exist.

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
