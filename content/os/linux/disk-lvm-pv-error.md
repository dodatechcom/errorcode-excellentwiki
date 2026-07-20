---
title: "[Solution] Linux: disk-lvm-pv-error — LVM physical volume error"
description: "Fix Linux disk-lvm-pv-error errors. LVM physical volume error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: LVM Physical Volume Error

LVM physical volume (PV) errors indicate problems with the underlying block devices used by LVM for storage pools.

## Common Causes

- Physical volume device not connected at boot (external drive, SAN LUN)
- Disk replaced without proper LVM removal procedures
- Partition table changed on a device that is an LVM PV
- PV UUID mismatch or duplicate after disk cloning
- Device mapper issues preventing PV detection

## How to Fix

### 1. Scan for Physical Volumes

```bash
sudo pvscan
sudo pvs -v
```

### 2. Restore PV Metadata

```bash
sudo pvck -d /dev/sdX
sudo pvcreate --restorefile /etc/lvm/backup/<vg_name> /dev/sdX
```

### 3. Handle Missing PVs

```bash
# Remove missing PV from VG
sudo vgreduce --removemissing <vg_name>

# Replace with new PV
sudo pvmove /dev/old_pv /dev/new_pv
sudo vgreduce <vg_name> /dev/old_pv
```

## Examples

```bash
$ sudo pvscan
  PV /dev/sda1   VG vg01         lvm2 [100.00 GiB]
  PV [unknown]   VG vg01         lvm2 [500.00 GiB]
  
$ sudo vgreduce --removemissing vg01
  Removed missing device from volume group vg01
```
