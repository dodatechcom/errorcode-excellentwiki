---
title: "[Solution] Docker Swarm service not found"
description: "Fix 'service not found' error in Docker Swarm. Resolve swarm service lookup failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm service not found

Error: service <name> not found

This error occurs when a Docker Swarm service command references a service that does not exist in the swarm.

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
