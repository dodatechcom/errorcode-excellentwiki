---
title: "[Solution] TiDB Plan Replayer Error — How to Fix"
description: "Fix TiDB plan replayer errors by resolving plan capture failures, fixing EXPLAIN ANALYZE issues, and handling plan replay problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Plan Replayer Error

TiDB plan replayer errors occur when using the Plan Replayer feature to capture and replay query execution plans for performance debugging.

## Why It Happens

- Plan Replayer capture is not enabled
- Captured plan data is corrupted
- Plan replay fails due to schema changes
- Captured plan exceeds size limits
- Plan Replayer dump file is not accessible
- Statistics have changed since capture

## Common Error Messages

```
ERROR: plan replayer not enabled
```

```
ERROR: plan capture failed
```

```
ERROR: plan replay failed - schema changed
```

```
ERROR: plan replayer dump too large
```

## How to Fix It

### 1. Capture Query Plan

```sql
-- Capture plan for a query
PLAN REPLAYER DUMP EXPLAIN SELECT * FROM users WHERE name = 'Alice';

-- Save plan to file
PLAN REPLAYER DUMP EXPLAIN INTO '/tmp/plan.dump' SELECT * FROM users;
```

### 2. Replay Captured Plan

```sql
-- Replay a captured plan
PLAN REPLAYER LOAD '/tmp/plan.dump';

-- Check plan statistics
EXPLAIN ANALYZE SELECT * FROM users WHERE name = 'Alice';
```

### 3. Fix Plan Replayer Issues

```sql
-- Enable Plan Replayer
SET tidb_enable_plan_replayer = ON;

-- Check captured plans
SELECT * FROM mysql.plan_replayer_status;

-- Clean up old plans
DELETE FROM mysql.plan_replayer_status WHERE create_time < DATE_SUB(NOW(), INTERVAL 7 DAY);
```

### 4. Debug Query Plans

```sql
-- Get detailed query plan
EXPLAIN ANALYZE
SELECT * FROM users WHERE name = 'Alice';

-- Check plan warnings
EXPLAIN FORMAT='verbose' SELECT * FROM users WHERE name = 'Alice';
```

## Common Scenarios

- **Plan Replayer not capturing**: Enable the feature with tidb_enable_plan_replayer.
- **Plan replay fails**: Ensure schema hasn't changed since capture.
- **Plan file too large**: Capture only specific queries, not all.

## Prevent It

- Enable Plan Replayer for performance debugging
- Capture plans before schema changes
- Keep plan dumps organized for analysis

## Related Pages

- [TiDB Slow Query Error](/tools/tidb/tidb-slow-query-error)
- [TiDB Query Error](/tools/tidb/tidb-query-error)
- [TiDB Statistics Error](/tools/tidb/tidb-statistics-error)
