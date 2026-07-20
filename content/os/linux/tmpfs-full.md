---
title: "[Solution] Linux: tmpfs-full — tmpfs full error"
description: "Fix Linux tmpfs-full errors. tmpfs full error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 6
---

# Linux: tmpfs Full

tmpfs full errors occur when the RAM-based temporary filesystem runs out of space.

## Common Causes

- /tmp filled by application temporary files
- /dev/shm filled by shared memory allocations
- Docker/container tmpfs mounts too small
- Browser cache in tmpfs consuming space
- Large file operations in /tmp

## How to Fix

### 1. Check tmpfs Usage

```bash
df -h | grep tmpfs
du -sh /tmp /var/tmp /dev/shm /run
```

### 2. Identify Large Files

```bash
sudo find /tmp -type f -size +100M -exec ls -lh {} \;
sudo du -sh /tmp/* | sort -rh | head -10
```

### 3. Clean tmpfs

```bash
sudo find /tmp -type f -atime +1 -delete
sudo rm -rf /tmp/* 2>/dev/null
```

### 4. Increase tmpfs Size

```bash
sudo mount -o remount,size=4G /tmp
# Or in /etc/fstab:
# tmpfs /tmp tmpfs defaults,size=4G 0 0
```

## Examples

```bash
$ df -h /tmp
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           1.6G  1.6G     0 100% /tmp

$ sudo du -sh /tmp/* | sort -rh | head -5
1.2G    /tmp/large-build-cache
400M    /tmp/docker-temp

$ sudo rm -rf /tmp/large-build-cache
$ df -h /tmp
tmpfs           1.6G  400M  1.2G  25% /tmp
```
