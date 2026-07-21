---
title: "[Solution] Linux: disk-hba-error -- host bus adapter error"
description: "Fix Linux disk HBA errors. Host bus adapter firmware or driver failure on storage server."
os: ["linux"]
error-types: ["disk-error"]
severities: ["error"]
---

# Linux: Disk HBA Error

HBA errors indicate problems with the Host Bus Adapter connecting system to storage.

## Common Causes

- HBA firmware incompatibility with kernel driver
- Optical transceiver failure in FC HBA
- PCIe slot power or link issues
- HBA BIOS/UEFI configuration mismatch
- Driver module not loaded after kernel update

## How to Fix

### 1. Check HBA Status

```bash
sudo lspci | grep -i fibre
sudo dmesg | grep -i hba
cat /sys/class/fc_host/host*/port_state
```

### 2. Reset HBA

```bash
echo 1 | sudo tee /sys/class/scsi_host/host0/issue_lip
sudo systemctl restart multipathd
```

### 3. Update HBA Driver

```bash
modinfo qla2xxx
sudo modprobe -r qla2xxx && sudo modprobe qla2xxx
```

## Examples

```bash
$ cat /sys/class/fc_host/host0/port_state
Linkdown
$ sudo dmesg | grep -i qla
[1234.567] qla2xxx 0000:03:00.0: Firmware error - 0x1234
[1234.568] qla2xxx 0000:03:00.0: ISP2277: Firmware crashed
```
