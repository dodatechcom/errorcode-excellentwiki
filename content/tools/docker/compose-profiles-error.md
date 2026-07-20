---
title: "[Solution] Docker Compose profiles error"
description: "Fix 'profiles error' in Docker Compose. Resolve compose service profile matching issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose profiles error

Error: service <name> has no matching profile

This error occurs when a compose command does not activate the profiles needed by certain services.

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
