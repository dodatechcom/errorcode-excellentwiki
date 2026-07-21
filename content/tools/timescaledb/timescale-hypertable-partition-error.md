---
title: "[Solution] TimescaleDB Hypertable Partition Error"
description: "How to fix TimescaleDB hypertable partitioning errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Partition interval too small
- Time column not indexed
- Partition pruning not working

## How to Fix

```sql
SELECT create_hypertable('conditions', 'time', chunk_time_interval => INTERVAL '1 day');
```

## Examples

```sql
EXPLAIN SELECT * FROM conditions WHERE time > now() - INTERVAL '1 day';
```
