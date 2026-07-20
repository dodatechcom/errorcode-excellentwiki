---
title: "[Solution] Docker Swarm node is down"
description: "Fix 'node is down' error in Docker Swarm. Resolve swarm operations on unreachable nodes."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm node is down

Error: node <name> is down

This error occurs when attempting to operate on a swarm node that is unreachable or has stopped communicating.

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
