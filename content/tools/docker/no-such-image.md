---
title: "[Solution] Docker no such image error"
description: "Fix 'No such image' error. Resolve Docker command failures when referencing an image that does not exist locally."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker no such image error

Error: No such image: <image>

This error occurs when Docker cannot find the specified image in the local image store. The image must be pulled or built first.

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
