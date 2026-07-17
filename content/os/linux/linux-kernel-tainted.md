---
title: "[Solution] Linux Kernel Tainted Warning — Fix"
description: "Fix Linux 'Kernel is tainted' warnings. Understand taint flags, identify the cause, and resolve proprietary module or hardware issues."
platforms: ["linux"]
severities: ["warning"]
error-types: ["system-error"]
tags: ["kernel-tainted", "taint", "proprietary-module", "kernel-module", "warning"]
weight: 5
---

# Linux: Kernel is tainted

The `Kernel is tainted` message indicates the kernel is running with a "taint" flag set. Tainting means the kernel can no longer guarantee that certain bugs or errors are caused by its own code — a proprietary driver, an overclocked CPU, or certain kernel configurations may be responsible. This warning appears in crash reports and kernel Oops messages to remind developers that the issue may not be a pure kernel bug.

## Common Causes

- Proprietary or out-of-tree kernel module loaded (e.g., NVIDIA driver, VMware/VirtualBox)
- Kernel module forced load (`insmod -f`)
- Machine Check Exception (MCE) from hardware issues
- SMP (multiprocessor) CPU with unsupported configuration
- Module loaded from staging tree
- Workaround for a CPU erratum enabled

## How to Fix

### 1. Check Taint Flags

```bash
# Check if kernel is tainted
cat /proc/sys/kernel/tainted

# The number is a bitmask; decode it
# 1 = proprietary module loaded
# 2 = module forced load
# 4 = SMP with unsupported CPU
# 8 = module loaded from staging tree
# 16 = workaround for CPU erratum
# 32 = MCE occurred
# 256 = module signed with unknown key
```

### 2. Identify the Tainting Module

```bash
# Check which modules are tainting the kernel
cat /proc/modules | grep -E ' \([PFXSL]\)'

# List all loaded modules
lsmod

# Look for out-of-tree modules
for mod in $(lsmod | tail -n +2 | awk '{print $1}'); do
  path=$(modinfo -n $mod 2>/dev/null)
  if [ -n "$path" ] && ! echo "$path" | grep -q '/kernel/'; then
    echo "Out-of-tree: $mod ($path)"
  fi
done
```

### 3. Replace Proprietary Modules

```bash
# Replace NVIDIA proprietary driver with Nouveau (open source)
sudo apt purge nvidia-*
sudo apt install xserver-xorg-video-nouveau

# For other proprietary drivers, check if open-source alternatives exist
sudo apt search <module-name>
```

### 4. Rebuild Signature for Signed Module Issues (Taint flag 256)

```bash
# If Secure Boot is enabled, sign the module
sudo apt install mokutil

# Check Secure Boot status
mokutil --sb-state

# Sign the module
sudo kmodsign sha512 /var/lib/shim-signed/mok/MOK.priv /var/lib/shim-signed/mok/MOK.der /lib/modules/$(uname -r)/kernel/drivers/gpu/drm/nvidia/nvidia.ko
```

### 5. Clear MCE Taint (Taint flag 32)

```bash
# MCE taint means hardware issues were detected
# Check for MCEs
dmesg | grep -i 'mce'

# Test memory
sudo memtester 1G 1

# Check CPU temperature
sensors

# Check system logs for hardware errors
sudo journalctl -k | grep -i 'hardware error'
```

### 6. Suppress the Warning (Not Recommended)

```bash
# You cannot "untaint" the kernel without rebooting
# The only way to clear taint flags is to reboot

# To prevent tainting in the future, avoid:
# - Loading proprietary modules
# - Using insmod -f
# - Overclocking hardware
```

### 7. Verify Kernel Signature

```bash
# Check if the kernel itself is signed
modinfo -F signature $(lsmod | head -1 | awk '{print $1}')

# Verify kernel image signature
sudo mokutil --import /boot/vmlinuz-$(uname -r)
```

## Examples

```bash
$ cat /proc/sys/kernel/tainted
256

# This means a module signed with an unknown key was loaded
# Likely a Secure Boot / MOK issue

$ dmesg | grep taint
[    0.000000] Kernel is tainted by module nvidia loaded with unknown key.
```

```bash
$ cat /proc/sys/kernel/tainted
1

# A proprietary module is loaded (e.g., NVIDIA driver)
```

## Related Errors

- [Kernel Oops]({{< relref "/os/linux/linux-kernel-oops" >}}) — Kernel bug detection
- [Kernel panic]({{< relref "/os/linux/kernel-panic2" >}}) — Fatal system error
- [Kernel module error]({{< relref "/os/linux/linux-kernel-module-error" >}}) — Module loading failures
