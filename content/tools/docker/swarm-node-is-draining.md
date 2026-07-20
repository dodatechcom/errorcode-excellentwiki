---
title: "[Solution] Docker Swarm node is draining"
description: "Fix 'node is draining' error in Docker Swarm. Resolve swarm operations on nodes in drain state."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm node is draining

Error: node <name> is draining

This error occurs when trying to schedule tasks on a swarm node that is in the draining state.

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
