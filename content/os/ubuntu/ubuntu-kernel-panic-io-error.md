---
title: "[Solution] Ubuntu Server: ubuntu-kernel-panic-io-error"
description: "Fix Ubuntu ubuntu-kernel-panic-io-error. I/O error triggers kernel panic."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Panic I/O Error

I/O error on storage device triggers kernel panic.

## Common Causes
- Disk hardware failure
- Bad sectors on system disk
- Storage controller failure

## How to Fix
1. Check disk health
```bash
sudo smartctl -a /dev/sda
dmesg | grep -i "error"
```
2. Check filesystem
```bash
sudo e2fsck -f /dev/sda1
```
3. Replace failing disk if needed

## Examples
```bash
$ dmesg | grep -i "error"
[  123.456] sd 0:0:0:0: [sda] FAILED Result: hostbyte=DID_OK
```