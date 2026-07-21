---
title: "[Solution] Ubuntu Server: kernel-ubuntu-modules-blacklist"
description: "Fix Ubuntu kernel-ubuntu-modules-blacklist. Essential kernel module is accidentally blacklisted."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Ubuntu Modules Blacklist

An essential kernel module has been accidentally blacklisted.

## Common Causes
- Admin blacklisted module for testing and forgot to re-enable
- Package post-install script blacklisted module
- Duplicate blacklist entries
- /etc/modprobe.d/ override from another package

## How to Fix
1. Find blacklist entries
```bash
grep -r "blacklist <module>" /etc/modprobe.d/
```
2. Remove or comment out blacklist
```bash
sudo nano /etc/modprobe.d/blacklist.conf
# Comment out the blacklist line
```
3. Rebuild module dependencies
```bash
sudo depmod -a
```

## Examples
```bash
$ grep -r "blacklist nouveau" /etc/modprobe.d/
/etc/modprobe.d/blacklist.conf:blacklist nouveau
```
