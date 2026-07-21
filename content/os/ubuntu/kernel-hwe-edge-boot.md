---
title: "[Solution] Ubuntu Server: kernel-hwe-edge-boot"
description: "Fix Ubuntu kernel-hwe-edge-boot. HWE edge kernel fails to boot due to driver issues."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel HWE Edge Boot Failure

The HWE edge kernel fails to boot due to hardware or driver incompatibility.

## Common Causes
- HWE edge kernel too new for hardware
- Missing proprietary drivers for new kernel
- NVIDIA driver incompatibility
- ZFS module not compiled for HWE edge

## How to Fix
1. Boot from standard HWE or GA kernel
2. Check installed kernels
```bash
dpkg -l | grep linux-image
```
3. Switch to GA kernel
```bash
sudo apt install linux-generic
sudo apt remove linux-generic-hwe-22.04-edge
sudo update-grub
```

## Examples
```bash
$ dpkg -l | grep linux-image
ii  linux-image-5.17.0-1003-oem      5.17.0-1003.4      amd64
ii  linux-image-5.15.0-25-generic    5.15.0-25.26       amd64
```
