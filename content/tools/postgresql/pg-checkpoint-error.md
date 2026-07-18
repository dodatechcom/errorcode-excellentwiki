---
title: "[Solution] PostgreSQL Checkpoint Completion Too Slow Error — How to Fix"
description: "Fix PostgreSQL slow checkpoint errors by tuning checkpoint parameters, increasing shared_buffers, optimizing WAL settings, and monitoring I/O performance"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
comments: true
---

# PostgreSQL Checkpoint Completion Too Slow Error

This error means PostgreSQL checkpoints are taking longer than expected to complete, causing excessive WAL accumulation and potential performance degradation. Checkpoints are the process where dirty shared buffer pages are flushed to disk.

## Why It Happens

- `shared_buffers` is too large, causing many dirty pages to flush
- `checkpoint_timeout` is too high, creating large checkpoints at once
- Disk I/O throughput is insufficient for the checkpoint write volume
- `max_wal_size` is too low, forcing frequent checkpoints
- The I/O subsystem is shared with other heavy workloads
- `checkpoint_completion_target` is not tuned for smooth I/O spreading
- OS page cache pressure from other processes competes with PostgreSQL I/O
- Checksum verification on pages adds overhead during checkpoint

## Common Error Messages

```
LOG: checkpoint complete: wrote 45213 buffers (27.6%); 0 WAL file(s) added, 0 removed, 3 recycled
LOG: checkpoint took 185.432 seconds
```

```
WARNING: checkpoint request pointed too far back
HINT: Consider increasing checkpoint_timeout or max_wal_size.
```

```
LOG: checkpoints are occurring too frequently (12 seconds apart)
HINT: Consider increasing the checkpoint_timeout parameter.
```

## How to Fix It

### 1. Monitor Checkpoint Performance

```sql
-- Check checkpoint statistics
SELECT
    checkpoints_timed,
    checkpoints_req,
    checkpoint_write_time,
    checkpoint_sync_time,
    buffers_checkpoint,
    buffers_backend
FROM pg_stat_bgwriter;

-- Calculate checkpoint frequency
SELECT
    checkpoints_req,
    checkpoints_timed,
    round(checkpoints_req::numeric / (checkpoints_req + checkpoints_timed) * 100, 1) AS forced_pct
FROM pg_stat_bgwriter;
```

### 2. Tune Checkpoint Parameters

```sql
-- Allow more time between checkpoints (default 5min)
ALTER SYSTEM SET checkpoint_timeout = '15min';

-- Spread checkpoint writes over more time (default 0.5)
ALTER SYSTEM SET checkpoint_completion_target = 0.9;

-- Increase max WAL before forced checkpoint (default 1GB)
ALTER SYSTEM SET max_wal_size = '4GB';

-- Increase min WAL to avoid premature checkpoints
ALTER SYSTEM SET min_wal_size = '1GB';

SELECT pg_reload_conf();
```

### 3. Optimize shared_buffers

```sql
-- Check current setting
SHOW shared_buffers;

-- Typical recommendation: 25% of system RAM
-- For a 16GB server: 4GB
ALTER SYSTEM SET shared_buffers = '4GB';

-- Requires restart
```

### 4. Improve I/O Performance

```bash
# Check I/O scheduler
cat /sys/block/sda/queue/scheduler

# Set deadline scheduler for SSDs
echo deadline | sudo tee /sys/block/sda/queue/scheduler

# Check I/O utilization
iostat -x 1 10

# Consider using a faster disk for PGDATA
# RAID 10 SSDs are recommended for write-heavy workloads
```

### 5. Monitor WAL Accumulation

```sql
-- Check WAL directory size
SELECT pg_size_pretty(sum(size)) AS wal_size
FROM pg_ls_waldir();

-- Check for checkpoints that are falling behind
SELECT
    now() AS current_time,
    pg_current_wal_lsn() AS current_lsn,
    last_checkpoint
FROM pg_stat_bgwriter;
```

## Common Scenarios

- **Checkpoint storm after restart**: After a restart, `shared_buffers` are cold and all pages are dirty. The first checkpoint flushes everything, causing a performance dip. Pre-warm buffers after restart.
- **Bulk data loading**: A large `COPY` or batch insert generates massive dirty pages. Increase `max_wal_size` temporarily during bulk operations.
- **Shared storage bottleneck**: PostgreSQL is on EBS or a NAS with limited IOPS. Upgrade to provisioned IOPS or local SSDs.

## Prevent It

- Monitor `checkpoints_req` relative to `checkpoints_timed`; if forced checkpoints exceed 25%, tune settings
- Use `checkpoint_completion_target = 0.9` to spread checkpoint writes evenly
- Place PostgreSQL on fast local SSDs rather than network storage

## Related Pages

- [PostgreSQL WAL Archiving Error](/tools/postgresql/pg-wal-archiving-error)
- [PostgreSQL Replication Lag](/tools/postgresql/pg-replication-lag)
- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
