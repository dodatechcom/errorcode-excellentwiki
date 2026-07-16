---
title: "[Solution] Docker Cannot connect to the Docker daemon at unix:///var/run/docker.sock"
description: "Fix Docker daemon socket connection errors. Resolve Docker daemon not running and permission issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["docker-socket", "daemon", "permission", "unix-socket", "connection"]
weight: 5
---

# Docker Cannot connect to the Docker daemon at unix:///var/run/docker.sock

This error means the Docker CLI cannot communicate with the Docker daemon. The daemon is either not running, not accessible, or your user lacks permission to access the socket.

## Common Causes

- Docker daemon service is not running
- Current user is not in the docker group (permission denied)
- Docker socket file does not exist or has wrong permissions
- Remote Docker host misconfiguration

## How to Fix

### Start the Docker Daemon

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Check Docker Daemon Status

```bash
sudo systemctl status docker
# If inactive: sudo systemctl start docker
```

### Add User to Docker Group

```bash
sudo usermod -aG docker $USER
# Log out and log back in for group changes to take effect
newgrp docker
```

### Check Socket Permissions

```bash
ls -la /var/run/docker.sock
# srw-rw---- 1 root docker 0 ... /var/run/docker.sock
# Your user must be in the 'docker' group
```

### Start Docker Desktop (macOS/Windows)

```bash
# macOS
open -a Docker

# Or restart Docker Desktop from the system tray
```

## Examples

```bash
# Example 1: Daemon not running
docker ps
# Cannot connect to the Docker daemon at unix:///var/run/docker.sock
# Fix: sudo systemctl start docker

# Example 2: Permission denied
docker ps
# permission denied while trying to connect to the Docker daemon socket
# Fix: sudo usermod -aG docker $USER && newgrp docker

# Example 3: Socket missing
ls /var/run/docker.sock
# No such file or directory
# Fix: sudo systemctl restart docker
```

## Related Errors

- [Docker Desktop Error]({{< relref "/tools/docker/docker-desktop-error" >}}) — WSL2 / VM errors
- [Docker Secrets Error]({{< relref "/tools/docker/docker-secrets" >}}) — permission denied
- [Permission Denied]({{< relref "/tools/docker/permission-denied3" >}}) — Docker permission issues
