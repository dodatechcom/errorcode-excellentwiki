---
title: "Ubuntu Disk I/O Error on Boot"
description: "System encounters disk I/O errors preventing normal boot"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Disk I/O Error on Boot

System encounters disk I/O errors preventing normal boot

## Common Causes

- Bad sectors on disk causing read/write failures
- Disk failing SMART health check
- Cable or connection issue with storage device
- Filesystem corruption from previous crash

## How to Fix

1. Check SMART: `sudo smartctl -a /dev/sda`
2. Test read: `sudo hdparm -t /dev/sda`
3. Check dmesg: `dmesg | grep -i error`
4. Boot from USB and run fsck on affected partition

## Examples

```bash
# Check disk SMART status
sudo smartctl -a /dev/sda

# Test disk read speed
sudo hdparm -Tt /dev/sda

# Check kernel I/O errors
dmesg | grep -i 'error\|fail'
```
