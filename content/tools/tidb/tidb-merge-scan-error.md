---
title: "[Solution] TiDB Merge Scan Error — How to Fix"
description: "Fix TiDB merge scan errors by resolving coprocessor merge failures, fixing table scan operator errors, and correcting distributed execution plans"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Merge Scan Error

TiDB merge scan errors occur when the coprocessor cannot merge results from multiple regions or when the distributed table scan operator encounters inconsistent data during parallel execution.

## Why It Happens

- Region merge operation overlaps with ongoing scans
- Coprocessor request exceeds region boundary during merge
- Table statistics are stale causing incorrect scan distribution
- Parallel scan goroutines encounter lock conflicts
- Region leader changes during the scan operation
- Coprocessor cache becomes invalid mid-scan

## Common Error Messages

```
ERROR: coprocessor request failed
```

```
ERROR: region is not available
```

```
ERROR: merge scan task cancelled
```

```
ERROR: stale region epoch
```

## How to Fix It

### 1. Check Region Health

```bash
# Check region status via pd-ctl
pd-ctl region <region_id>

# Check for unhealthy regions
pd-ctl operator scan | grep error

# List all regions for a table
pd-ctl operator add scatter-region <region_id>
```

### 2. Fix Table Statistics

```sql
-- Update table statistics
ANALYZE TABLE my_table;

-- Check last analyze time
SHOW STATS_META WHERE table_name = 'my_table';

-- Analyze with specific columns
ANALYZE TABLE my_table COLUMNS id, name, created_at;
```

### 3. Retry with Hint

```sql
-- Force index to avoid merge scan
SELECT /*+ USE_INDEX(my_table, idx_primary) */ * FROM my_table
WHERE id BETWEEN 1 AND 10000;

-- Use NO_MERGE_JOIN hint
SELECT /*+ NO_MERGE_JOIN(t1, t2) */ *
FROM table1 t1 JOIN table2 t2 ON t1.id = t2.id;

-- Increase coprocessor timeout
SET tidb_gc_life_time = '10m';
```

### 4. Resolve Stale Epoch

```bash
# Check if regions have stale epochs
pd-ctl region check stale

# Manually split a large region if needed
pd-ctl operator add split-region <region_id>

# Check for region leader
pd-ctl region leader <region_id>
```

## Common Scenarios

- **Scan fails after region split**: Wait for region heartbeat or restart the query.
- **Merge scan timeout on large table**: Increase `tidb_gc_life_time` and update statistics.
- **Coprocessor request cancelled**: Check for region leader changes in PD logs.

## Prevent It

- Keep table statistics up to date with regular ANALYZE
- Monitor region health in the PD dashboard
- Avoid very large scan operations without proper indexes

## Related Pages

- [TiDB Coprocessor Error](/tools/tidb/tidb-coprocessor-error)
- [TiDB Region Error](/tools/tidb/tidb-region-error)
- [TiDB Statistics Error](/tools/tidb/tidb-statistics-error)
