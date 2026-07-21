---
title: "[Solution] TimescaleDB Distributed Reorder Error"
description: "How to fix TimescaleDB distributed reorder errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Reorder on distributed hypertable failing
- Index not found
- Data node unreachable

## How to Fix

```sql
CLUSTER conditions USING conditions_time_idx;
```

## Examples

```sql
SELECT * FROM pg_stat_user_indexes WHERE schemaname = 'public';
```
