---
title: "[Solution] Docker Compose environment variable missing"
description: "Fix 'environment variable missing' error in Docker Compose. Resolve missing required env vars in compose configuration."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose environment variable missing

Warning: <var> is not set, using default

This error occurs when a compose file references an environment variable from the host shell that is not set.

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
