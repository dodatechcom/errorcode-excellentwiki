---
title: "[Solution] Docker Compose command not found"
description: "Fix 'command not found' error in Docker Compose. Resolve compose command execution failures inside containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose command not found

Error: <command> not found

This error occurs when the command specified in a compose service's `command` field does not exist in the container image.

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
