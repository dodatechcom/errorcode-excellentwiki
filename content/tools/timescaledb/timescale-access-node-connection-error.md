---
title: "[Solution] TimescaleDB Access Node Connection Error"
description: "How to fix TimescaleDB access node connection errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Data node connection refused
- Network latency too high
- Connection pool exhausted

## How to Fix

```sql
SELECT * FROM timescaledb_information.data_nodes;
```

## Examples

```sql
SELECT * FROM pg_stat_activity WHERE backend_type = 'timescaledb';
```
