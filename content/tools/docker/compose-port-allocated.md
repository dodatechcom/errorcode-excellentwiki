---
title: "[Solution] Docker Compose port already allocated"
description: "Fix 'port already allocated' error in Docker Compose. Resolve compose port conflicts when ports are already in use."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose port already allocated

Error: starting container: Ports are not available: listen tcp 0.0.0.0:8080: bind: address already in use

This error occurs when a port specified in the compose file is already in use on the host machine.

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
