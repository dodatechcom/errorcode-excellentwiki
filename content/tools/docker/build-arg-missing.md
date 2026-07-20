---
title: "[Solution] Docker build ARG missing"
description: "Fix 'ARG missing' error in Docker build. Resolve Dockerfile build argument issues when required ARGs are not provided."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build ARG missing

Error: missing build argument <name>

This error occurs when a Dockerfile uses an ARG that must be provided via `--build-arg` and no default value is set.

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
