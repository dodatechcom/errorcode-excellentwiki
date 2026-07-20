---
title: "[Solution] Docker unknown blob error"
description: "Fix 'unknown blob' error. Resolve Docker registry layer download failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker unknown blob error

Error: unknown blob

This error occurs when Docker tries to download a layer that does not exist in the registry. The image may be corrupted.

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
