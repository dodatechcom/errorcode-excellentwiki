---
title: "ZFS Dataset Mount Read-Only Error"
description: "ZFS dataset mounted read-only due to pool or dataset errors"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# ZFS Dataset Mount Read-Only Error

ZFS dataset mounted read-only due to pool or dataset errors

## Common Causes

- Pool entered degraded/FAULTED state
- Snapshot rollback left dataset read-only
- Disk errors preventing write access
- Mount option explicitly set to read-only

## How to Fix

1. Check pool status: `zpool status`
2. Check mount options: `mount | grep zfs`
3. Remount read-write: `sudo zfs set readonly=off <dataset>`
4. Clear errors: `zpool clear <pool>`

## Examples

```bash
# Check if dataset is read-only
zfs get readonly tank/mydata

# Remount as read-write
sudo zfs set readonly=off tank/mydata

# Clear pool errors
sudo zpool clear tank
```
