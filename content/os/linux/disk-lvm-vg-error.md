---
title: "[Solution] Linux: disk-lvm-vg-error — LVM volume group error"
description: "Fix Linux disk-lvm-vg-error errors. LVM volume group error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: LVM Volume Group Error

LVM volume group (VG) errors occur when metadata spanning multiple physical volumes becomes inconsistent or a PV is missing.

## Common Causes

- One or more physical volumes in the VG are missing or failed
- VG metadata corruption after unclean shutdown
- LVM filter in /etc/lvm/lvm.conf excluding a needed device
- Duplicate PV UUIDs after cloning disks or restoring from backup

## How to Fix

### 1. Check VG Status

```bash
sudo vgs -v
sudo vgdisplay -v
```

### 2. Scan and Activate

```bash
sudo vgscan
sudo vgchange -ay <vg_name>
```

### 3. Fix Duplicate PV UUIDs

```bash
sudo pvchange -u /dev/sdX
```

### 4. Restore from Backup

```bash
sudo vgcfgrestore -f /etc/lvm/archive/<vg_name>_<timestamp>.vg <vg_name>
```

## Examples

```bash
$ sudo vgs
  WARNING: Couldn't find device with uuid XXXXXX-YYYY-ZZZZ.
  VG    #PV #LV #SN Attr   VSize   VFree
  vg01    2   3   0 wz-pn- 600.00g 20.00g

$ sudo vgchange -ay vg01
  1 logical volume(s) in volume group "vg01" now active
```
