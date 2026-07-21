---
title: "Ubuntu Landlock LSM Error"
description: "Landlock Linux Security Module preventing application operations"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Landlock LSM Error

Landlock Linux Security Module preventing application operations

## Common Causes

- Application trying to access filesystem outside Landlock rules
- Landlock access rights not properly configured
- Kernel version too old for Landlock features
- Application sandbox too restrictive

## How to Fix

1. Check Landlock: `cat /sys/kernel/security/lsm`
2. Verify kernel: `uname -r` (Landlock requires 5.13+)
3. Check app logs for Landlock denials: `journalctl -k | grep landlock`
4. Update application or adjust Landlock configuration

## Examples

```bash
# Check LSM configuration
cat /sys/kernel/security/lsm

# Check kernel version
uname -r

# Check Landlock denials
sudo journalctl -k | grep -i landlock
```
