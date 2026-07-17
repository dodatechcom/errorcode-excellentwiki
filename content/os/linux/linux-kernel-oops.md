---
title: "[Solution] Linux Kernel Oops — BUG at Line Fix"
description: "Fix Linux Kernel Oops 'BUG at' errors. Diagnose kernel bugs from faulty modules, hardware issues, and corrupted memory."
platforms: ["linux"]
severities: ["critical"]
error-types: ["system-error"]
weight: 5
---

# Linux: Kernel Oops — BUG at

A `Kernel Oops` is a non-fatal kernel error (unlike a panic) where the kernel detects an inconsistency and reports it. The message `BUG at <file>:<line>` specifies exactly which kernel source file and line triggered the assertion. While the system may continue running after an Oops, the kernel is in an unstable state and should be rebooted.

## Common Causes

- Faulty or incompatible kernel module (driver)
- Memory corruption (bad RAM, overclocking)
- Filesystem driver bug or corruption
- Hardware failure (CPU, motherboard, disk controller)
- Kernel bug triggered by specific conditions

## How to Fix

### 1. Capture the Oops Output

```bash
# View kernel messages immediately after the Oops
dmesg | tail -100

# Save the full Oops output for analysis
dmesg > kernel-oops-$(date +%Y%m%d-%H%M%S).log
```

Look for the `BUG:` line and the register dump — this tells you which kernel function triggered the error.

### 2. Identify the Faulty Module

```bash
# Check which modules are loaded
lsmod | grep -i <module_name>

# Look at the Oops for "EIP" or "RIP" pointing to a module
# Example output:
# RIP: 0010:[<ffffffffa03e2000>]  [<ffffffffa03e2000>] faulty_module+0x10/0x50

# Unload the suspected module
sudo modprobe -r faulty_module

# Blacklist it to prevent loading on boot
echo "blacklist faulty_module" | sudo tee /etc/modprobe.d/blacklist-faulty.conf
```

### 3. Test RAM for Errors

```bash
# Install memtester
sudo apt install memtester    # Debian/Ubuntu
sudo dnf install memtester    # Fedora/RHEL

# Test memory
sudo memtester 1G 5

# Reboot and use Memtest86+ from GRUB
# At GRUB menu, select "Memtest86+"
```

### 4. Check Hardware with dmesg

```bash
# Look for hardware errors
dmesg | grep -iE 'error|fault|fail|hardware'

# Check disk health
sudo smartctl -H /dev/sda
sudo smartctl -l error /dev/sda

# Check CPU errors
dmesg | grep -i 'mce'   # Machine Check Exception
```

### 5. Boot with a Previous Kernel

```bash
# At GRUB, select "Advanced options" and choose an older kernel
# Remove the current kernel
sudo apt remove linux-image-$(uname -r)
sudo apt autoremove
```

### 6. Disable Kernel Module Features

```bash
# Pass module options at boot
# Edit GRUB_CMDLINE_LINUX in /etc/default/grub
sudo nano /etc/default/grub

# Example: disable ACPI for testing
# GRUB_CMDLINE_LINUX="acpi=off noapic"

sudo update-grub
```

### 7. Report the Kernel Bug

```bash
# Install kernel debug symbols (if available)
sudo apt install linux-image-$(uname -r)-dbgsym

# Use scripts from the kernel source to decode the Oops
# Install kernel build tools
sudo apt install linux-headers-$(uname -r)

# Report to bugzilla.kernel.org with the full Oops output
```

## Examples

```
BUG: unable to handle kernel NULL pointer dereference at 0000000000000010
IP: [<ffffffffa03e2000>] faulty_module+0x10/0x50 [faulty_module]
PGD 0 
Oops: 0002 [#1] SMP
```

```
BUG: scheduling while atomic: swapper/0/0/0x00000200
Modules linked in: ...
CPU: 0 PID: 0 Comm: swapper/0 Tainted: G        W
```

## Related Errors

- [Kernel panic]({{< relref "/os/linux/kernel-panic2" >}}) — Fatal kernel error
- [Kernel tainted warning]({{< relref "/os/linux/linux-kernel-tainted" >}}) — Kernel running with tainted modules
- [Segmentation fault]({{< relref "/os/linux/segfault11" >}}) — Userspace memory access violation
