---
title: "[Solution] Docker Permission Denied — permission denied while connecting to Docker daemon"
description: "Fix Docker permission denied error. Resolve Cannot connect to the Docker daemon permission issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Permission Denied — permission denied while connecting to Docker daemon socket

This error occurs when the current user does not have permission to access the Docker daemon socket. Docker requires root or docker group membership to communicate with the daemon.

## Common Causes

- User is not in the `docker` group
- Docker socket permissions are incorrect
- Running Docker in rootless mode without proper setup
- Docker daemon is not running

## How to Fix

### Add User to Docker Group

```bash
sudo usermod -aG docker $USER
newgrp docker
```

### Fix Socket Permissions

```bash
sudo chmod 666 /var/run/docker.sock
```

### Run with sudo

```bash
sudo docker <command>
```

### Check Docker Daemon Status

```bash
sudo systemctl status docker
```

### Start Docker Daemon

```bash
sudo systemctl start docker
```

## Examples

```bash
# Example 1: Permission denied on docker command
docker run hello-world
# permission denied while connecting to Docker daemon socket
# Fix: sudo usermod -aG docker $USER && newgrp docker

# Example 2: Docker socket permission issue
ls -la /var/run/docker.sock
# srw-rw---- 1 root docker 0 Jan 1 00:00 /var/run/docker.sock
# Fix: sudo chmod 666 /var/run/docker.sock

# Example 3: Docker daemon not running
sudo systemctl status docker
# Fix: sudo systemctl start docker
```

## Related Errors

- [No Space Left]({{< relref "/tools/docker/no-space" >}}) — disk space exhausted
- [Permission Denied SSH]({{< relref "/tools/git/permission-denied2" >}}) — SSH authentication failure
