---
title: "[Solution] Docker: Permission Denied on docker.sock"
description: "Fix 'permission denied' on docker.sock on Linux. Resolve Docker socket access issues for non-root users and CI/CD pipelines."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["docker", "docker.sock", "permission", "socket", "unix", "daemon"]
weight: 5
---

# Docker: Permission Denied on docker.sock

The `permission denied on docker.sock` error occurs when a user or process tries to access the Docker daemon socket without the required permissions. The error reads:

> "Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock"

## What This Error Means

Docker daemon listens on a Unix socket file (`/var/run/docker.sock`) for API requests. By default, this socket is owned by `root:docker` with `660` permissions. Any user not in the `docker` group cannot connect to the daemon. CI/CD tools, scripts, and containerized Docker clients all need socket access.

## Common Causes

- User not in the `docker` group
- Socket permissions changed (e.g., by a security policy)
- Running Docker inside a container without mounting the socket
- SELinux blocking socket access
- Socket file missing (Docker daemon not running)

## How to Fix

### Add User to Docker Group

```bash
sudo usermod -aG docker $USER
newgrp docker
groups $USER
```

### Fix Socket Permissions

```bash
# Check socket permissions
ls -la /var/run/docker.sock

# Fix ownership
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock
```

### Mount Docker Socket in Containers

```bash
# For Docker-in-Docker scenarios
docker run -v /var/run/docker.sock:/var/run/docker.sock docker:latest docker ps
```

### Fix SELinux for Socket Access

```bash
# Check SELinux context
ls -Z /var/run/docker.sock

# Allow container access to socket
sudo setsebool -P container_manage_cgroup on
```

### Use TCP Socket Instead

```bash
# Configure Docker daemon to listen on TCP
# /etc/docker/daemon.json
{
  "hosts": ["unix:///var/run/docker.sock", "tcp://0.0.0.0:2375"]
}

sudo systemctl restart docker
```

### Verify Docker Is Running

```bash
sudo systemctl status docker
sudo journalctl -u docker --since "5 minutes ago"
```

## Related Errors

- [Docker Volume Permission Denied]({{< relref "/os/linux/linux-docker-volume-error" >}}) — Volume mount permission issues
- [Docker Network Bridge Error]({{< relref "/os/linux/linux-docker-network-error" >}}) — Network configuration issues
- [Docker Compose Network Error]({{< relref "/os/linux/linux-docker-compose-error" >}}) — Compose network creation failures
