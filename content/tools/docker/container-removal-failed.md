---
title: "[Solution] Docker Container Removal Failed — Unable to remove filesystem"
description: "Fix Docker container removal failed error. Force remove containers and resolve filesystem issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Unable to remove filesystem / container removal failed

This error occurs when Docker cannot remove a container's filesystem. This often happens with containers that have volumes or are stuck in a bad state.

## Common Causes

- Container has active volume mounts
- Container process still running
- Filesystem lock on container layers
- Docker daemon cannot access storage directory
- Container in restarting state

## How to Fix

### Force Remove Container

```bash
docker rm -f <container>
```

### Stop Then Remove

```bash
docker stop <container>
docker rm <container>
```

### Remove with Volume

```bash
docker rm -v <container>
```

### Remove All Stopped Containers

```bash
docker container prune -f
```

### Check Container Status

```bash
docker ps -a --filter id=<container>
```

### Restart Docker Daemon

```bash
sudo systemctl restart docker
```

### Manual Filesystem Cleanup

```bash
sudo rm -rf /var/lib/docker/overlay2/<container-layer-id>
```

## Examples

```bash
# Example 1: Force remove
docker rm -f my-container

# Example 2: Prune all stopped
docker container prune -f
# Deleted: my-container

# Example 3: Remove with volumes
docker rm -v my-container
# Removes container and anonymous volumes
```

## Related Errors

- [Docker rm force]({{< relref "/tools/docker/docker-rm-force" >}}) — related error
- [Container already exists]({{< relref "/tools/docker/container-already-exists" >}}) — related error
