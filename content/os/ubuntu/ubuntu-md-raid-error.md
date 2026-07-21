---
title: "Ubuntu Software RAID Array Degraded"
description: "Software RAID array enters degraded state due to disk failure"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Software RAID Array Degraded

Software RAID array enters degraded state due to disk failure

## Common Causes

- One or more disks in RAID array failed
- Disk disconnected or not detected
- Spare disk not configured for automatic rebuild
- Superblock corruption on member disk

## How to Fix

1. Check array: `cat /proc/mdstat`
2. Mark disk failed: `sudo mdmanage /dev/md0 --fail /dev/sdb1`
3. Remove failed disk: `sudo mdmanage /dev/md0 --remove /dev/sdb1`
4. Add replacement: `sudo mdmanage /dev/md0 --add /dev/sdc1`

## Examples

```bash
# Check RAID status
cat /proc/mdstat

# Check array details
sudo mdadm --detail /dev/md0

# Replace failed disk
sudo mdadm --fail /dev/md0 /dev/sdb1
sudo mdadm --remove /dev/md0 /dev/sdb1
sudo mdadm --add /dev/md0 /dev/sdc1
```
