---
title: "[Solution] Linux: disk-timeout — disk timeout error"
description: "Fix Linux disk-timeout errors. disk timeout error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 10
---
# Linux: Disk Timeout Error

A disk timeout error occurs when a storage device fails to complete an I/O request within the kernel's deadline (typically 30-60 seconds). The kernel logs "task blocked for more than 120 seconds" messages and may kill processes.

## Common Causes

- Failing hard drive with mechanical wear causing long seek times
- Loose or faulty SATA/SAS cables causing intermittent disconnects
- Aggressive power management (APM, NCQ) on the drive or controller
- Overheating causing drive throttling or temporary unresponsiveness
- Driver bugs or controller firmware issues

## How to Fix

### 1. Check Kernel Messages

```bash
dmesg | grep -iE "timeout|blocked for more than" | tail -30
journalctl -k -p err | grep -iE "timeout|blocked"
```

### 2. Check Disk Health

```bash
sudo smartctl -a /dev/sdX | grep -E "Reallocated|Pending|Uncorrectable|CRC"
sudo smartctl -H /dev/sdX
```

### 3. Increase I/O Timeout

```bash
# Check current timeout
cat /sys/block/sdX/device/timeout

# Increase to 180 seconds
echo 180 | sudo tee /sys/block/sdX/device/timeout

# Make persistent
echo 'ACTION=="add", SUBSYSTEM=="scsi", ATTR{device/timeout}="180"' | sudo tee /etc/udev/rules.d/50-io-timeout.rules
```

### 4. Disable NCQ

```bash
# Add to kernel cmdline in /etc/default/grub: libata.force=noncq
sudo update-grub
```

### 5. Check Cables and Connections

```bash
# Reseat SATA cables and check link speed
sudo dmesg | grep -i "SATA link"
```

## Examples

```bash
$ dmesg | grep "blocked for more than"
[12345.678] INFO: task kworker/0:1:456 blocked for more than 120 seconds.
[12345.678]       Tainted: P           O    5.15.0-86-generic

$ cat /sys/block/sda/device/timeout
30
$ echo 180 | sudo tee /sys/block/sda/device/timeout
180
```
