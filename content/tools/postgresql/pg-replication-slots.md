---
title: "[Solution] PostgreSQL Replication Slot Lagging Behind - Fix WAL Retention"
description: "Fix PostgreSQL replication slot lagging by monitoring slot lag, dropping stale slots, and configuring max_slot_wal_keep_size properly"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
---

# PostgreSQL Replication Slot Lagging Behind

A replication slot lagging behind means the standby server or consumer has not consumed WAL (Write-Ahead Log) segments fast enough, causing the primary to retain WAL files that would otherwise be recycled. This can fill up disk and degrade performance.

## What This Error Means

PostgreSQL replication slots guarantee that WAL data needed by a standby is not removed from the primary. If the standby falls too far behind, the primary keeps accumulating WAL files. You may see warnings like:

```
WARNING: replication slot "my_slot" is lagging behind
```

Or in the server log:

```
LOG: could not remove file "pg_wal/000000010000000000000015": No such file or directory
```

Monitoring tools may report the lag in bytes or segments. The `pg_replication_slots` view tracks this:

```sql
SELECT slot_name, wal_status, safe_wal_size, restart_lsn
FROM pg_replication_slots;
```

## Why It Happens

- The standby server has slow network connectivity to the primary
- The standby is under heavy load and cannot apply WAL fast enough
- A logical replication consumer (like Debezium) is paused or slow
- The replication slot was created but the consumer is no longer running
- `max_slot_wal_keep_size` is not set, allowing unlimited WAL accumulation
- WAL generation rate exceeds the standby's apply rate during peak workloads

## How to Fix It

### 1. Check Current Slot Status

```sql
SELECT
    slot_name,
    plugin,
    slot_type,
    active,
    wal_status,
    pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) AS lag
FROM pg_replication_slots;
```

### 2. Set max_slot_wal_keep_size

```sql
-- Limit WAL retention for replication slots (PostgreSQL 13+)
-- This prevents unlimited disk usage
ALTER SYSTEM SET max_slot_wal_keep_size = '10GB';
SELECT pg_reload_conf();
```

### 3. Drop Stale Replication Slots

```sql
-- If the consumer is gone and you no longer need the slot
SELECT pg_drop_replication_slot('my_stale_slot');
```

### 4. Monitor WAL Directory Size

```bash
# Check WAL directory size
du -sh /var/lib/postgresql/data/pg_wal/

# Monitor WAL file count
ls /var/lib/postgresql/data/pg_wal/ | wc -l
```

### 5. Increase Standby Apply Rate

```bash
# On the standby, check recovery delay
SELECT
    now() - pg_last_xact_replay_timestamp() AS replication_delay;
```

```sql
-- On the primary, check the send rate
SELECT
    client_addr,
    sent_lsn,
    write_lsn,
    flush_lsn,
    replay_lsn,
    pg_size_pretty(pg_wal_lsn_diff(sent_lsn, replay_lsn)) AS replay_lag
FROM pg_stat_replication;
```

### 6. Use pg_sync_replication Cautiously

```sql
-- synchronous_commit = remote_apply provides stronger guarantees
-- but increases replication lag if the standby is slow
ALTER SYSTEM SET synchronous_commit = 'remote_apply';
SELECT pg_reload_conf();
```

## Common Mistakes

- Not monitoring replication slot lag -- unmonitored slots can fill entire disks
- Setting `max_slot_wal_keep_size` too low, causing replication slots to become invalid too quickly
- Forgetting to drop replication slots when decommissioning standby servers
- Not accounting for the WAL generation rate during bulk operations (like `pg_dump` or data loading)
- Assuming logical replication slots behave the same as physical replication slots for WAL retention

## Related Pages

- [PostgreSQL WAL Segment Error](/tools/postgresql/pg-wal-segment-error)
- [PostgreSQL Disk Full](/tools/postgresql/pg-disk-full)
- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)
- [MySQL Replication Error](/tools/mysql/mysql-replication-error)
