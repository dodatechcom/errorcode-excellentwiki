---
title: "[Solution] TimescaleDB Distributed Reindex Error"
description: "How to fix TimescaleDB distributed reindex errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Reindex on distributed hypertable failing
- Index not found
- Data node unreachable

## How to Fix

```sql
REINDEX INDEX conditions_time_idx;
```

## Examples

```sql
SELECT * FROM pg_stat_user_indexes WHERE schemaname = 'public';
```
