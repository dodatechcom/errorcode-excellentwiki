---
title: "[Solution] Docker Swarm secret creation failed"
description: "Fix 'secret creation failed' error in Docker Swarm. Resolve swarm secret creation issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm secret creation failed

Error: secret <name> creation failed

This error occurs when Docker Swarm cannot create a secret. The secret data may be too large or the swarm is locked.

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
