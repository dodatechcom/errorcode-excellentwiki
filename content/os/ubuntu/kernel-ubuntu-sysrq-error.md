---
title: "[Solution] Ubuntu Server: kernel-ubuntu-sysrq-error"
description: "Fix Ubuntu kernel-ubuntu-sysrq-error. Magic SysRq key functions failing or misconfigured."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Ubuntu SysRq Error

The Magic SysRq key functions are failing or misconfigured.

## Common Causes
- SysRq disabled in kernel config
- /proc/sys/kernel/sysrq set to 0
- Wrong key combination used
- Serial console not configured for SysRq

## How to Fix
1. Check current SysRq setting
```bash
cat /proc/sys/kernel/sysrq
```
2. Enable SysRq
```bash
echo 1 | sudo tee /proc/sys/kernel/sysrq
```
3. Make persistent
```bash
echo "kernel.sysrq = 1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

## Examples
```bash
$ cat /proc/sys/kernel/sysrq
0

$ echo 1 | sudo tee /proc/sys/kernel/sysrq
1
```
