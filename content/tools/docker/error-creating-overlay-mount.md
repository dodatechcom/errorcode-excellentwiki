---
title: "[Solution] Docker Error Creating Overlay Mount — error creating overlay mount"
description: "Fix Docker error creating overlay mount. Resolve overlay2 storage driver issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# error creating overlay mount

This error occurs when Docker cannot create the overlay mount needed for container filesystem layers. The overlay2 storage driver fails to set up the union filesystem.

## Common Causes

- Overlay filesystem not supported on host
- Too many overlay mounts
- Kernel module not loaded
- Docker data directory full
- Storage driver misconfiguration

## How to Fix

### Check Overlay Support

```bash
grep overlay /proc/filesystems
# Should show: overlay
```

### Load Overlay Module

```bash
sudo modprobe overlay
```

### Check Current Overlay Mounts

```bash
mount | grep overlay | wc -l
```

### Restart Docker

```bash
sudo systemctl restart docker
```

### Check Docker Storage Driver

```bash
docker info | grep "Storage Driver"
# Should be: overlay2
```

### Increase fs.max_user_namespaces

```bash
sudo sysctl -w fs.max_user_namespaces=28633
```

## Examples

```bash
# Example 1: Check overlay support
grep overlay /proc/filesystems
# overlay

# Example 2: Load module
sudo modprobe overlay
sudo systemctl restart docker

# Example 3: Check mount count
mount | grep overlay | wc -l
# If very high, restart Docker daemon
```

## Related Errors

- [Error creating overlay]({{< relref "/tools/docker/error-creating-overlay" >}}) — related error
- [Mount failed]({{< relref "/tools/docker/mount-failed" >}}) — related error
