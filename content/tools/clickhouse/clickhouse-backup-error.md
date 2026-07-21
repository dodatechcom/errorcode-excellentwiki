---
title: "[Solution] ClickHouse Backup Error"
description: "Fix ClickHouse backup errors when using clickhouse-backup or BACKUP/RESTORE commands"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Backup Error

Backup errors occur when ClickHouse backup operations fail due to resource or configuration issues.

## Common Causes

- Insufficient disk space for backup
- Backup target path not writable
- ClickHouse backup tool not installed
- Backup exceeds timeout limit

## How to Fix

Check backup status:

```bash
clickhouse-backup list
```

Run backup:

```bash
clickhouse-backup create my_backup
```

Check backup disk usage:

```bash
du -sh /var/lib/clickhouse/backups/
```

## Examples

```bash
clickhouse-backup create --tables "default.*" daily_backup_2024
```
