---
title: "[Solution] Docker Compose service not found"
description: "Fix 'service not found' error in Docker Compose. Resolve compose file parsing issues when referencing undefined services."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose service not found

Service '<name>' not found in docker-compose.yml

This error occurs when a docker-compose command references a service that is not defined in the compose file.

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
