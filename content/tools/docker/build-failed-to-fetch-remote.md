---
title: "[Solution] Docker build failed to fetch remote"
description: "Fix 'failed to fetch remote' error. Resolve Docker build failures when downloading remote dependencies."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build failed to fetch remote

ERROR: failed to fetch remote <url>

This error occurs when Docker BuildKit cannot download a remote resource (like a Git repository or tarball) specified in the Dockerfile.

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
