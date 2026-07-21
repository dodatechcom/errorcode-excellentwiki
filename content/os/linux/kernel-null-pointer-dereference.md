---
title: "[Solution] Linux: kernel-null-pointer-dereference -- kernel null pointer dereference"
description: "Fix Linux kernel null pointer dereference errors. Kernel NULL pointer dereference causing panic."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Kernel Null Pointer Dereference

A kernel null pointer dereference occurs when the kernel attempts to access memory at address 0x0.

## Common Causes

- Buggy kernel module accessing uninitialized pointer
- Race condition in driver code
- Corrupted kernel data structures
- Faulty hardware causing memory corruption
- Kernel version incompatibility with module

## How to Fix

### 1. Analyze Crash Log

```bash
sudo dmesg | grep -i "null pointer" | tail -5
sudo journalctl -k | grep -A 20 "null pointer"
```

### 2. Check Loaded Modules

```bash
lsmod
sudo cat /proc/modules | awk '{print $1}'
```

### 3. Update Kernel

```bash
sudo apt update && sudo apt upgrade linux-image-$(uname -r)
sudo yum update kernel
```

## Examples

```bash
$ sudo dmesg | grep -i "null pointer"
[12345.678] BUG: unable to handle kernel NULL pointer dereference at 0000000000000020
[12345.679] PGD 0 P4D 0
[12345.680] Oops: 0000 [#1] SMP NOPTI
[12345.681] RIP: 0010:my_driver_read+0x1a/0x40 [my_module]
```
