---
title: "[Solution] Linux: zfs-pool-error — ZFS pool error"
description: "Fix Linux zfs-pool-error errors. ZFS pool error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["filesystem-error"]
weight: 12
---

# Linux: ZFS Pool Error Error

ZFS pool error errors occur when the ZFS filesystem encounters pool, dataset, or data integrity issues.

## Common Causes

- Pool device failure or removal
- Checksum mismatch from data corruption
- Pool or dataset space exhaustion
- Snapshot or clone conflicts
- ZFS feature flag incompatibility

## How to Fix

### 1. Check Pool Status

```bash
sudo zpool status -v
sudo zpool list
sudo zfs list -r -t filesystem,volume
```

### 2. Check for Errors

```bash
sudo zpool status -x
sudo zpool events -v | tail -20
```

### 3. Repair Pool

```bash
sudo zpool scrub tank
sudo zpool clear tank
sudo zpool replace tank <old-device> <new-device>
```

### 4. Check Dataset Properties

```bash
sudo zfs get all tank | grep -i "pool-error"
```

## Examples

```bash
$ sudo zpool status tank
  pool: tank
 state: ONLINE
  scan: scrub repaired 0B in 00:00:00

$ sudo zfs list
NAME              USED  AVAIL  REFER  MOUNTPOINT
tank              500G   1.5T   200G  /tank
tank/data         300G   1.5T   300G  /tank/data
```
