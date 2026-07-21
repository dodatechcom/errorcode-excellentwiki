---
title: "[Solution] Linux: lvm-vdo-error -- VDO optimizer failure"
description: "Fix Linux LVM VDO errors. VDO compression or deduplication layer failure."
os: ["linux"]
error-types: ["lvm-error"]
severities: ["error"]
---

# Linux: LVM VDO Error

LVM VDO errors occur when Virtual Data Optimizer encounters compression failures.

## Common Causes

- VDO pool running out of physical space
- Deduplication cache size insufficient
- Compression algorithm encountering unsupported data
- VDO metadata corruption
- Kernel module for VDO not loaded

## How to Fix

### 1. Check VDO Status

```bash
sudo vdo list
sudo vdo status --name <vdo_name>
sudo lvs -a -o +vdo_creation_time
```

### 2. Extend VDO Volume

```bash
sudo vdo extend --name <vdo_name> --vdoLogicalSize 200G
sudo lvextend -L +50G <vg>/<vdo_pool>
```

### 3. Repair VDO

```bash
sudo vdo stop --name <vdo_name>
sudo vdo start --name <vdo_name>
sudo vdo status --name <vdo_name> --compression
```

## Examples

```bash
$ sudo vdo list
vdo_name        vdo_status  logical_volumes
myvdo           running     1
$ sudo vdo status --name myvdo
  VDO status: running
  Compression: enabled
  Deduplication: enabled
  Physical: 50.0G used of 100.0G
```
