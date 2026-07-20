---
title: "[Solution] Linux: inode-full — inode exhaustion error"
description: "Fix Linux inode-full errors. inode exhaustion error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---

# Linux: Inode Full

The inode full error occurs when a filesystem runs out of inodes, preventing new file creation even with free space.

## Common Causes

- Too many small files exhausting inode table
- Filesystem created with too few inodes
- Mail spool or cache directory with millions of tiny files
- Filesystem not formatted with enough inodes
- Inode leak from kernel bug

## How to Fix

### 1. Check Inode Usage

```bash
df -i /mount/point
ls -la /mount/point | wc -l
```

### 2. Find Directories with Many Files

```bash
sudo find /mount/point -xdev -type d -print0 | xargs -0 -I{} sh -c 'echo "$(ls -1 "{}" | wc -l) {}"' | sort -rn | head -10
```

### 3. Clean Up Small Files

```bash
sudo find /mount/point -type f -size 0 -delete
sudo find /mount/point -name "*.tmp" -atime +7 -delete
```

### 4. Recreate Filesystem with More Inodes

```bash
sudo mkfs.ext4 -N <num_inodes> /dev/sda1
# Restore from backup
```

## Examples

```bash
$ df -i /var/spool/mail
Filesystem     Inodes IUsed IFree IUse% Mounted on
/dev/sda1      655360 655360     0  100% /var/spool

$ sudo find /var/spool/mail -type f | wc -l
655360
# All inodes consumed by mail files

$ sudo find /var/spool/mail -type f -atime +90 -delete
# Delete old mail
$ df -i /var/spool/mail
Filesystem     Inodes IUsed IFree IUse%
/dev/sda1      655360 600000 55360   92%
```
