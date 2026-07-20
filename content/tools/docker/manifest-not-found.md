---
title: "[Solution] Docker manifest not found"
description: "Fix 'manifest not found' error. Resolve Docker pull failures when an image manifest does not exist in the registry."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker manifest not found

manifest for <image>:<tag> not found: manifest unknown

This error occurs when the specified image tag does not exist in the registry. The image may have been deleted or the tag is incorrect.

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
