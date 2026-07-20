---
title: "[Solution] Linux: kernel-percpu-error — Per-CPU memory allocation error"
description: "Fix Linux kernel-percpu-error errors. Per-CPU memory allocation error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["kernel-error"]
weight: 10
---

# Linux: Kernel Percpu Error Error

Kernel percpu error errors occur when the kernel encounters issues with percpu error operations or subsystem components.

## Common Causes

- Hardware incompatibility or failure affecting percpu error
- Kernel module or driver bugs in the percpu error subsystem
- Insufficient system resources or configuration limits
- Firmware or microcode issues
- Kernel parameter misconfiguration

## How to Fix

### 1. Check Kernel Logs

```bash
sudo dmesg | grep -i "percpu-error" | tail -30
sudo journalctl -k --no-pager -n 50 | grep -i "percpu-error"
```

### 2. Check Kernel Parameters

```bash
cat /proc/cmdline
sysctl -a 2>/dev/null | grep -i "percpu-error"
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
sudo lspci -vvv | grep -i "percpu-error" | head -20
sudo lsusb -v 2>/dev/null | grep -i "percpu-error" | head -10
```

## Examples

```bash
$ dmesg | grep -i "percpu-error" | tail -5
[12345.678] kernel: percpu-error error detected on device
[12345.679] kernel: percpu-error subsystem: failed to initialize

$ cat /proc/cmdline
BOOT_IMAGE=/vmlinuz-... root=... ro quiet

# Adjust kernel parameter and reboot
$ echo "<parameter>=<value>" | sudo tee -a /etc/sysctl.d/99-percpu-error.conf
```
