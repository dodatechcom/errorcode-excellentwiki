---
title: "[Solution] TimescaleDB Access Node Error — How to Fix"
description: "Fix TimescaleDB access node errors by resolving coordinator failures, fixing query routing issues, and recovering from access node crashes"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Access Node Error

TimescaleDB access node errors occur when the coordinator node in a distributed hypertable cluster fails to route queries, manage data nodes, or handle distributed operations.

## Why It Happens

- Access node cannot connect to data nodes
- Query plan generation fails for distributed queries
- Too many concurrent distributed queries
- Access node runs out of memory for query coordination
- Metadata cache is corrupted
- Access node disk space is full

## Common Error Messages

```
ERROR: access node connection failed
```

```
ERROR: distributed query planning failed
```

```
ERROR: access node out of memory
```

```
ERROR: metadata cache corruption
```

## How to Fix It

### 1. Check Access Node Status

```sql
-- Verify access node is functioning
SELECT * FROM timescaledb_information.data_nodes;

-- Check distributed hypertables
SELECT * FROM timescaledb_information.hypertables
WHERE is_distributed = true;

-- Test basic distributed query
SELECT count(*) FROM distributed_events;
```

### 2. Fix Query Routing

```sql
-- Force query to specific data node
SELECT * FROM distributed_events
WHERE time > NOW() - INTERVAL '1 day'
AND _timescaledb_internal.get_chunk_id_for_time('distributed_events', time) IS NOT NULL;

-- Check query plan for distributed query
EXPLAIN ANALYZE
SELECT time_bucket('1 hour', time), avg(data)
FROM distributed_events
WHERE time > NOW() - INTERVAL '1 day'
GROUP BY 1;
```

### 3. Fix Metadata Issues

```sql
-- Refresh metadata cache
SELECT timescaledb维修_metadata_cache();

-- Or restart PostgreSQL to clear cache
-- sudo systemctl restart postgresql

-- Check for orphaned chunks
SELECT * FROM _timescaledb_catalog.chunk
WHERE hypertable_id NOT IN (SELECT id FROM _timescaledb_catalog.hypertable);
```

### 4. Monitor Access Node

```sql
-- Check access node resource usage
SELECT * FROM pg_stat_activity
WHERE query LIKE '%distributed%';

-- Check memory usage
SELECT * FROM pg_stat_activity
WHERE state = 'active';

-- Monitor distributed query performance
SELECT query, mean_exec_time, calls
FROM pg_stat_statements
WHERE query LIKE '%distributed_events%'
ORDER BY mean_exec_time DESC;
```

## Common Scenarios

- **Distributed query times out**: Check data node connectivity and query plans.
- **Access node crashes under load**: Increase memory and connection limits.
- **Metadata corruption**: Restart access node to rebuild cache.

## Prevent It

- Monitor access node resource usage regularly
- Keep data node connections healthy
- Use connection pooling on the access node

## Related Pages

- [TimescaleDB Data Node Error](/tools/timescaledb/timescale-data-node-error)
- [TimescaleDB Multinode Error](/tools/timescaledb/timescale-multinode-error)
- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
