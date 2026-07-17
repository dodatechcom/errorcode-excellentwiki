---
title: "[Solution] Docker Volume Mount Permission Denied"
description: "Fix Docker volume mount permission denied errors. Resolve container volume access and ownership issues."
tools: ["docker"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["volume", "mount", "permission", "denied", "bind-mount", "docker"]
weight: 5
---

## What This Error Means

A Docker volume mount permission denied error occurs when a container cannot access a mounted volume or bind mount due to file system permission restrictions. The container process lacks the necessary read/write access to the mounted path.

## Common Causes

- Container runs as a non-root user without access to the host path
- Host directory has restrictive permissions (wrong ownership or mode)
- SELinux or AppArmor policies block access to the host path
- The volume was created with different ownership than expected
- Docker Desktop file sharing settings restrict access

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

### Use a Named Volume

```bash
docker volume create app-data
docker run -v app-data:/app/data my-image
```

### Fix SELinux Context

```bash
docker run -v /host/path:/container/path:z my-image
```

### Fix Docker Desktop Permissions (macOS/Windows)

```bash
# In Docker Desktop settings, add the path to File Sharing
# Or use a named volume instead of bind mount
```

## Examples

```bash
# Example 1: Permission denied on bind mount
docker run -v /data/app:/app my-image
# Error: permission denied
# Fix: sudo chown -R 1000:1000 /data/app

# Example 2: Named volume avoids permission issues
docker volume create app-data
docker run -v app-data:/app/data my-image

# Example 3: Use SELinux label for RHEL/CentOS
docker run -v /host/data:/app/data:Z my-image
```

## Related Errors

- [Docker Compose Error]({{< relref "/tools/docker/docker-compose-error-v2" >}}) — docker compose up failed
- [Docker Network Error]({{< relref "/tools/docker/docker-network-error-v2" >}}) — network bridge creation failed
- [Docker BuildKit Error]({{< relref "/tools/docker/docker-buildkit-error" >}}) — BuildKit build error
