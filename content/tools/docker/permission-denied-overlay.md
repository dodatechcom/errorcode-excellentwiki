---
title: "[Solution] Docker Permission Denied Overlay — permission denied while trying to connect to Docker daemon"
description: "Fix Docker overlay permission denied error. Resolve overlay2 storage driver access issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

# permission denied while trying to connect to the Docker daemon socket at /var/run/docker.sock

This specific permission denied error often relates to the overlay2 storage driver or volume mount permissions. The Docker daemon cannot access the filesystem layer it needs.

## Common Causes

- Overlay mount directory has wrong ownership
- SELinux or AppArmor blocking access
- Volume mount with incorrect permissions
- Docker data directory permissions corrupted

## How to Fix

### Reset Docker Data Directory Permissions

```bash
sudo chown -R root:root /var/lib/docker
sudo chmod -R 700 /var/lib/docker
```

### Check SELinux Status

```bash
getenforce
# If Enforcing, try:
sudo setsebool -P container_manage_cgroup on
```

### Fix Volume Permissions

```bash
docker run -v /path/on/host:/path/in/container --user $(id -u):$(id -g) my-image
```

### Restart Docker After Permission Changes

```bash
sudo systemctl restart docker
```

## Examples

```bash
# Example 1: Fix overlay permissions
sudo chown -R root:root /var/lib/docker
sudo systemctl restart docker

# Example 2: Run with user mapping
docker run -v /data:/app --user 1000:1000 my-app

# Example 3: Check SELinux
getenforce
# Enforcing
sudo setsebool -P container_manage_cgroup on
```

## Related Errors

- [Socket permission denied]({{< relref "/tools/docker/docker-socket-permission" >}}) — related error
- [Cannot connect to daemon]({{< relref "/tools/docker/cannot-connect-to-docker-daemon" >}}) — related error
