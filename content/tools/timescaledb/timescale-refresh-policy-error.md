---
title: "[Solution] TimescaleDB Refresh Policy Error"
description: "How to fix TimescaleDB refresh policy errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Refresh policy not set
- Refresh interval wrong
- Policy not enabled

## How to Fix

```sql
SELECT add_continuous_aggregate_policy('my_cagg', start_offset => INTERVAL '1 hour', end_offset => INTERVAL '0', schedule_interval => INTERVAL '1 hour');
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs WHERE proc_name = 'policy_refresh';
```
