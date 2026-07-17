---
title: "[Solution] Linux docker Permission Denied — Fix"
description: "Fix Linux 'docker: permission denied' errors. Add users to docker group, fix socket permissions, and resolve Docker access issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: docker: permission denied

The `docker: permission denied` or `Got permission denied while trying to connect to the Docker daemon socket` error means the current user does not have permission to access the Docker daemon. Docker requires either root privileges or membership in the `docker` group to communicate with the daemon via the Unix socket.

## What This Error Means

The Docker daemon (`dockerd`) runs as root and listens on a Unix socket at `/var/run/docker.sock`. By default, only root can access this socket. When a non-root user runs `docker` commands, the Docker client tries to connect to this socket and gets denied. The fix is to add the user to the `docker` group, which has read/write access to the socket.

## Common Causes

- User not added to the `docker` group
- Docker socket permissions changed
- Docker daemon not running
- Running Docker in rootless mode incorrectly
- SELinux blocking Docker socket access
- Docker installed but daemon not started

## How to Fix

### 1. Add User to docker Group

```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Log out and back in for group change to take effect
# Or use newgrp to apply immediately
newgrp docker

# Verify
groups $USER
```

### 2. Fix Docker Socket Permissions

```bash
# Check socket permissions
ls -la /var/run/docker.sock

# Fix permissions (temporary fix)
sudo chmod 666 /var/run/docker.sock

# Or change group ownership
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock
```

### 3. Start Docker Daemon

```bash
# Check Docker status
sudo systemctl status docker

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Verify Docker is running
docker info
```

### 4. Verify Docker Installation

```bash
# Check Docker version
docker --version

# Check if Docker is installed properly
sudo which docker
sudo which dockerd

# Check Docker daemon logs
sudo journalctl -u docker --since "10 minutes ago"
```

### 5. Fix SELinux Issues (RHEL/CentOS/Fedora)

```bash
# Check if SELinux is blocking Docker
sudo ausearch -m AVC -ts recent | grep docker

# Set SELinux boolean for container management
sudo setsebool -P container_manage_cgroup on

# Check Docker socket context
ls -Z /var/run/docker.sock
```

### 6. Use Rootless Docker

For running Docker without root:

```bash
# Install rootless Docker
dockerd-rootless-setuptool.sh install

# Set environment variables
export DOCKER_HOST=unix:///run/user/$(id -u)/docker.sock

# Or use systemd user service
systemctl --user start docker
```

### 7. Use sudo Temporarily

```bash
# Run Docker commands with sudo
sudo docker run hello-world

# Or create an alias
echo 'alias docker="sudo docker"' >> ~/.bashrc
source ~/.bashrc
```

## Examples

```bash
$ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock:
Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied

$ sudo usermod -aG docker $USER
$ newgrp docker
$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

```bash
$ docker info
Cannot connect to the Docker daemon at unix:///var/run/docker.sock.
Is the docker daemon running?

$ sudo systemctl status docker
● docker.service - Docker Application Container Engine
     Active: inactive (dead)

$ sudo systemctl start docker
$ docker info
Server Version: 24.0.7
```

## Related Errors

- [podman namespace error]({{< relref "/os/linux/linux-podman-error" >}}) — Podman container issues
- [lxc container error]({{< relref "/os/linux/linux-lxc-error" >}}) — LXC container issues
- [Permission denied]({{< relref "/os/linux/connection-refused7" >}}) — General permission issues
