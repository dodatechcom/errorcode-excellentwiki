---
title: "[Solution] Docker no such container error"
description: "Fix 'No such container' error. Resolve Docker command failures when referencing a container that does not exist."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker no such container error

Error: No such container: <name>

This error occurs when you reference a container name or ID that does not exist. The container may have been removed or the name is incorrect.

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
