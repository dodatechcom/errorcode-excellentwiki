---
title: "[Solution] Docker Socket Permission — permission denied on docker.sock"
description: "Fix Docker socket permission denied errors. Resolve docker.sock access issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["socket", "permission", "denied", "docker.sock", "docker"]
weight: 5
---

A Docker socket permission error occurs when a user or container cannot access the Docker daemon socket. This prevents Docker commands from being executed.

## Common Causes

- Current user is not in the `docker` group
- Docker socket has restrictive file permissions
- Running Docker commands as a non-root user without group membership
- Container trying to access host Docker socket without proper volume mount
- Docker daemon socket not exposed

## How to Fix

### Add User to Docker Group

```bash
sudo usermod -aG docker $USER
newgrp docker
```

### Check Socket Permissions

```bash
ls -la /var/run/docker.sock
# srw-rw---- 1 root docker 0 ... /var/run/docker.sock
```

### Fix Socket Permissions Temporarily

```bash
sudo chmod 666 /var/run/docker.sock
```

### Mount Docker Socket in Container

```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock my-image
```

### Verify Group Membership

```bash
groups $USER
```

## Examples

```bash
# Example 1: Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
docker ps

# Example 2: Mount socket for Docker-in-Docker
docker run -v /var/run/docker.sock:/var/run/docker.sock docker:latest docker ps

# Example 3: Check permissions
ls -la /var/run/docker.sock
# Fix: sudo chmod 666 /var/run/docker.sock
```

## Related Errors

- [Docker Volume Error]({{< relref "/tools/docker/docker-volume-error" >}}) — volume mount permission denied
- [Docker Exec Error]({{< relref "/tools/docker/docker-exec-error" >}}) — docker exec failed
