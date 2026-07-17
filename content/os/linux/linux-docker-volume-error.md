---
title: "[Solution] Docker Volume Permission Denied — Fix Mount Errors"
description: "Fix Docker volume permission denied errors on Linux. Resolve bind mount permission issues, SELinux context errors, and UID/GID mismatches."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Docker Volume Permission Denied — Fix Mount Errors

A Docker volume permission denied error occurs when a container cannot read or write to a mounted volume or bind mount. The error reads:

> "Mounts denied: The path [path] is not shared from the Docker VM and is not known to Docker."

Or:

> "Permission denied" inside the container when accessing mounted files.

## What This Error Means

Docker containers run with their own isolated filesystem. When you mount a host directory as a bind mount, the container's user must have permission to access the files. The container typically runs as root, but SELinux, AppArmor, or UID/GID mismatches can block access.

## Common Causes

- Host directory owned by a different user than the container user
- SELinux blocking container access to host files
- Docker Desktop for Mac/Windows VM file sharing issues
- Read-only mount used for a write operation
- ACL restrictions on the host directory
- Container user is not root and lacks permissions

## How to Fix

### Fix Host Directory Permissions

```bash
# Make directory accessible to everyone (quick fix)
sudo chmod -R 777 /path/to/mount

# Or change ownership to match container user
sudo chown -R 1000:1000 /path/to/mount
```

### Fix SELinux Context (RHEL/CentOS/Fedora)

```bash
# Add SELinux context label for Docker
sudo chcon -R -t svirt_sandbox_file_t /path/to/mount

# Or use :z flag in docker run
docker run -v /path/to/mount:/data:z nginx

# Use :Z for private (only this container) context
docker run -v /path/to/mount:/data:Z nginx
```

### Use a Named Volume Instead of Bind Mount

```bash
# Create a named volume
docker volume create mydata

# Use the named volume
docker run -v mydata:/data nginx
```

### Run Container as Specific User

```bash
# Run as root
docker run --user root -v /path/to/mount:/data nginx

# Run as specific UID:GID
docker run --user 1000:1000 -v /path/to/mount:/data nginx
```

### Fix Docker Desktop Volume Sharing

On Docker Desktop (Mac/Windows):

1. Go to **Docker Desktop > Settings > Resources > File Sharing**.
2. Add the directory to the shared list.
3. Apply and restart.

### Use --privileged (Last Resort)

```bash
# Grant full access to host devices
docker run --privileged -v /path/to/mount:/data nginx
```

**Warning**: This disables all security boundaries. Only use for debugging.

## Related Errors

- [Docker Socket Permission Denied]({{< relref "/os/linux/linux-docker-socket-permission" >}}) — Docker daemon socket access issues
- [Docker Container OOM Killed]({{< relref "/os/linux/linux-docker-out-of-memory" >}}) — Container memory limits
- [Docker Healthcheck Failed]({{< relref "/os/linux/linux-docker-healthcheck" >}}) — Container health check failures
