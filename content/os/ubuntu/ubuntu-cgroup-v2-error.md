---
title: "[Solution] Ubuntu Server: ubuntu-cgroup-v2-error"
description: "Fix Ubuntu ubuntu-cgroup-v2-error. cgroup v2 configuration causes issues."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Cgroup V2 Error

cgroup v2 configuration causes system or container issues.

## Common Causes
- cgroup v2 enabled but app expects v1
- Memory controller not available
- systemd not using cgroup v2

## How to Fix
1. Check cgroup version
```bash
stat -fc %T /sys/fs/cgroup
```
2. Check cgroup controllers
```bash
cat /sys/fs/cgroup/cgroup.controllers
```
3. Switch to cgroup v1 if needed
```bash
# In GRUB: systemd.unified_cgroup_hierarchy=0
sudo nano /etc/default/grub
GRUB_CMDLINE_LINUX="systemd.unified_cgroup_hierarchy=0"
sudo update-grub
```

## Examples
```bash
$ stat -fc %T /sys/fs/cgroup
cgroup2fs
```