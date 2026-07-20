---
title: "[Solution] Docker bind mount source missing"
description: "Fix 'bind mount source missing' error. Resolve Docker bind mount failures when the host path does not exist."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker bind mount source missing

docker: Error response from daemon: invalid mount config: bind source path does not exist

This error occurs when the host path specified in a bind mount does not exist.

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
