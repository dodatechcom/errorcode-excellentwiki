---
title: "Fix Linux: nvme-controller-reset -- NVMe controller reset in Linux"
description: "Fix NVMe controller resets causing storage disconnections on Linux systems."
os: ["linux"]
error-types: [["disk"]]
severities: [["error", "warning"]]
---

NVMe controller resets occur when the controller becomes unresponsive, triggering an automatic reset by the NVMe subsystem.

## Common Causes
- Controller firmware crash
- PCIe link instability or errors
- Thermal throttling of NVMe drive
- Power management issues

## How to Fix
1. Check NVMe error log:
   nvme smart-log /dev/nvme0
   dmesg | grep -i nvme
2. Disable power management:
   nvme set-feature /dev/nvme0 -f 0x01 -v 0
3. Check PCIe link status:
   lspci -vv -s 02:00.0
4. Update NVMe firmware:
   nvme fw-download /dev/nvme0 --fw=firmware.bin

## Examples
### Common Error Message
nvme nvme0: controller reset\n
NVMe: Abort I/O QID 1
