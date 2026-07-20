---
title: "[Solution] Docker Compose dependency cycle"
description: "Fix 'dependency cycle' error in Docker Compose. Resolve circular depends_on relationships between services."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose dependency cycle

Error: dependency cycle detected in docker-compose.yml

This error occurs when services have circular dependencies through the `depends_on` configuration.

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
