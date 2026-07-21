---
title: "[Solution] Linux: disk-backplane-error -- backplane communication error"
description: "Fix Linux disk backplane errors. Storage backplane communication failure for drives."
os: ["linux"]
error-types: ["disk-error"]
severities: ["error"]
---

# Linux: Disk Backplane Error

Disk backplane errors occur when storage backplane cannot communicate with drives.

## Common Causes

- Backplane expander chip failure
- SAS/SATA link negotiation failure
- Backplane power distribution issue
- Missing or faulty backplane firmware
- Cable or connector damage

## How to Fix

### 1. Check Drive Links

```bash
sudo sg_ses -i /dev/sg0
sudo sas2ircu list
dmesg | grep -i "link reset"
```

### 2. Rescan and Reset

```bash
echo "- - -" | sudo tee /sys/class/scsi_host/host*/scan
sudo ipmitool raw 0x30 0xE2 0x01
```

### 3. Update Firmware

```bash
sudo storcli /c0 show
sudo storcli /c0/callall start
```

## Examples

```bash
$ sudo dmesg | grep -i "link reset"
[5678.123] mptsas: Link reset for host 0
[5678.124] mptsas: ioc0: SAS Link Down timeout
$ sudo storcli /c0 show
Number of drives: 12
Drive Pos: 4, State: Failed
```
