---
title: "[Solution] TimescaleDB Backup Error — How to Fix"
description: "Fix TimescaleDB backup errors by resolving pg_basebackup failures, fixing continuous backup issues, and handling chunk backup problems"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Backup Error

TimescaleDB backup errors occur when using pg_basebackup, pg_dump, or continuous archiving to back up TimescaleDB databases.

## Why It Happens

- pg_basebackup fails due to WAL accumulation
- pg_dump is too slow for large hypertables
- Backup disk space is insufficient
- Replication slot is not created for continuous backup
- Backup exceeds timeout limits
- Compression fails during backup

## Common Error Messages

```
ERROR: base backup failed
```

```
ERROR: WAL archiving failed
```

```
ERROR: backup disk space insufficient
```

```
ERROR: pg_dump timed out
```

## How to Fix It

### 1. Use pg_basebackup

```bash
# Basic backup
pg_basebackup -h localhost -p 5432 -U replicator \
  -D /backup/base -Fp -Xs -P -R

# Backup with compression
pg_basebackup -h localhost -p 5432 -U replicator \
  -D /backup/base -Ft -z -Xs -P

# Backup to specific WAL position
pg_basebackup -h localhost -p 5432 -U replicator \
  -D /backup/base -Fp -Xs -P --wal-method=stream
```

### 2. Configure Continuous Archiving

```sql
-- On primary: configure WAL archiving
ALTER SYSTEM SET archive_mode = on;
ALTER SYSTEM SET archive_command = 'cp %p /backup/wal/%f';
SELECT pg_reload_conf();

-- Create replication slot for backup
SELECT pg_create_physical_replication_slot('backup_slot');
```

### 3. Backup Hypertables Efficiently

```bash
# pg_dump with parallel workers
pg_dump -h localhost -p 5432 -U postgres \
  -d timescaledb -Fc -j 4 -f /backup/timescaledb.dump

# Backup specific hypertable only
pg_dump -h localhost -p 5432 -U postgres \
  -d timescaledb -t sensor_data -Fc -f /backup/sensor_data.dump

# Restore from dump
pg_restore -h localhost -p 5432 -U postgres \
  -d timescaledb -j 4 /backup/timescaledb.dump
```

### 4. Monitor Backup Status

```bash
# Check backup progress
ls -la /backup/base/

# Check WAL archive status
ls -la /backup/wal/ | wc -l

# Verify backup integrity
pg_verifybackup /backup/base
```

## Common Scenarios

- **pg_basebackup is slow on large DB**: Use `-Ft` for tar format with compression.
- **WAL files accumulate during backup**: Ensure `archive_command` is working.
- **Restore fails**: Verify TimescaleDB extension is installed on target.

## Prevent It

- Schedule regular backups with pg_basebackup or pg_dump
- Test backup restoration periodically
- Monitor backup disk space and WAL retention

## Related Pages

- [TimescaleDB Restore Error](/tools/timescaledb/timescale-restore-error)
- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Migration Error](/tools/timescaledb/timescale-migration-error)
