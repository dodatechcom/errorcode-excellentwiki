---
title: "[Solution] Linux: kernel-modules-not-loading -- kernel modules not loading"
description: "Fix Linux kernel modules not loading errors. Kernel modules fail to load at boot time."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Kernel Modules Not Loading

Kernel modules fail to load at boot, causing missing hardware support or driver functionality.

## Common Causes

- Module blacklisted in /etc/modprobe.d/
- modprobe.conf has incorrect syntax
- initramfs does not include the module
- Module depends on another unloaded module
- Secure Boot blocking unsigned modules

## How to Fix

### 1. Check Module Status

```bash
lsmod | grep <module_name>
sudo modprobe -v <module_name>
dmesg | tail -30
```

### 2. Remove Blacklist

```bash
grep -r <module_name> /etc/modprobe.d/
sudo sed -i "/blacklist <module_name>/d" /etc/modprobe.d/*.conf
```

### 3. Add to initramfs

```bash
echo "<module_name>" | sudo tee -a /etc/modules
sudo update-initramfs -u 2>/dev/null
sudo dracut -f 2>/dev/null
```

## Examples

```bash
$ lsmod | grep usb_storage
$ sudo modprobe -v usb_storage
insmod /lib/modules/5.15.0-56/kernel/drivers/usb/storage/usb-storage.ko
$ grep blacklist /etc/modprobe.d/*
/etc/modprobe.d/blacklist.conf:blacklist usb_storage
```
