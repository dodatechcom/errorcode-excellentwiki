---
title: "APT Clean Error"
description: "Error when running apt-get clean or apt clean commands"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# APT Clean Error

Error when running apt-get clean or apt clean commands

## Common Causes

- Permission denied on /var/cache/apt/archives/
- Disk filesystem is read-only
- Broken symlinks in cache directory
- Package cache corrupted by interrupted transaction

## How to Fix

1. Run with sudo: `sudo apt-get clean`
2. Check filesystem is not read-only: `mount | grep ' / '`
3. Remove cache manually: `sudo rm -rf /var/cache/apt/archives/*`
4. Fix broken symlinks: `sudo find /var/cache/apt -type l -delete`

## Examples

```bash
# Force clean even with errors
sudo rm -rf /var/cache/apt/archives/*

# Verify cache is empty
ls /var/cache/apt/archives/
```
