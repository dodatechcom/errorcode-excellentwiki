---
title: "[Solution] Docker Volume Error — permission denied on volume mount"
description: "Fix Docker volume mount permission denied errors. Resolve container volume access issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A Docker volume error occurs when a container cannot mount or access a volume due to permission issues. The container process lacks the necessary file system permissions.

## Common Causes

- The container runs as a non-root user that lacks write access to the mounted path
- The host directory has restrictive permissions (chmod/chown)
- SELinux or AppArmor policies block access to the host path
- The volume was created with different ownership
- File system type does not support required permissions

## How to Fix

### Check Host Directory Permissions

```bash
ls -la /host/path
stat /host/path
```

### Fix Permissions on Host

```bash
sudo chown -R 1000:1000 /host/path
sudo chmod -R 755 /host/path
```

### Run Container as Root

```bash
docker run -v /host/path:/container/path --user root my-image
```

### Create Named Volume Instead

```bash
docker volume create my-volume
docker run -v my-data:/container/path my-image
```

### Fix SELinux Context

```bash
docker run -v /host/path:/container/path:z my-image
```

## Examples

```bash
# Example 1: Permission denied on bind mount
docker run -v /data/app:/app my-image
# Error: permission denied
# Fix: sudo chown -R 1000:1000 /data/app

# Example 2: Use named volume
docker volume create app-data
docker run -v app-data:/app/data my-image
```

## Related Errors

- [Docker Socket Permission]({{< relref "/tools/docker/docker-socket-permission" >}}) — permission denied on docker.sock
- [Docker Compose Error]({{< relref "/tools/docker/docker-compose-error" >}}) — docker-compose up failed
