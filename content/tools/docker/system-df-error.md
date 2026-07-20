---
title: "[Solution] Docker system df error"
description: "Fix 'docker system df' error. Resolve Docker disk usage reporting failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker system df error

Error: docker system df failed

This error occurs when Docker cannot report disk usage statistics. The storage driver may be in an inconsistent state.

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
