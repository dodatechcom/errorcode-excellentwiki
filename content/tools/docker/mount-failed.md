---
title: "[Solution] Docker Mount Failed — mount failed"
description: "Fix Docker mount failed error. Resolve volume and bind mount issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# mount failed

This error occurs when Docker cannot mount a volume or bind mount into a container. The mount operation fails due to permissions, paths, or filesystem issues.

## Common Causes

- Source path does not exist
- Insufficient permissions on source directory
- SELinux blocking the mount
- Volume already mounted to another container
- NFS or remote filesystem unreachable
- Docker daemon cannot access mount source

## How to Fix

### Verify Source Path Exists

```bash
ls -la /path/on/host
```

### Fix Permissions

```bash
sudo chown -R 1000:1000 /path/on/host
sudo chmod -R 755 /path/on/host
```

### Check SELinux

```bash
# Add :Z flag for private mount
docker run -v /path:/mount:Z my-image
# Add :z flag for shared mount
docker run -v /path:/mount:z my-image
```

### Check Mount Points

```bash
mount | grep /path/on/host
```

### Create Missing Directories

```bash
mkdir -p /path/on/host
```

## Examples

```bash
# Example 1: Source path missing
docker run -v /data:/app my-image
# mount failed: /data does not exist
mkdir -p /data

# Example 2: SELinux issue
docker run -v /data:/app my-image
# mount failed (permission denied)
docker run -v /data:/app:Z my-image

# Example 3: Check mounts
mount | grep /data
```

## Related Errors

- [Docker volume error]({{< relref "/tools/docker/docker-volume-error" >}}) — related error
- [Error creating overlay]({{< relref "/tools/docker/error-creating-overlay" >}}) — related error
