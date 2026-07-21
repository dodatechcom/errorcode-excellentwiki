---
title: "[Solution] Ubuntu Server: ubuntu-kernel-panic-triple-fault"
description: "Fix Ubuntu ubuntu-kernel-panic-triple-fault. Triple fault causes immediate reboot."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Panic Triple Fault

Triple fault causes immediate system reboot.

## Common Causes
- Virtualization guest triple fault
- Kernel bug in interrupt handling
- Corrupted IDT/GDT

## How to Fix
1. Check for crash dumps
```bash
ls /var/crash/
sudo systemctl status kdump-tools
```
2. Check VM logs if virtualized
```bash
sudo tail -100 /var/log/libvirt/qemu/<vm>.log
```
3. Enable crash dump
```bash
sudo apt install kdump-tools
sudo systemctl enable kdump-tools
```

## Examples
```bash
$ ls /var/crash/
2023-03-15-10:00/
```