---
title: "[Solution] Ubuntu Server: dpkg-unpack-error"
description: "Fix Ubuntu dpkg-unpack-error. dpkg fails while unpacking a package during installation."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Dpkg Unpack Error

dpkg fails while unpacking a package due to filesystem or data issues.

## Common Causes
- Insufficient disk space on the target partition
- File permission denied during unpacking
- Existing file conflicts with package contents
- Corrupted .deb archive
- Read-only filesystem

## How to Fix
1. Check disk space
```bash
df -h
```
2. Force overwriting conflicting files
```bash
sudo dpkg --force-overwrite -i <package>.deb
```
3. Check filesystem is writable
```bash
mount | grep " / "
```

## Examples
```bash
$ sudo dpkg -i nginx_1.18.0_amd64.deb
dpkg: error processing archive nginx_1.18.0_amd64.deb (--unpack):
 unable to open /etc/nginx/nginx.conf.dpkg-new: No space left on device

$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G   20G     0 100% /
```
