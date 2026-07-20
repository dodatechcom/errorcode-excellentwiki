---
title: "[Solution] Docker no such network error"
description: "Fix 'No such network' error. Resolve Docker network command failures when referencing a non-existent network."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker no such network error

Error: No such network: <name>

This error occurs when you reference a Docker network that does not exist. Network names must match exactly.

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
