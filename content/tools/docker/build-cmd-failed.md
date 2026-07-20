---
title: "[Solution] Docker build CMD instruction error"
description: "Fix 'CMD instruction error' in Docker build. Resolve Dockerfile CMD or ENTRYPOINT configuration issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build CMD instruction error

Error: docker: Error response from daemon: invalid CMD instruction.

This error occurs when the CMD instruction in the Dockerfile has an invalid format or references a missing executable.

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
