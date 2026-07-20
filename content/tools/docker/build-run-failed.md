---
title: "[Solution] Docker build RUN command failed"
description: "Fix 'RUN failed' error. Resolve Docker build failures when a RUN command in the Dockerfile exits with a non-zero status."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build RUN command failed

ERROR: failed to solve: process "/bin/sh -c <command>" did not complete successfully: exit code: <n>

This error occurs when a RUN instruction in the Dockerfile fails. The command returned a non-zero exit code.

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
