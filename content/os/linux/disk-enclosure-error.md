---
title: "[Solution] Linux: disk-enclosure-error -- enclosure management error"
description: "Fix Linux disk enclosure errors. SCSI enclosure management error preventing drive monitoring."
os: ["linux"]
error-types: ["disk-error"]
severities: ["error"]
---

# Linux: Disk Enclosure Error

Disk enclosure errors occur when SCSI enclosure services cannot communicate with processor.

## Common Causes

- SES device not responding on SCSI bus
- Enclosure management cable disconnected
- Firmware incompatibility between host and enclosure
- Multipath path failure to enclosure processor
- Enclosure power supply issues

## How to Fix

### 1. Check Enclosure Status

```bash
sudo sg_ses /dev/sg0
sudo lsscsi -g
```

### 2. Scan SCSI Bus

```bash
echo "- - -" | sudo tee /sys/class/scsi_host/host*/scan
sudo rescan-scsi-bus.sh
dmesg | grep -i enclosure
```

### 3. Check Multipath

```bash
sudo multipath -ll
sudo mpathconf --show_config
```

## Examples

```bash
$ sudo lsscsi -g
[0:0:0:0]    disk    SEAGATE  ST4000NM0023     LS04  /dev/sda  /dev/sg0
[0:0:8:0]    enclosu SEAGATE  SHBJ424          LS01  -         /dev/sg8
$ dmesg | grep enclosure
[1234.567] ses 0:0:8:0: enclosure doesn't implement SES
```
