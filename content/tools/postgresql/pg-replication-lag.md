---
title: "[Solution] PostgreSQL Replication Lag Exceeds Threshold — How to Fix"
description: "Fix PostgreSQL replication lag by optimizing WAL generation, tuning replica settings, monitoring lag metrics, and resolving network bottlenecks"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
comments: true
---

# PostgreSQL Replication Lag Exceeds Threshold

This error means the standby (replica) server has fallen too far behind the primary in applying WAL (Write-Ahead Log) records. When lag exceeds the configured threshold, monitoring alerts fire and read traffic may be redirected away from the replica.

## Why It Happens

- The replica has insufficient I/O throughput to keep up with WAL generation
- Network bandwidth between primary and replica is saturated
- Large batch operations on the primary generate excessive WAL
- The replica is running expensive queries that compete with WAL replay
- `max_wal_senders` or `wal_keep_size` is too low on the primary
- The standby server's `hot_standby_feedback` is interfering with vacuum
- Replication slot on the primary has accumulated too much WAL
- CPU bottleneck on the replica prevents fast WAL replay

## Common Error Messages

```
WARNING: replication delay exceeds 60000ms (current: 125000ms)
```

```
FATAL: terminating connection due to replication timeout
```

```
LOG: standby replication slot "replica_slot" is now active, lag: 1200 MB
```

## How to Fix It

### 1. Monitor Current Replication Lag

```sql
-- On the primary: check replication status
SELECT
    client_addr,
    state,
    sent_lsn,
    write_lsn,
    flush_lsn,
    replay_lsn,
    pg_wal_lsn_diff(sent_lsn, replay_lsn) AS lag_bytes
FROM pg_stat_replication;
```

```sql
-- On the replica: check recovery status
SELECT
    now() - pg_last_xact_replay_timestamp() AS replication_lag,
    pg_last_wal_receive_lsn() AS receive_lsn,
    pg_last_wal_replay_lsn() AS replay_lsn;
```

### 2. Tune WAL Settings on Primary

```sql
-- Increase WAL keep size (in MB)
ALTER SYSTEM SET wal_keep_size = 2048;

-- Check max_wal_senders
SHOW max_wal_senders;
ALTER SYSTEM SET max_wal_senders = 10;
SELECT pg_reload_conf();
```

### 3. Optimize Replica Performance

```sql
-- On replica: reduce resource contention
ALTER SYSTEM SET max_parallel_workers = 4;
ALTER SYSTEM SET max_parallel_workers_per_gather = 2;

-- Allow replica to use hot_standby queries without feedback lag
ALTER SYSTEM SET hot_standby_feedback = on;
ALTER SYSTEM SET max_standby_streaming_delay = 30s;
SELECT pg_reload_conf();
```

### 4. Use a Replication Slot to Prevent WAL Cleanup

```sql
-- Create a replication slot on the primary
SELECT pg_create_physical_replication_slot('replica_slot');

-- On the replica, configure the slot
ALTER SYSTEM SET primary_slot_name = 'replica_slot';
SELECT pg_reload_conf();
```

### 5. Monitor and Alert on Lag

```sql
-- Create a monitoring query
CREATE OR REPLACE VIEW replication_lag_monitor AS
SELECT
    client_addr,
    state,
    pg_wal_lsn_diff(sent_lsn, replay_lsn) AS lag_bytes,
    pg_size_pretty(pg_wal_lsn_diff(sent_lsn, replay_lsn)) AS lag_pretty,
    replay_lag
FROM pg_stat_replication;

-- Alert when lag exceeds 100MB
SELECT * FROM replication_lag_monitor
WHERE lag_bytes > 104857600;
```

## Common Scenarios

- **Bulk data load on primary**: A `COPY` or batch `INSERT` of millions of rows generates large WAL bursts. Throttle the load or schedule it during low-traffic periods.
- **Replica overloaded with analytics**: Long analytical queries on the replica block WAL replay. Move analytics to a separate reporting instance.
- **Network saturation**: The WAN link between primary and replica data centers is at capacity. Upgrade bandwidth or implement WAL compression with `wal_compression = on`.

## Prevent It

- Monitor replication lag continuously and alert when it exceeds 30 seconds
- Use `wal_compression = on` to reduce WAL volume over slow networks
- Keep batch operations on the primary reasonably sized and throttled

## Related Pages

- [PostgreSQL WAL Archiving Error](/tools/postgresql/pg-wal-archiving-error)
- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)
- [PostgreSQL Checkpoint Error](/tools/postgresql/pg-checkpoint-error)
