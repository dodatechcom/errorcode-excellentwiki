---
title: "[Solution] Ubuntu Server: kernel-dkms-build-error"
description: "Fix Ubuntu kernel-dkms-build-error. DKMS module build fails after kernel upgrade."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel DKMS Build Error

DKMS fails to build a module after kernel upgrade.

## Common Causes
- Kernel headers not installed
- Build tools missing
- Source code incompatible with new kernel API
- Missing kernel header symlinks

## How to Fix
1. Install kernel headers
```bash
sudo apt install linux-headers-$(uname -r)
```
2. Install build essentials
```bash
sudo apt install build-essential dkms
```
3. Rebuild DKMS module
```bash
sudo dkms autoinstall
sudo dkms install <module>/<version> -k <kernel-version>
```

## Examples
```bash
$ sudo dkms status
nvidia/510.108.03, 5.15.0-25-generic, x86_64: installed (module version mismatch)

$ sudo dkms install nvidia/510.108.03 -k 5.15.0-25-generic
Error! Kernel not found
```
