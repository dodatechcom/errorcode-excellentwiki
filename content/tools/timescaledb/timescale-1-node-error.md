---
title: "[Solution] TimescaleDB 1 Node Error — How to Fix"
description: "Fix TimescaleDB single-node errors by resolving standalone deployment issues, fixing resource limits, and recovering from node failures"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB 1 Node Error

TimescaleDB single-node errors occur when running TimescaleDB on a single PostgreSQL instance. Single-node deployments have specific limitations and failure modes.

## Why It Happens

- Single node is a single point of failure
- Disk space is exhausted on the only node
- Memory is insufficient for all operations
- No replication for disaster recovery
- Background workers compete for limited resources
- Hypertable chunk count grows unbounded

## Common Error Messages

```
FATAL: no data nodes available for distributed query
```

```
ERROR: insufficient resources on single node
```

```
ERROR: disk full on single node
```

```
FATAL: too many background workers for single node
```

## How to Fix It

### 1. Optimize Single-Node Configuration

```ini
# In postgresql.conf - optimized for single node
shared_buffers = '4GB'
work_mem = '256MB'
maintenance_work_mem = '2GB'
effective_cache_size = '12GB'
max_connections = 100
max_worker_processes = 8
timescaledb.max_background_workers = 4
```

### 2. Manage Storage on Single Node

```sql
-- Enable compression to save space
ALTER TABLE sensor_data SET (
  timescaledb.compress,
  timescaledb.compress_segmentby = 'sensor_id'
);

-- Add compression policy
SELECT add_compression_policy('sensor_data', INTERVAL '7 days');

-- Add retention policy to manage growth
SELECT add_retention_policy('sensor_data', INTERVAL '90 days');
```

### 3. Monitor Single-Node Health

```sql
-- Check disk usage
SELECT pg_size_pretty(pg_database_size('timescaledb'));

-- Check chunk count
SELECT hypertable_name, num_chunks
FROM timescaledb_information.hypertables;

-- Check background worker status
SELECT * FROM pg_stat_activity
WHERE backend_type LIKE '%TimescaleDB%';
```

### 4. Plan for High Availability

```bash
# Set up streaming replication for HA
# Primary node:
SELECT pg_create_physical_replication_slot('standby1');

# Standby node configuration:
# primary_conninfo = 'host=primary_ip port=5432'
# primary_slot_name = 'standby1'
```

## Common Scenarios

- **Single node disk full**: Enable compression and retention policies.
- **Single node performance degrades**: Optimize configuration and add monitoring.
- **Single node failure causes outage**: Set up replication for high availability.

## Prevent It

- Implement regular backups with pg_basebackup
- Set up monitoring for disk, memory, and connection usage
- Plan migration path to multi-node if growth requires it

## Related Pages

- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Connection Error](/tools/timescaledb/timescale-connection-error)
- [TimescaleDB Multinode Error](/tools/timescaledb/timescale-multinode-error)
