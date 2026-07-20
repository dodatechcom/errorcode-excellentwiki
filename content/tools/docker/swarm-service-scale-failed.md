---
title: "[Solution] Docker Swarm service scale failed"
description: "Fix 'scale failed' error in Docker Swarm. Resolve swarm service scaling failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm service scale failed

Error: service <name> scale failed: resource constraints

This error occurs when swarm cannot scale a service to the desired number of replicas due to resource limits.

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
