---
title: "[Solution] Docker Compose interpolation error"
description: "Fix 'interpolation error' in Docker Compose. Resolve compose variable substitution issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose interpolation error

Error: invalid interpolation format for <key>

This error occurs when a compose file uses invalid syntax for variable interpolation.

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
