---
title: "[Solution] TiDB BR Backup Error — How to Fix"
description: "Fix TiDB Backup & Restore (BR) errors when backup or restore operations fail during large-scale data protection"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB BR Backup Error

BR (Backup & Restore) errors occur when TiDB's backup and restore tool fails to create consistent backups or restore data from backup files.

## Why It Happens

- Backup storage is full or unavailable
- TiKV nodes are too busy to create snapshots
- Backup file format is incompatible with TiDB version
- Network bandwidth is insufficient for backup transfer
- GC life time is shorter than backup duration

## Common Error Messages

```
BR: backup failed: unable to create snapshot
```

```
error: restore failed: backup file is corrupted
```

```
br: backup storage is not writable
```

```
error: GC safe point is too old for backup
```

## How to Fix It

### 1. Check BR Status

```bash
br backup full --pd pd:2379 --storage local:///backup/
```

### 2. Extend GC Life Time

```sql
SET GLOBAL tidb_gc_life_time = '24h';
```

### 3. Verify Backup Files

```bash
br validate backup --pd pd:2379 --storage local:///backup/
```

### 4. Restore from Backup

```bash
br restore full --pd pd:2379 --storage local:///backup/
```

## Examples

```
$ br backup full --pd pd:2379 --storage local:///backup/
Full backup success: 100%
Backup duration: 15m30s
Backup size: 50GB
```

## Prevent It

- Ensure sufficient storage for backups
- Schedule backups during low-traffic periods
- Extend GC life time to cover backup duration

## Related Pages

- [TiDB Backup Error](/tools/tidb/tidb-backup-error)
- [TiDB BR Error](/tools/tidb/tidb-br-error)
- [TiDB BR Error Code](/tools/tidb/tidb-br-error-code)
