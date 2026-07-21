---
title: "[Solution] Linux: cgroup-v2-error -- cgroup v2 migration error"
description: "Fix Linux cgroup v2 errors. Cgroup v2 migration or configuration failure on unified hierarchy."
os: ["linux"]
error-types: ["cgroup-error"]
severities: ["error"]
---

# Linux: Cgroup V2 Error

Cgroup v2 errors occur when the unified cgroup hierarchy fails to initialize.

## Common Causes

- Kernel boot parameter disabling cgroup v2
- initramfs not supporting unified hierarchy
- systemd version too old for cgroup v2
- Container runtime expecting cgroup v1 paths
- Mixed v1/v2 mounts causing conflicts

## How to Fix

### 1. Check Current Cgroup Version

```bash
stat -fc %T /sys/fs/cgroup/
cat /proc/filesystems | grep cgroup
mount | grep cgroup
```

### 2. Enable Cgroup v2

```bash
# Add to GRUB: systemd.unified_cgroup_hierarchy=1
GRUB_CMDLINE_LINUX="systemd.unified_cgroup_hierarchy=1"
sudo update-grub
```

### 3. Verify Migration

```bash
ls /sys/fs/cgroup/
cat /sys/fs/cgroup/cgroup.controllers
mount -t cgroup2 none /sys/fs/cgroup
```

## Examples

```bash
$ stat -fc %T /sys/fs/cgroup/
tmpfs
# tmpfs = cgroup v1, cgroup2fs = cgroup v2
$ mount | grep cgroup
tmpfs on /sys/fs/cgroup type tmpfs (rw)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw)
```
