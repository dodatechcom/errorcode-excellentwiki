---
title: "[Solution] Linux Docker Permission Denied — Add to docker Group"
description: "Fix Linux 'docker permission denied' errors. Add users to the docker group, fix socket permissions, and resolve Docker access issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: docker — permission denied — add to docker group

The `docker: permission denied` or `Got permission denied while trying to connect to the Docker daemon socket` error means the current user does not have permission to access the Docker daemon. The Docker daemon runs as root and requires either root privileges or membership in the `docker` group to interact with the daemon socket.

## What This Error Means

The Docker daemon (`dockerd`) listens on a Unix socket at `/var/run/docker.sock`. The socket is owned by `root:docker` with permissions `660`. Any user in the `docker` group can read/write to this socket. When a user not in the group runs a `docker` command, the client cannot connect to the socket and returns a permission denied error.

## Common Causes

- User not added to the `docker` group after installation
- Docker socket permissions changed by security policy
- User logged in before Docker was installed (session needs refresh)
- SELinux or AppArmor blocking socket access
- Running in a container or chroot without proper device access
- Docker installed via rootless mode with wrong socket path

## How to Fix

### 1. Add User to docker Group

```bash
# Add current user to docker group
sudo usermod -aG docker $USER

# Apply group change without logging out
newgrp docker

# Verify group membership
groups $USER
```

### 2. Fix Docker Socket Permissions

```bash
# Check current socket permissions
ls -la /var/run/docker.sock

# Expected output:
# srw-rw---- 1 root docker 0 ... /var/run/docker.sock

# Fix if ownership is wrong
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock
```

### 3. Refresh Group Membership

```bash
# If newgrp does not work, start a new session
# Log out and log back in

# Or use su to get a new shell with updated groups
su - $USER

# Verify
id
# uid=1000(user) gid=1000(user) groups=1000(user),999(docker)
```

### 4. Start Docker Daemon

```bash
# If Docker daemon is not running
sudo systemctl status docker
sudo systemctl start docker
sudo systemctl enable docker

# Verify the socket exists
ls -la /var/run/docker.sock
```

### 5. Fix SELinux Blocking Access

```bash
# Check if SELinux is the cause
sudo ausearch -m AVC -ts recent | grep docker

# Allow container management
sudo setsebool -P container_manage_cgroup on

# Check socket context
ls -Z /var/run/docker.sock
```

### 6. Use sudo as Temporary Workaround

```bash
# Run Docker commands with sudo
sudo docker ps

# Create an alias for convenience
echo 'alias docker="sudo docker"' >> ~/.bashrc
source ~/.bashrc
```

### 7. Use Rootless Docker

```bash
# Install rootless Docker for non-root operation
# https://docs.docker.com/engine/security/rootless/

dockerd-rootless-setuptool.sh install

# Set environment
export DOCKER_HOST=unix:///run/user/$(id -u)/docker.sock
```

## Examples

```bash
$ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock

$ id
uid=1000(admin) gid=1000(admin) groups=1000(admin)

$ sudo usermod -aG docker admin
$ newgrp docker

$ id
uid=1000(admin) gid=1000(admin) groups=1000(admin),999(docker)

$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Related Errors

- [Docker permission error]({{< relref "/os/linux/linux-docker-error" >}}) — General Docker permission issues
- [SELinux context error]({{< relref "/os/linux/linux-selinux-context-error" >}}) — SELinux labeling issues
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — General permission issues
