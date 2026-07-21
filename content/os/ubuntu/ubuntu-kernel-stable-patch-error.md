---
title: "[Solution] Ubuntu Server: ubuntu-kernel-stable-patch-error"
description: "Fix Ubuntu ubuntu-kernel-stable-patch-error. Stable kernel patch fails to apply."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Stable Patch Error

Stable kernel patch or update fails to apply cleanly.

## Common Causes
- Custom patches conflict with stable patch
- Kernel source modified locally
- Patch expects different base version

## How to Fix
1. Check kernel version
```bash
uname -r
apt list --installed | grep linux-image
```
2. Update from repository
```bash
sudo apt update
sudo apt upgrade linux-generic
```
3. Check available versions
```bash
apt-cache policy linux-generic
```

## Examples
```bash
$ apt-cache policy linux-generic
linux-generic:
  Installed: 5.15.0-25.26
  Candidate: 5.15.0-76.83
```