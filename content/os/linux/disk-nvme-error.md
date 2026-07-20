---
title: "[Solution] Linux: disk-nvme-error — NVMe disk error"
description: "Fix Linux disk-nvme-error errors. NVMe disk error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["disk"]
weight: 12
---
# Linux: NVMe Error

NVMe errors indicate problems with Non-Volatile Memory Express SSDs. These range from command timeouts to fatal controller errors.

## Common Causes

- NVMe firmware bugs or incompatibility with kernel version
- PCIe link issues (training failures, width/speed downgrades)
- Power management transitions causing device timeouts
- Drive reaching endurance limits (write wear out)
- Overheating causing thermal throttling or shutdown

## How to Fix

### 1. Check NVMe Device

```bash
sudo nvme list
sudo nvme list-subsys /dev/nvme0
sudo nvme error-log /dev/nvme0
```

### 2. Check Kernel Messages

```bash
dmesg | grep -i nvme | tail -40
```

### 3. Check PCIe Link

```bash
sudo lspci -vvvs $(readlink /sys/class/nvme/nvme0/device | cut -d'/' -f4) | grep -E "Speed|Width|LnkSta"
```

### 4. Reset NVMe Controller

```bash
echo 1 | sudo tee /sys/class/nvme/nvme0/device/remove
echo 1 | sudo tee /sys/bus/pci/rescan
```

## Examples

```bash
$ sudo nvme error-log /dev/nvme0
Error Log Entries for device:nvme0 entries:12
 Entry[0]
 error_count    : 5
 opcode         : 0x02
 sqid           : 0
 status_code    : 0x404 (Internal Device Error)

$ dmesg | grep nvme
[ 1234.567] nvme nvme0: I/O 123 QID 2 timeout, aborting
[ 1234.789] nvme nvme0: Abort status: 0x0
[ 1235.012] nvme nvme0: I/O 123 QID 2 timeout, reset controller
```
