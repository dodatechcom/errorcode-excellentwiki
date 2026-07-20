---
title: "[Solution] Linux: kernel-panic — kernel panic"
description: "Fix Linux kernel-panic errors. kernel panic with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["process-error"]
weight: 14
---
# Linux: Kernel Panic

A kernel panic is a safety measure where the kernel halts the system after detecting a fatal, unrecoverable error. It is the Linux equivalent of a Windows "Blue Screen of Death."

## Common Causes

- Faulty hardware (bad RAM, CPU issues, overheating)
- Buggy kernel drivers or modules
- Filesystem corruption at the kernel level
- Attempting to access invalid memory addresses
- Kernel NULL pointer dereference
- Out-of-date firmware or BIOS

## How to Fix

### 1. Capture Panic Messages

```bash
# If system is still accessible before crash
dmesg --level=emerg,alert,crit | tail -50

# Check logs after reboot
journalctl -k -p emerg -b -1
```

### 2. Check Hardware

```bash
# Memory test
sudo memtester 1G 1

# CPU stress test
sudo apt install stress
stress --cpu 4 --timeout 30

# Check temperatures
sudo sensors
```

### 3. Update Kernel

```bash
sudo apt update && sudo apt upgrade
sudo apt install linux-image-generic
```

### 4. Boot with Different Kernel Parameters

Add to GRUB_CMDLINE_LINUX:
- `acpi=off` for ACPI-related panics
- `nomodeset` for graphics-related panics
- `memtest` for memory issues

```bash
sudo update-grub
```

### 5. Configure kdump

```bash
sudo apt install kdump-tools
sudo systemctl enable kdump-tools
```

## Examples

```bash
$ dmesg --level=emerg
[12345.678] Kernel panic - not syncing: Fatal exception
[12345.678] CPU: 0 PID: 1234 Comm: myapp Tainted: P           O
[12345.678] Hardware name: Dell Inc. PowerEdge R740/0FDM5W
[12345.678] Call Trace:
[12345.678]  <NMI>
[12345.678]  panic+0x101/0x2e0
[12345.678]  oops_end+0xb3/0xc0
```
