---
title: "[Solution] Docker container name is already in use"
description: "Fix 'container name already in use' error. Resolve Docker container naming conflicts when starting containers with duplicate names."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker container name is already in use

docker: Error response from daemon: Conflict. The container name "/<name>" is already in use by container "<id>".

This error occurs when you try to create a container with a name that is already assigned to an existing container. Container names must be unique on a system.

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
