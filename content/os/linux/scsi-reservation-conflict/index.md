---
title: "Fix Linux: scsi-reservation-conflict -- SCSI reservation conflict in Linux"
description: "Resolve SCSI reservation conflicts causing I/O failures on Linux systems."
os: ["linux"]
error-types: [["disk", "storage"]]
severities: [["error", "warning"]]
---

SCSI reservation conflicts occur when multiple hosts attempt to reserve the same LUN simultaneously, blocking I/O operations.

## Common Causes
- Multiple hosts accessing same LUN without cluster software
- Persistent reservation not cleared after failover
- Stale SCSI registrations from crashed hosts
- SAN fabric path issues

## How to Fix
1. Check current reservations:
   sg_persist -r /dev/sdX
2. Clear reservations from one host:
   sg_persist --clear /dev/sdX
3. Check SCSI device status:
   cat /proc/scsi/scsi
4. Force release with bus reset:
   echo 1 > /sys/class/scsi_device/X:0:0:0/device/reset

## Examples
### Common Error Message
sd 0:0:0:0: [sda] FAILED\n
Key=0x000000ff  scope=3  type=0x00
