---
title: "[Solution] Docker Swarm leader election failed"
description: "Fix 'leader election failed' error in Docker Swarm. Resolve swarm manager leader election issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Swarm leader election failed

Error: leader election failed

This error occurs when the swarm manager nodes cannot elect a leader. This usually indicates a networking or consensus issue.

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
