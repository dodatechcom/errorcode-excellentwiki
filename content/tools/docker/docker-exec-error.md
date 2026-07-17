---
title: "[Solution] Docker Exec Error — docker exec failed"
description: "Fix Docker exec errors. Resolve issues running commands inside containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["exec", "container", "command", "interactive", "docker"]
weight: 5
---

A Docker exec error occurs when you cannot run commands inside a running container. This can happen if the container is stopped, the command is invalid, or permissions are insufficient.

## Common Causes

- Container is not running (exited or paused)
- The command or executable does not exist in the container
- Insufficient permissions to run the command as the specified user
- Container does not have a shell installed (minimal images like Alpine)
- The container's PID 1 process has exited

## How to Fix

### Check Container Status

```bash
docker ps -a | grep <container>
```

### Start the Container

```bash
docker start <container>
```

### Run as Root

```bash
docker exec -u root <container> <command>
```

### Use sh Instead of bash (minimal images)

```bash
docker exec -it <container> sh
```

### Check Available Executables

```bash
docker exec <container> ls /bin
```

## Examples

```bash
# Example 1: Exec into running container
docker exec -it my-container sh
# Container is not running
# Fix: docker start my-container

# Example 2: Run as root
docker exec -u root my-container apt-get update

# Example 3: Minimal image without bash
docker exec -it alpine-container sh
# Not: docker exec -it alpine-container bash
```

## Related Errors

- [Docker Socket Permission]({{< relref "/tools/docker/docker-socket-permission" >}}) — permission denied on docker.sock
- [Docker Out of Memory]({{< relref "/tools/docker/docker-out-of-memory" >}}) — container OOM killed
