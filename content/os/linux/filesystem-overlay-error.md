---
title: "[Solution] Linux: filesystem-overlay-error -- overlay mount failed"
description: "Fix Linux overlay filesystem errors. Overlay filesystem mount failure in containers."
os: ["linux"]
error-types: ["filesystem-error"]
severities: ["error"]
---

# Linux: Overlay Filesystem Error

Overlay filesystem errors occur when the overlay mount fails due to misconfigured directories.

## Common Causes

- Upper directory on same filesystem as lower
- Missing workdir for overlay mount
- Unsupported filesystem for upperdir
- Kernel does not support overlayfs
- Permissions preventing whiteout creation

## How to Fix

### 1. Check Overlay Support

```bash
modprobe overlay
cat /proc/filesystems | grep overlay
dmesg | grep -i overlay
```

### 2. Verify Directory Structure

```bash
ls -la /overlay/upper
ls -la /overlay/work
ls -la /overlay/lower
```

### 3. Mount Correctly

```bash
sudo mkdir -p /overlay/{upper,work,lower,merged}
sudo mount -t overlay overlay \
  -o lowerdir=/overlay/lower,upperdir=/overlay/upper,workdir=/overlay/work \
  /overlay/merged
```

## Examples

```bash
$ sudo mount -t overlay overlay -o lowerdir=/lower,upperdir=/upper,workdir=/work /merged
mount: /merged: mount(2) system call failed: Invalid argument.
$ cat /proc/filesystems | grep overlay
nodev\toverlay
```
