---
title: "[Solution] Docker build secrets error"
description: "Fix 'build secrets error' in Docker. Resolve Docker BuildKit secret mounting issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build secrets error

ERROR: failed to solve: secret <name> not found

This error occurs when a Dockerfile references a build secret that is not provided via `--secret`.

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
