---
title: "[Solution] Linux: filesystem-devtmpfs-error -- devtmpfs mount failure"
description: "Fix Linux devtmpfs errors. Devtmpfs mount failure causing missing device nodes in /dev."
os: ["linux"]
error-types: ["filesystem-error"]
severities: ["error"]
---

# Linux: Devtmpfs Filesystem Error

Devtmpfs mount errors prevent automatic device node creation in /dev.

## Common Causes

- Kernel not compiled with CONFIG_DEVTMPFS
- initramfs missing devtmpfs mount
- Boot loader skipping devtmpfs setup
- Container environments without /dev
- udev not populating device nodes

## How to Fix

### 1. Check Devtmpfs Status

```bash
mount | grep devtmpfs
ls /dev/null /dev/zero /dev/random
```

### 2. Mount Devtmpfs

```bash
sudo mount -t devtmpfs devtmpfs /dev
sudo udevadm trigger
```

### 3. Verify Device Nodes

```bash
ls -la /dev/sd*
ls -la /dev/null /dev/zero /dev/random /dev/urandom
```

## Examples

```bash
$ mount | grep devtmpfs
$ ls /dev/sda
ls: cannot access /dev/sda: No such file or directory
$ sudo mount -t devtmpfs devtmpfs /dev
$ ls /dev/sda
/dev/sda
```
