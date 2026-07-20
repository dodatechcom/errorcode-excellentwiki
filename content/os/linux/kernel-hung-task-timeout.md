---
title: "[Solution] Linux: kernel-hung-task-timeout — Task hung for more than 120 seconds"
description: "Fix Linux kernel-hung-task-timeout errors. Task hung for more than 120 seconds with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["kernel-error"]
weight: 10
---

# Linux: Kernel Hung Task Timeout Error

Kernel hung task timeout errors occur when the kernel encounters issues with hung task timeout operations or subsystem components.

## Common Causes

- Hardware incompatibility or failure affecting hung task timeout
- Kernel module or driver bugs in the hung task timeout subsystem
- Insufficient system resources or configuration limits
- Firmware or microcode issues
- Kernel parameter misconfiguration

## How to Fix

### 1. Check Kernel Logs

```bash
sudo dmesg | grep -i "hung-task-timeout" | tail -30
sudo journalctl -k --no-pager -n 50 | grep -i "hung-task-timeout"
```

### 2. Check Kernel Parameters

```bash
cat /proc/cmdline
sysctl -a 2>/dev/null | grep -i "hung-task-timeout"
```

### 3. Update or Reconfigure

```bash
# Update kernel
sudo apt update && sudo apt install linux-image-$(uname -r)
# Or adjust kernel parameters
sudo sysctl -w <parameter>=<value>
```

### 4. Check Hardware Status

```bash
sudo lspci -vvv | grep -i "hung-task-timeout" | head -20
sudo lsusb -v 2>/dev/null | grep -i "hung-task-timeout" | head -10
```

## Examples

```bash
$ dmesg | grep -i "hung-task-timeout" | tail -5
[12345.678] kernel: hung-task-timeout error detected on device
[12345.679] kernel: hung-task-timeout subsystem: failed to initialize

$ cat /proc/cmdline
BOOT_IMAGE=/vmlinuz-... root=... ro quiet

# Adjust kernel parameter and reboot
$ echo "<parameter>=<value>" | sudo tee -a /etc/sysctl.d/99-hung-task-timeout.conf
```
