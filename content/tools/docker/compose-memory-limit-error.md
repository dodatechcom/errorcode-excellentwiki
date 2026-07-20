---
title: "[Solution] Docker Compose memory limit error"
description: "Fix 'memory limit error' in Docker Compose. Resolve compose memory reservation configuration issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose memory limit error

Error: invalid memory limit: <value>

This error occurs when the memory limit specified in a compose file has an invalid value.

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
