---
title: "[Solution] TimescaleDB Continuous Aggregate Drop Error — How to Fix"
description: "Fix TimescaleDB continuous aggregate drop errors by resolving dependency conflicts, fixing materialized view cleanup, and handling policy removal"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Continuous Aggregate Drop Error

TimescaleDB continuous aggregate drop errors occur when attempting to drop a continuous aggregate that has active refresh policies, dependencies, or dependent objects.

## Why It Happens

- Continuous aggregate has an active refresh policy
- Another view or function depends on the continuous aggregate
- Insufficient privileges to drop the materialized view
- Continuous aggregate is referenced in a GRANT statement
- Background worker is currently refreshing the aggregate
- The drop is attempted inside an explicit transaction

## Common Error Messages

```
ERROR: cannot drop continuous aggregate with active policy
```

```
ERROR: cannot drop because other objects depend on it
```

```
ERROR: permission denied for continuous aggregate
```

```
ERROR: continuous aggregate is being refreshed
```

## How to Fix It

### 1. Remove Policies Before Dropping

```sql
-- List policies on the continuous aggregate
SELECT * FROM timescaledb_information.jobs
WHERE hypertable_name = 'avg_hourly';

-- Remove refresh policy
SELECT remove_continuous_aggregate_policy('avg_hourly');

-- Now drop the continuous aggregate
DROP MATERIALIZED VIEW avg_hourly;
```

### 2. Drop Dependencies First

```sql
-- Check what depends on the continuous aggregate
SELECT dependent_ns.nspname || '.' || dependent_view.relname AS dependent_view
FROM pg_depend
JOIN pg_rewrite ON pg_rewrite.evclass = pg_depend.objid
JOIN pg_class dependent_view ON pg_rewrite.ev_class = dependent_view.oid
JOIN pg_namespace dependent_ns ON dependent_view.relnamespace = dependent_ns.oid
JOIN pg_class source_table ON pg_depend.refobjid = source_table.oid
WHERE source_table.relname = 'avg_hourly';

-- Drop dependent views first
DROP VIEW IF EXISTS v_user_stats;
DROP MATERIALIZED VIEW avg_hourly;
```

### 3. Force Drop

```sql
-- Drop everything in one command
DROP MATERIALIZED VIEW avg_hourly CASCADE;

-- This also drops policies and dependent objects
-- WARNING: may affect other objects
```

### 4. Handle Concurrent Refresh Conflict

```sql
-- Wait for background refresh to complete
SELECT * FROM timescaledb_information.jobs
WHERE proc_name = 'continuous_agg_refresh'
  AND hypertable_name = 'avg_hourly';

-- Stop the background worker if needed
SELECT _timescaledb_internal.stop_background_workers();

-- Then drop
DROP MATERIALIZED VIEW avg_hourly;

-- Restart workers
SELECT _timescaledb_internal.start_background_workers();
```

## Common Scenarios

- **Drop fails with active policy**: Remove the policy first with remove_continuous_aggregate_policy.
- **Other views depend on it**: Drop them first or use CASCADE.
- **Permission denied**: Connect as the owner or a superuser.

## Prevent It

- Always remove policies before dropping continuous aggregates
- Use CASCADE only when you understand all dependent objects
- Check dependencies with pg_depend before dropping

## Related Pages

- [TimescaleDB Continuous Aggregate Error](/tools/timescaledb/timescale-continuous-aggregate-error)
- [TimescaleDB Continuous Aggregate Policies](/tools/timescaledb/timescaledb-continuous-aggregate-policies)
- [TimescaleDB Policy Error](/tools/timescaledb/timescale-policy-error)
