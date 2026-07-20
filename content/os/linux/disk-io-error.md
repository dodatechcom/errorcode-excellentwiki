---
title: "[Solution] Linux: disk-io-error — disk I/O error"
description: "Fix Linux disk-io-error errors. disk I/O error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["disk"]
weight: 12
---
# Linux: Disk I/O Error

A disk I/O error (EIO, errno 5) means the kernel could not read from or write to a storage device. This typically indicates hardware failure or filesystem corruption.

## Common Causes

- Failing hard drive with bad sectors or mechanical failure
- Loose or faulty SATA/SAS cables causing transmission errors
- Power supply issues causing voltage drops to the drive
- Filesystem corruption on the affected partition
- Disk controller failure or driver incompatibility

## How to Fix

### 1. Check Kernel Logs

```bash
dmesg | grep -iE "I/O error|Buffer I/O|failed command" | tail -30
journalctl -k -p err | grep -iE "ata|sd|nvme" | tail -20
```

### 2. Identify the Failing Device

```bash
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE,MODEL
```

### 3. Check SMART Health

```bash
sudo smartctl -H /dev/sdX
sudo smartctl -l error /dev/sdX
sudo smartctl -A /dev/sdX | grep -E "Reallocated|Pending|Uncorrectable|CRC"
```

### 4. Run Filesystem Check

```bash
sudo umount /dev/sdX 2>/dev/null
sudo fsck -f /dev/sdX
```

### 5. Attempt Data Recovery

```bash
sudo ddrescue -d -r3 /dev/sdX /dev/sdY /tmp/rescue.log
```

## Examples

```bash
$ dmesg | grep "I/O error"
[51234.567] sd 0:0:0:0: [sda] tag#0 FAILED Result: hostbyte=DID_OK driverbyte=DRIVER_OK
[51234.567] sd 0:0:0:0: [sda] Sense Key : Medium Error [current]
[51234.567] sd 0:0:0:0: [sda] Add. Sense: Unrecovered read error

$ sudo smartctl -H /dev/sda
SMART overall-health self-assessment test result: FAILED
```
