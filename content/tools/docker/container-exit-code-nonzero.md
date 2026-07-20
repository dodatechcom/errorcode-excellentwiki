---
title: "[Solution] Docker container exit code non-zero"
description: "Fix 'container exit code non-zero' error. Debug Docker containers that exit with error codes."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker container exit code non-zero

docker: Error response from daemon: container <name> exited with code <n>

This error occurs when the main process inside a container exits with a non-zero exit code, indicating a failure.

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
