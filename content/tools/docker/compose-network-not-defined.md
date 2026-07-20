---
title: "[Solution] Docker Compose network not defined"
description: "Fix 'network not defined' error in Docker Compose. Resolve compose file issues when referencing undefined networks."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose network not defined

Network '<name>' not found in docker-compose.yml

This error occurs when a service references a network that is not defined in the `networks` section of the compose file.

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
