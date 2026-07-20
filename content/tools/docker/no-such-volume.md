---
title: "[Solution] Docker no such volume error"
description: "Fix 'No such volume' error. Resolve Docker volume command failures when referencing a non-existent volume."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker no such volume error

Error: No such volume: <name>

This error occurs when you reference a Docker volume that does not exist. The volume must be created first with `docker volume create`.

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
