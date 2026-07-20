---
title: "[Solution] Docker tag invalid format"
description: "Fix 'invalid tag format' error. Resolve Docker image tagging failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker tag invalid format

Error: invalid reference format: repository name must be lowercase

This error occurs when the image tag or repository name has an invalid format.

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
