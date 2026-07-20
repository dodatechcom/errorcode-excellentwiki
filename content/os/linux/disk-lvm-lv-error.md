---
title: "[Solution] Linux: disk-lvm-lv-error — LVM logical volume error"
description: "Fix Linux disk-lvm-lv-error errors. LVM logical volume error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: LVM Logical Volume Error

LVM logical volume (LV) errors occur when accessing or activating logical volumes within a volume group.

## Common Causes

- Logical volume not automatically activated after system boot
- Snapshot overflow (100% full, causing invalidation)
- Filesystem on the LV corrupted and needs fsck
- LV device node missing in /dev due to device mapper issues
- LV metadata size mismatch

## How to Fix

### 1. Check LV Status

```bash
sudo lvs -a -o +devices
sudo lvdisplay -m
```

### 2. Activate the LV

```bash
sudo lvchange -ay <vg_name>/<lv_name>
```

### 3. Check Snapshot Status

```bash
sudo lvs -a -o +snap_percent
# Remove invalid snapshot
sudo lvremove <vg_name>/<snap_name>
```

### 4. Extend LV if Full

```bash
sudo lvextend -r -L +10G <vg_name>/<lv_name>
```

## Examples

```bash
$ sudo lvs -a -o +devices,snap_percent
  LV       VG   Attr       LSize  Snap%  Devices
  root     vg01 -wi-a----- 50.00g        /dev/sda1
  snap_r   vg01 swi-a-s--- 10.00g 100.00 /dev/sda1

$ sudo lvremove vg01/snap_r
  Logical volume "snap_r" successfully removed
```
