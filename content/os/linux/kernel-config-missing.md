---
title: "[Solution] Linux: kernel-config-missing -- kernel config file missing"
description: "Fix Linux kernel config missing errors. Kernel configuration file not found on system."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["warning"]
---

# Linux: Kernel Config Missing

Kernel config missing errors occur when /proc/config.gz or /boot/config is unavailable.

## Common Causes

- Kernel built without CONFIG_IKCONFIG enabled
- /proc/config.gz not mounted or unavailable
- Custom kernel missing configuration export
- Distribution kernel stripped config support
- Container environment hiding /proc entries

## How to Fix

### 1. Check for Config

```bash
ls /boot/config-$(uname -r)
zcat /proc/config.gz 2>/dev/null || echo "Not available"
```

### 2. Install Config Package

```bash
sudo apt install linux-config-$(uname -r) 2>/dev/null
sudo yum install kernel-headers-$(uname -r) 2>/dev/null
```

### 3. Extract from /proc

```bash
sudo cat /boot/config-$(uname -r) | grep CONFIG_IKCONFIG
gunzip -c /proc/config.gz > /boot/config-$(uname -r)
```

## Examples

```bash
$ zcat /proc/config.gz 2>&1
zcat: /proc/config.gz: No such file or directory
$ ls /boot/config-*
ls: cannot access './config-*': No such file or directory
$ sudo apt install linux-config-5.15.0-56
Reading package lists... Done
```
