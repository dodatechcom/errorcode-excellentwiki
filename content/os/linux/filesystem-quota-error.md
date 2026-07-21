---
title: "[Solution] Linux: filesystem-quota-error -- disk quota exceeded"
description: "Fix Linux filesystem quota errors. Disk quota exceeded preventing file creation."
os: ["linux"]
error-types: ["filesystem-error"]
severities: ["error"]
---

# Linux: Filesystem Quota Error

Disk quota errors occur when a user or group exceeds their allocated disk space or inode limits.

## Common Causes

- User exceeding allocated block quota
- Group quota limit reached
- Inode quota exceeded (too many files)
- Quota not properly enabled on filesystem
- Soft quota grace period expired

## How to Fix

### 1. Check Quota Status

```bash
sudo repquota -a
quota -u <username>
quota -g <groupname>
```

### 2. Enable Quota

```bash
sudo quotacheck -cugm /home
sudo quotaon /home
```

### 3. Adjust Quotas

```bash
sudo edquota -u <username>
sudo edquota -g <groupname>
sudo setquota -u <username> 10G 12G 0 0 /home
```

## Examples

```bash
$ sudo repquota -a
*** Report for user quotas on device /dev/sda2
Block grace time: 7days; Inode grace time: 7days
                        Block limits                File limits
User            used    soft    hard  grace    used  soft  hard  grace
root      --   500M      0       0              12345    0     0
john      --   10.2G    10G   12G   6days     89012  50k  60k
# john over soft limit, grace period counting down
```
