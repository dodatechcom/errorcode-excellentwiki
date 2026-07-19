---
title: "[Solution] Docker Error Creating Overlay — error creating overlay"
description: "Fix Docker error creating overlay error. Resolve overlay2 storage and mount issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# error creating overlay for container

This error occurs when Docker fails to create the overlay filesystem for a container's layers. It is closely related to overlay mount errors but may indicate different root causes.

## Common Causes

- Docker daemon configuration issue
- Storage directory permissions wrong
- Device or filesystem full
- Kernel version incompatible with overlay2
- Docker data corruption

## How to Fix

### Check Docker Data Directory

```bash
df -h /var/lib/docker
```

### Verify Directory Permissions

```bash
ls -la /var/lib/docker/
sudo chown -R root:root /var/lib/docker
```

### Check Docker Storage Configuration

```bash
docker info | grep -A5 "Storage Driver"
```

### Clean Up Docker Data

```bash
docker system prune -a
```

### Check Kernel Version

```bash
uname -r
# overlay2 requires kernel 4.0+
```

### Reset Docker Storage

```bash
sudo systemctl stop docker
sudo rm -rf /var/lib/docker/overlay2/*
sudo systemctl start docker
```

## Examples

```bash
# Example 1: Check disk space
df -h /var/lib/docker
# Filesystem  Size  Used  Avail
# /dev/sda1   50G   48G   2G  <-- Almost full

# Example 2: Check kernel
uname -r
# 5.4.0 -- supports overlay2

# Example 3: Clean up
docker system prune -a
# Reclaim space
```

## Related Errors

- [Error creating overlay mount]({{< relref "/tools/docker/error-creating-overlay-mount" >}}) — related error
- [Mount failed]({{< relref "/tools/docker/mount-failed" >}}) — related error
