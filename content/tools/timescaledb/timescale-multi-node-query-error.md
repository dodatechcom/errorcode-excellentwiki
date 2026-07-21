---
title: "[Solution] TimescaleDB Multi-Node Query Error — How to Fix"
description: "Fix TimescaleDB multi-node query errors by resolving distributed query failures, fixing cross-node join issues, and handling query pushdown errors"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Multi-Node Query Error

TimescaleDB multi-node query errors occur when queries on distributed hypertables fail to execute across data nodes due to pushdown failures, network issues, or incompatible operations.

## Why It Happens

- Query cannot be pushed down to data nodes (e.g., contains mutable functions)
- Network latency causes query timeouts
- Data node returns incompatible results
- Query uses features not supported in distributed mode
- Foreign server options are misconfigured
- Query plan is not optimized for distributed execution

## Common Error Messages

```
ERROR: could not execute distributed query
```

```
ERROR: query pushdown failed
```

```
ERROR: data node returned incompatible result
```

```
ERROR: distributed query timeout
```

## How to Fix It

### 1. Fix Query Pushdown Issues

```sql
-- Avoid mutable functions that prevent pushdown
-- Wrong:
SELECT NOW() + INTERVAL '1 day' FROM distributed_readings;

-- Correct: filter before query
SELECT * FROM distributed_readings
WHERE time > NOW() - INTERVAL '1 day';

-- Use immutable functions for pushdown
SELECT * FROM distributed_readings
WHERE time > '2024-01-01'::TIMESTAMPTZ;
```

### 2. Increase Query Timeout

```sql
-- Increase statement timeout for distributed queries
SET statement_timeout = '300s';

-- Increase data node connection timeout
ALTER SERVER dn1 OPTIONS (SET timeout '60');

-- Query again
SELECT * FROM distributed_readings
WHERE time > NOW() - INTERVAL '7 days';
```

### 3. Optimize Distributed Query Plans

```sql
-- Use EXPLAIN to check pushdown
EXPLAIN
SELECT * FROM distributed_readings
WHERE device_id = 1 AND time > NOW() - INTERVAL '1 day';

-- Force a specific join method
SELECT /*+ HashJoin(a b) */ a.*, b.*
FROM distributed_readings a
JOIN device_info b ON a.device_id = b.id;
```

### 4. Fix Foreign Server Configuration

```sql
-- Check server options
SELECT srvoptions FROM pg_foreign_server
WHERE srvname = 'dn1';

-- Update options
ALTER SERVER dn1 OPTIONS (
  SET timeout '60',
  SET fetch_size '10000'
);
```

## Common Scenarios

- **Query returns wrong results**: Check for pushdown issues with EXPLAIN.
- **Distributed query is slow**: Reduce the amount of data returned from data nodes with better filters.
- **Query times out**: Increase statement_timeout and check data node network latency.

## Prevent It

- Use EXPLAIN to verify query pushdown before deploying
- Filter data at the data node level to reduce network transfer
- Monitor distributed query performance in the TimescaleDB dashboard

## Related Pages

- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
- [TimescaleDB Distributed Error](/tools/timescaledb/timescale-distributed-error)
- [TimescaleDB Data Node Error](/tools/timescaledb/timescale-data-node-error)
