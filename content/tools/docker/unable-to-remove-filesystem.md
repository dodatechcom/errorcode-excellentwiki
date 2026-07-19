---
title: "[Solution] Docker Unable to Remove Filesystem — unable to remove filesystem"
description: "Fix Docker unable to remove filesystem error. Resolve container layer and overlay issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

# unable to remove filesystem

This error occurs when Docker cannot delete the container's filesystem from disk. This is a more specific version of container removal failure related to storage layers.

## Common Causes

- Overlay mount still in use
- Container process holding file locks
- Docker storage driver corruption
- Insufficient disk permissions
- Container in inconsistent state

## How to Fix

### Force Remove Container

```bash
docker rm -f <container>
```

### Check Docker Storage Driver

```bash
docker info | grep "Storage Driver"
```

### Restart Docker Daemon

```bash
sudo systemctl restart docker
```

### Check Overlay Mounts

```bash
mount | grep overlay
```

### Remove Container and All Layers

```bash
docker rm -f <container>
docker system prune -f
```

### Manual Cleanup

```bash
# Stop Docker first
sudo systemctl stop docker
# Remove stuck container data
sudo rm -rf /var/lib/docker/containers/<container-id>
# Restart Docker
sudo systemctl start docker
```

## Examples

```bash
# Example 1: Force remove
docker rm -f stuck-container

# Example 2: Check overlay mounts
mount | grep overlay
# /dev/sda1 on /var/lib/docker/overlay2/...

# Example 3: Full cleanup
docker rm -f stuck-container
docker system prune -f
```

## Related Errors

- [Container removal failed]({{< relref "/tools/docker/container-removal-failed" >}}) — related error
- [Error creating overlay mount]({{< relref "/tools/docker/error-creating-overlay-mount" >}}) — related error
