---
title: "[Solution] TimescaleDB Join Error — How to Fix"
description: "Fix TimescaleDB join errors on hypertables by resolving cross-chunk join failures, fixing partition-wise join issues, and handling distributed joins"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Join Error

TimescaleDB join errors occur when joining hypertables or joining a hypertable with a regular table fails due to chunk pruning, partition alignment, or distributed query issues.

## Why It Happens

- JOIN does not include the time column for chunk pruning
- Partition-wise join is enabled but tables are not co-partitioned
- Cross-node join fails on distributed hypertables
- Hash join runs out of memory for large unpruned joins
- JOIN condition references columns that are not indexed
- LATERAL JOIN with hypertable produces incorrect results

## Common Error Messages

```
ERROR: could not find chunk for join
```

```
ERROR: join between hypertables requires time conditions
```

```
ERROR: distributed join failed
```

```
ERROR: out of memory in hash join
```

## How to Fix It

### 1. Add Time Conditions to JOIN

```sql
-- Incorrect: no time pruning
SELECT a.*, b.*
FROM sensor_data a
JOIN device_info b ON a.device_id = b.id;

-- Correct: add time condition
SELECT a.*, b.*
FROM sensor_data a
JOIN device_info b ON a.device_id = b.id
WHERE a.time > NOW() - INTERVAL '1 day';
```

### 2. Use Time-Based JOIN

```sql
-- Join two hypertables with aligned time
SELECT a.*, b.*
FROM readings a
JOIN temperatures b
  ON a.device_id = b.device_id
  AND a.time = b.time
WHERE a.time > NOW() - INTERVAL '1 hour';

-- Use time_bucket for aligned aggregation
SELECT
  time_bucket('1 hour', r.time) AS bucket,
  AVG(r.reading) AS avg_reading,
  AVG(t.temperature) AS avg_temp
FROM readings r
JOIN temperatures t
  ON r.device_id = t.device_id
  AND time_bucket('1 hour', r.time) = time_bucket('1 hour', t.time)
WHERE r.time > NOW() - INTERVAL '1 day'
GROUP BY bucket;
```

### 3. Fix Distributed JOIN Issues

```sql
-- Ensure JOIN is on the distribution column
-- For distributed hypertables
SELECT a.*, b.*
FROM distributed_readings a
JOIN distributed_temperatures b
  ON a.device_id = b.device_id
WHERE a.time > NOW() - INTERVAL '1 day';
```

### 4. Optimize JOIN Memory

```sql
-- Increase work memory for hash joins
SET work_mem = '256MB';

-- Use merge join hint
SELECT /*+ MergeJoin(a b) */ a.*, b.*
FROM sensor_data a
JOIN device_info b ON a.device_id = b.id
WHERE a.time > NOW() - INTERVAL '1 day';
```

## Common Scenarios

- **JOIN is slow without time condition**: Always include a time filter to enable chunk pruning.
- **Distributed JOIN fails**: Ensure the JOIN condition includes the distribution column.
- **Hash join OOM**: Increase work_mem or add filters to reduce the result set.

## Prevent It

- Always include time conditions when joining hypertables
- Align chunk intervals between co-joined hypertables
- Use distribution columns in JOIN conditions for distributed hypertables

## Related Pages

- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
- [TimescaleDB Distributed Error](/tools/timescaledb/timescale-distributed-error)
- [TimescaleDB Hypertable Error](/tools/timescaledb/timescale-hypertable-error)
