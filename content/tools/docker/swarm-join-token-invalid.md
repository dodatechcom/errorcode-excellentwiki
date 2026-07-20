---
title: "[Solution] Docker Swarm join token invalid"
description: "Fix 'join token invalid' error in Docker Swarm. Resolve swarm node join failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm join token invalid

Error: join token is invalid

This error occurs when attempting to join a swarm node with an incorrect or expired join token.

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
