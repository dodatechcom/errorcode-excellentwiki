---
title: "Fix Linux: multipath-io-error -- multipath I/O error in Linux"
description: "Fix multipath I/O errors caused by path failures or configuration issues on Linux."
os: ["linux"]
error-types: [["disk", "storage"]]
severities: [["error", "warning"]]
---

Multipath I/O errors occur when the DM multipath layer fails to route I/O through available paths to storage.

## Common Causes
- All paths to LUN are down
- SCSI reservation conflicts
- Storage array failover failure
- Incorrect multipath.conf settings

## How to Fix
1. Check multipath status:
   multipathd show paths
   multipathd show map
2. Verify SCSI devices:
   ls -la /dev/mapper/
   cat /proc/scsi/scsi
3. Rescan SCSI buses:
   echo 1 > /sys/class/scsi_device/host0/rescan
4. Reload multipath configuration:
   multipathd reconfigure

## Examples
### Common Error Message
multipath: error in getprio\n
mpath0: remaining active paths: 0
