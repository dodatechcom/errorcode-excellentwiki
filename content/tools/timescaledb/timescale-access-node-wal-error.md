---
title: "[Solution] TimescaleDB Access Node WAL Error"
description: "How to fix TimescaleDB access node WAL errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- WAL files not archived
- WAL archive command failing
- WAL retention too short

## How to Fix

```ini
wal_level = replica
archive_mode = on
archive_command = 'cp %p /archive/%f'
```

## Examples

```sql
SELECT * FROM pg_stat_archiver;
```
