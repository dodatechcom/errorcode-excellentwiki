---
title: "[Solution] Docker Compose extends error"
description: "Fix 'extends error' in Docker Compose. Resolve compose service inheritance issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose extends error

Error: service <name> extends service <base> which is not defined

This error occurs when a service uses `extends` to inherit from a service that does not exist.

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
