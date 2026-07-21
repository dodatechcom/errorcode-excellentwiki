---
title: "[Solution] Linux: kernel-module-version-mismatch -- kernel module version mismatch"
description: "Fix Linux kernel module version mismatch errors. Module does not match running kernel version."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Kernel Module Version Mismatch

Kernel module version mismatch occurs when a compiled module does not match the running kernel version, preventing it from loading.

## Common Causes

- Kernel upgraded without recompiling modules
- DKMS build failed after kernel update
- Mixing distribution kernels with third-party modules
- /lib/modules directory contains stale module files
- Incorrect kernel headers installed

## How to Fix

### 1. Check Running Kernel

```bash
uname -r
cat /proc/version
```

### 2. Rebuild Module

```bash
sudo dkms autoinstall -k $(uname -r)
sudo depmod -a
sudo modprobe <module_name>
```

### 3. Reinstall Headers and Module

```bash
sudo apt install linux-headers-$(uname -r) 2>/dev/null
sudo yum install kernel-devel-$(uname -r) 2>/dev/null
sudo dkms install <module>/<version>
```

## Examples

```bash
$ uname -r
5.15.0-56-generic
$ ls /lib/modules/
5.15.0-56-generic  5.15.0-48-generic
$ sudo dkms autoinstall -k 5.15.0-56-generic
```
