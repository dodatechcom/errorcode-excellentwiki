---
title: "[Solution] Linux: kernel-tainted — Fix kernel tainted warning"
description: "Fix Linux kernel-tainted errors. Warning kernel tainted with non-GPL module loaded."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---

# Linux: Kernel Tainted Error

Kernel tainted errors occur when the kernel encounters issues with tainted operations or subsystem components.

## Common Causes

- Hardware incompatibility or failure affecting tainted
- Kernel module or driver bugs in the tainted subsystem
- Insufficient system resources or configuration limits
- Firmware or microcode issues
- Kernel parameter misconfiguration

## How to Fix

### 1. Check Kernel Logs

```bash
sudo dmesg | grep -i "tainted" | tail -30
sudo journalctl -k --no-pager -n 50 | grep -i "tainted"
```

### 2. Check Kernel Parameters

```bash
cat /proc/cmdline
sysctl -a 2>/dev/null | grep -i "tainted"
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
sudo lspci -vvv | grep -i "tainted" | head -20
sudo lsusb -v 2>/dev/null | grep -i "tainted" | head -10
```

## Examples

```bash
$ dmesg | grep -i "tainted" | tail -5
[12345.678] kernel: tainted error detected on device
[12345.679] kernel: tainted subsystem: failed to initialize

$ cat /proc/cmdline
BOOT_IMAGE=/vmlinuz-... root=... ro quiet

# Adjust kernel parameter and reboot
$ echo "<parameter>=<value>" | sudo tee -a /etc/sysctl.d/99-tainted.conf
```
