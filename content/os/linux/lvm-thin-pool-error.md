---
title: "[Solution] Linux: lvm-thin-pool-error -- thin pool provisioning error"
description: "Fix Linux LVM thin pool errors. Thin pool provisioning or space exhaustion failure."
os: ["linux"]
error-types: ["lvm-error"]
severities: ["error"]
---

# Linux: LVM Thin Pool Error

LVM thin pool errors occur when the thin pool runs out of space or becomes corrupted.

## Common Causes

- Thin pool metadata space exhausted
- Data space in thin pool fully allocated
- Metadata corruption from power loss
- Thin pool not monitoring for space usage
- Automatic extension not configured

## How to Fix

### 1. Check Thin Pool Status

```bash
sudo lvs
sudo lvs -o+data_percent,metadata_percent
sudo dmsetup status <vg>-<pool>
```

### 2. Extend Thin Pool

```bash
sudo lvextend -L +10G <vg>/<pool>
sudo lvextend -l +100%FREE <vg>/<pool>-tpool
```

### 3. Repair Metadata

```bash
sudo lvconvert --repair <vg>/<pool>
sudo thin_check /dev/<vg>/<pool>-tpool
```

## Examples

```bash
$ sudo lvs -o+data_percent,metadata_percent
  LV     VG   Attr       LSize   Data%  Meta%
  data   myvg  twi-aotz-- 50.00g 98.50  100.00
# Metadata at 100% - needs extension
$ sudo lvextend -L +5G myvg/pool-tpool
```
