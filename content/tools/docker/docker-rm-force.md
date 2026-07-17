---
title: "[Solution] Docker cannot remove container: resource is busy"
description: "Fix Docker cannot remove container resource busy error. Resolve stuck containers and volume mount conflicts."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker cannot remove container: resource is busy

Docker cannot remove a container because it is still in use by a running process, mounted volume, or network namespace. The container is actively referenced by another resource.

## Common Causes

- Container is still running when you try to remove it
- Volume mounted by the container is in use by another process
- Container is referenced by a stopped container's --volumes-from
- Docker network still has active endpoints attached to the container

## How to Fix

### Stop Container Before Removing

```bash
docker stop <container-name>
docker rm <container-name>
```

### Force Remove Running Container

```bash
docker rm -f <container-name>
# Stops and removes in one step
```

### List Containers Using a Volume

```bash
docker ps -a --filter volume=<volume-name>
docker volume inspect <volume-name>
```

### Remove All Stopped Containers

```bash
docker container prune
# Or remove everything unused
docker system prune -a --volumes
```

### Find Process Using the Resource

```bash
lsof +D /var/lib/docker/volumes/<volume-name>/_data
# Kill the process using the volume
fuser -k /var/lib/docker/volumes/<volume-name>/_data
```

## Examples

```bash
# Example 1: Running container
docker rm my-container
# Error: You cannot remove a running container
# Fix: docker stop my-container && docker rm my-container

# Example 2: Volume in use
docker rm -v my-container
# Error: container abc123 is using volume data-vol
# Fix: stop all containers using the volume first

# Example 3: Device or resource busy
docker rm my-container
# Error: remove my-container: device or resource busy
# Fix: docker rm -f my-container
# Or find and kill the process: lsof +D /var/lib/docker/...
```

## Related Errors

- [Docker Socket Error]({{< relref "/tools/docker/docker-socket" >}}) — cannot connect to Docker daemon
- [No Space Left]({{< relref "/tools/docker/no-space" >}}) — disk space exhausted
- [Container Exited]({{< relref "/tools/docker/container-exited" >}}) — unexpected container exit
