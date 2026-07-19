---
title: "[Solution] Docker Permission Denied — Got permission denied while trying to connect"
description: "Fix Docker permission denied error when connecting to Docker daemon. Resolve docker.sock access issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# permission denied while trying to connect to the Docker daemon socket

This error occurs when your user does not have permission to access the Docker daemon socket. It is the most common Docker permission issue on Linux systems.

## Common Causes

- Current user is not in the `docker` group
- Docker socket has restrictive permissions
- Running as a non-root user without proper group membership
- Docker group changes not yet applied (need logout/login)

## How to Fix

### Add User to Docker Group

```bash
sudo usermod -aG docker $USER
newgrp docker
```

You may need to log out and back in for group changes to take effect.

### Temporary Fix: Use sudo

```bash
sudo docker ps
```

### Check Current User Groups

```bash
groups $USER
# Should include "docker"
```

### Fix Socket Permissions

```bash
sudo chmod 666 /var/run/docker.sock
```

### Verify Socket Ownership

```bash
ls -la /var/run/docker.sock
# srw-rw---- 1 root docker ...
```

## Examples

```bash
# Example 1: Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
docker ps

# Example 2: Check groups
groups $USER
# admin1 : admin1 docker

# Example 3: Fix after fresh install
sudo usermod -aG docker $USER
# Log out and log back in
docker run hello-world
```

## Related Errors

- [Socket permission denied]({{< relref "/tools/docker/docker-socket-permission" >}}) — related error
- [Cannot connect to daemon]({{< relref "/tools/docker/cannot-connect-to-docker-daemon" >}}) — related error
