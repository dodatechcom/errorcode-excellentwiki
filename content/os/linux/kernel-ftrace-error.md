---
title: "[Solution] Linux: kernel-ftrace-error — Function tracing subsystem error"
description: "Fix Linux kernel-ftrace-error errors. Function tracing subsystem error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["kernel-error"]
weight: 8
---

# Linux: Kernel Ftrace Error Error

Kernel ftrace error errors occur when the kernel encounters issues with ftrace error operations or subsystem components.

## Common Causes

- Hardware incompatibility or failure affecting ftrace error
- Kernel module or driver bugs in the ftrace error subsystem
- Insufficient system resources or configuration limits
- Firmware or microcode issues
- Kernel parameter misconfiguration

## How to Fix

### 1. Check Kernel Logs

```bash
sudo dmesg | grep -i "ftrace-error" | tail -30
sudo journalctl -k --no-pager -n 50 | grep -i "ftrace-error"
```

### 2. Check Kernel Parameters

```bash
cat /proc/cmdline
sysctl -a 2>/dev/null | grep -i "ftrace-error"
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
sudo lspci -vvv | grep -i "ftrace-error" | head -20
sudo lsusb -v 2>/dev/null | grep -i "ftrace-error" | head -10
```

## Examples

```bash
$ dmesg | grep -i "ftrace-error" | tail -5
[12345.678] kernel: ftrace-error error detected on device
[12345.679] kernel: ftrace-error subsystem: failed to initialize

$ cat /proc/cmdline
BOOT_IMAGE=/vmlinuz-... root=... ro quiet

# Adjust kernel parameter and reboot
$ echo "<parameter>=<value>" | sudo tee -a /etc/sysctl.d/99-ftrace-error.conf
```
