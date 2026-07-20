---
title: "[Solution] Linux: disk-scsi-error — SCSI disk error"
description: "Fix Linux disk-scsi-error errors. SCSI disk error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["disk"]
weight: 12
---
# Linux: SCSI Disk Error

SCSI errors indicate problems with SCSI devices (including SATA via ATA/SATA pass-through, SAS, Fibre Channel, iSCSI).

## Common Causes

- SCSI command timeout or abort due to unresponsive device
- Target device returned CHECK CONDITION with a sense key error
- Bus reset or device reset events affecting multiple drives
- Driver issues with mpt3sas, megaraid_sas, or other SCSI HBA drivers

## How to Fix

### 1. Identify SCSI Errors

```bash
dmesg | grep -iE "scsi|sd |sas|mpt" | grep -iE "error|fail|timeout|abort" | tail -30
```

### 2. Check SCSI Devices

```bash
cat /proc/scsi/scsi
sudo lsscsi
```

### 3. Reset SCSI Device

```bash
echo "scsi remove-single-device 0 0 0 0" | sudo tee /proc/scsi/scsi
echo "scsi add-single-device 0 0 0 0" | sudo tee /proc/scsi/scsi
```

### 4. Rescan SCSI Bus

```bash
for host in /sys/class/scsi_host/host*/scan; do
    echo "- - -" | sudo tee $host
done
```

## Examples

```bash
$ dmesg | grep scsi | grep error
[ 3456.789] sd 0:0:0:0: [sda] FAILED Result: hostbyte=DID_BAD_TARGET driverbyte=DRIVER_OK

$ cat /proc/scsi/scsi
Attached devices:
Host: scsi0 Channel: 00 Id: 00 Lun: 00
  Vendor: ATA      Model: ST1000DM003-1CH1 Rev: CC47
  Type:   Direct-Access                    ANSI  SCSI revision: 05
```
