---
title: "Ubuntu eCryptfs Home Directory Encryption Error"
description: "eCryptfs encrypted home directory fails to mount or decrypt"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu eCryptfs Home Directory Encryption Error

eCryptfs encrypted home directory fails to mount or decrypt

## Common Causes

- Login passphrase incorrect
- Mount passphrase not wrapped properly
- eCryptfs module not loaded
- Directory permissions prevent mounting

## How to Fix

1. Check module: `lsmod | grep ecryptfs`
2. Load module: `sudo modprobe ecryptfs`
3. Check mount: `mount | grep ecryptfs`
4. Manual mount: `sudo ecryptfs-mount-private`

## Examples

```bash
# Check if ecryptfs is loaded
lsmod | grep ecryptfs

# Load ecryptfs module
sudo modprobe ecryptfs

# Check encrypted home mount
mount | grep ecryptfs
```
