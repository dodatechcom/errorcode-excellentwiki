---
title: "[Solution] Linux: filesystem-proc-mount-error -- proc filesystem mount failure"
description: "Fix Linux proc filesystem mount errors. Proc filesystem cannot be mounted on system."
os: ["linux"]
error-types: ["filesystem-error"]
severities: ["error"]
---

# Linux: Proc Filesystem Mount Error

Proc filesystem mount errors occur when /proc cannot be mounted, breaking system tools.

## Common Causes

- initramfs missing proc mount instructions
- Container namespace missing /proc
- Kernel not compiled with CONFIG_PROC_FS
- fstab entry for proc is incorrect
- Read-only root filesystem preventing mount

## How to Fix

### 1. Check Proc Status

```bash
mount | grep proc
ls -la /proc/1/cmdline
```

### 2. Manually Mount Proc

```bash
sudo mount -t proc proc /proc
```

### 3. Fix fstab

```bash
grep proc /etc/fstab
# Should contain: proc /proc proc defaults 0 0
sudo systemctl daemon-reload
```

## Examples

```bash
$ mount | grep proc
$ ls /proc/1/cmdline
ls: cannot access /proc/1/cmdline: No such file or directory
$ sudo mount -t proc proc /proc
$ ls /proc/1/cmdline
/sbin/init
```
