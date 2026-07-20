---
title: "[Solution] Linux: kernel-panic-not-syncing — Kernel panic not syncing"
description: "Fix Linux kernel-panic-not-syncing errors. Kernel panic not syncing with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["kernel-error"]
weight: 15
---
# Linux: Kernel Panic - Not Syncing

"Kernel panic - not syncing" indicates the kernel encountered a fatal error it cannot recover from and halts the system.

## Common Causes

- Fatal machine check exception from CPU hardware error
- Kernel BUG() triggered by a software bug
- VFS (Virtual Filesystem) unable to mount root filesystem
- Out of memory and no process can be killed (panic_on_oom)
- Critical kernel thread crashed (kthreadd, init)

## How to Fix

### 1. Identify the Error Message

```bash
# Check panic message from previous boot
journalctl -k -b -1 | grep -i "panic\|BUG\|Oops"
```

### 2. Boot into Recovery Mode

Boot with `single` or `emergency` from GRUB.

### 3. Check Root Filesystem

```bash
# If panic is from VFS, check root device
sudo blkid
sudo fsck -f /dev/sda1
```

### 4. Update or Reinstall Kernel

```bash
sudo apt install --reinstall linux-image-$(uname -r)
```

### 5. Temporarily Disable Panic on OOM

```bash
sudo sysctl -w vm.panic_on_oom=0
```

## Examples

```bash
$ journalctl -k -b -1 | grep panic
Jul 19 03:15:01 server kernel: Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)
Jul 19 03:15:01 server kernel: Kernel panic - not syncing: Out of memory and no killable processes...

$ sudo blkid /dev/sda1
/dev/sda1: UUID="12345678-1234-1234-1234-123456789012" TYPE="ext4"
```
