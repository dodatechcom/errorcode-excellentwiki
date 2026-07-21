---
title: "PostgreSQL WAL Segment Error"
description: "WAL (Write-Ahead Log) segment cannot be archived or recycled"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PostgreSQL WAL Segment Error

WAL (Write-Ahead Log) segment cannot be archived or recycled

## Common Causes

- WAL archive command failing
- archive_command returns non-zero exit code
- pg_wal directory full of WAL segments
- WAL segment naming conflict

## How to Fix

1. Check archive status: `SELECT * FROM pg_stat_archiver;`
2. Verify archive_command works: test it manually
3. Clean old WAL: `pg_archivecleanup /path/to/archive <oldest_wal>`
4. Check pg_wal size: `du -sh /var/lib/postgresql/*/main/pg_wal/`

## Examples

```sql
-- Check WAL archiver status
SELECT * FROM pg_stat_archiver;

-- Check WAL configuration
SHOW archive_mode;
SHOW archive_command;
```
