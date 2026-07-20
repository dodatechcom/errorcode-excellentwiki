---
title: "[Solution] Linux: disk-quota-exceeded — disk quota exceeded error"
description: "Fix Linux disk-quota-exceeded errors. disk quota exceeded error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 6
---
# Linux: Disk Quota Exceeded

A quota exceeded error (EDQUOT, errno 122) occurs when a user or group surpasses their allocated disk space.

## Common Causes

- User filled their home directory beyond the soft or hard limit
- Application (mail server, database) writing files under the user's quota
- Temporary files accumulating without cleanup
- Quota limits set too low for the normal workload

## How to Fix

### 1. Check Quota Usage

```bash
quota -v
sudo quota -v <username>
```

### 2. Find Large Files

```bash
find /home/<username> -xdev -type f -size +10M -exec ls -lh {} \;
du -sh /home/<username>/* | sort -rh | head -10
```

### 3. Clean Up

```bash
rm -rf ~/.local/share/Trash/*
rm -rf ~/.cache/*
```

### 4. Increase Quota

```bash
sudo setquota -u <username> 0 2000000 2200000 0 /dev/sdX
# Or interactively
sudo edquota -u <username>
```

## Examples

```bash
$ quota -v
Disk quotas for user jdoe (uid 1001):
 Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
  /dev/sda1  9999999 5000000 5500000    none    1234       0       0
write failed: Disk quota exceeded
```
