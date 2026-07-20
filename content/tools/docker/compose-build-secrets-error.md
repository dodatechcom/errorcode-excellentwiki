---
title: "[Solution] Docker Compose build secrets error"
description: "Fix 'build secrets error' in Docker Compose. Resolve compose file build secret configuration issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose build secrets error

Error: secret <name>: file not found

This error occurs when a build secret specified in a compose file references a file that does not exist.

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
