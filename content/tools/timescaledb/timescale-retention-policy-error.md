---
title: "[Solution] TimescaleDB Retention Policy Error — How to Fix"
description: "Fix TimescaleDB retention policy errors by resolving drop_chunks failures, fixing policy scheduling, and handling data retention configuration"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Retention Policy Error

TimescaleDB retention policy errors occur when automatic data retention policies fail to drop old chunks, schedule incorrectly, or conflict with other operations.

## Why It Happens

- Retention policy schedule is too aggressive
- Chunks are locked by active queries during drop
- Background worker is not running
- Retention interval is smaller than the chunk interval
- Cascading deletes fail due to foreign key constraints
- Disk space is not reclaimed after chunk drop

## Common Error Messages

```
ERROR: retention policy failed to drop chunk
```

```
ERROR: could not drop chunk due to lock
```

```
WARNING: retention policy job skipped
```

```
ERROR: retention interval too short
```

## How to Fix It

### 1. Check Retention Policy Status

```sql
-- View retention policies
SELECT * FROM timescaledb_information.jobs
WHERE proc_name = 'policy_retention';

-- Check dropped chunks
SELECT chunk_name, range_start, range_end
FROM timescaledb_information.chunks
WHERE hypertable_name = 'sensor_data'
ORDER BY range_start;
```

### 2. Configure Retention Policy Correctly

```sql
-- Add retention policy (drop data older than 90 days)
SELECT add_retention_policy('sensor_data', INTERVAL '90 days');

-- Remove existing policy
SELECT remove_retention_policy('sensor_data');

-- Re-add with corrected interval
SELECT add_retention_policy('sensor_data', INTERVAL '180 days');
```

### 3. Manually Drop Chunks

```sql
-- Drop chunks older than a specific time
SELECT drop_chunks('sensor_data', older_than => INTERVAL '90 days');

-- Drop chunks for a specific time range
SELECT drop_chunks('sensor_data',
  older_than => '2024-01-01'::TIMESTAMPTZ
);

-- Verify chunks are dropped
SELECT COUNT(*) AS remaining_chunks
FROM timescaledb_information.chunks
WHERE hypertable_name = 'sensor_data';
```

### 4. Fix Lock Conflicts

```sql
-- Check for active queries on old chunks
SELECT pid, query, state, query_start
FROM pg_stat_activity
WHERE query LIKE '%sensor_data%';

-- Cancel blocking queries
SELECT pg_cancel_backend(<pid>);

-- Then retry the retention policy
SELECT drop_chunks('sensor_data', older_than => INTERVAL '90 days');
```

## Common Scenarios

- **Retention policy not dropping data**: Check background worker status and job configuration.
- **Chunks locked during drop**: Wait for or cancel active queries.
- **Disk space not reclaimed**: VACUUM the hypertable after dropping chunks.

## Prevent It

- Set retention interval larger than chunk interval
- Monitor disk space and chunk counts regularly
- Run VACUUM after dropping large numbers of chunks

## Related Pages

- [TimescaleDB Drop Chunk Error](/tools/timescaledb/timescale-drop-chunk-error)
- [TimescaleDB Policy Error](/tools/timescaledb/timescale-policy-error)
- [TimescaleDB Space Error](/tools/timescaledb/timescale-space-error)
