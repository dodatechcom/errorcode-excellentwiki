---
title: "ZFS Send/Receive Replication Error"
description: "ZFS send/receive replication between pools fails"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# ZFS Send/Receive Replication Error

ZFS send/receive replication between pools fails

## Common Causes

- Source and destination pools incompatible versions
- Incremental replication stream corrupted
- Insufficient space on receiving pool
- Network interruption during stream transfer

## How to Fix

1. Check pool versions: `zpool get version`
2. Use full send: `zfs send <snap> | zfs recv <dest>`
3. Check available space: `zfs list -o space <pool>`
4. Compress stream: `zfs send <snap> | gzip | zfs recv <dest>`

## Examples

```bash
# Full ZFS replication
sudo zfs send tank/data@migrate | sudo zfs recv backup/data

# Incremental replication
sudo zfs send -i tank/data@migrate tank/data@new | sudo zfs recv backup/data

# Check receiving pool space
zfs list -o space backup
```
