---
title: "[Solution] Docker Swarm node already part of swarm"
description: "Fix 'node already part of swarm' error. Resolve swarm node join failures when the node is already in a cluster."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm node already part of swarm

Error: This node is already part of a swarm

This error occurs when trying to join a node to a swarm that is already part of a cluster.

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
