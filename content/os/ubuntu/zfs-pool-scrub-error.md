---
title: "ZFS Pool Scrub Error"
description: "ZFS pool scrub operation fails or reports errors"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# ZFS Pool Scrub Error

ZFS pool scrub operation fails or reports errors

## Common Causes

- Disk read errors during scrub
- Checksum mismatches detected
- Pool in degraded state cannot complete scrub
- Insufficient memory for scrub operation

## How to Fix

1. Check scrub status: `zpool status -v <pool>`
2. Run scrub: `zpool scrub <pool>`
3. Check disk health: `sudo smartctl -a /dev/sdX`
4. Replace failed device: `zpool replace <pool> /dev/old /dev/new`

## Examples

```bash
# Start scrub
sudo zpool scrub tank

# Check scrub status
zpool status tank

# Check disk health
sudo smartctl -a /dev/sda
```
