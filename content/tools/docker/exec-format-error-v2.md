---
title: "[Solution] Docker exec format error"
description: "Fix 'exec format error' in Docker. Resolve executable format issues when running commands in containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker exec format error

docker: Error response from daemon: OCI runtime create failed: exec: executable file not found in $PATH

This error occurs when the command you try to execute in a container does not exist or has the wrong architecture.

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
