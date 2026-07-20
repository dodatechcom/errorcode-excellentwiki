---
title: "[Solution] Docker Swarm service update failed"
description: "Fix 'service update failed' error in Docker Swarm. Resolve swarm service update failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm service update failed

Error: service <name> update failed

This error occurs when a swarm service update cannot be applied. The new configuration may be invalid or resources unavailable.

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
