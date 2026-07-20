---
title: "[Solution] Docker Swarm lock unavailable"
description: "Fix 'lock unavailable' error in Docker Swarm. Resolve swarm locking and autolock issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm lock unavailable

Error: swarm is locked, use --unlock to unlock

This error occurs when attempting to manage a locked swarm without providing the unlock key.

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
