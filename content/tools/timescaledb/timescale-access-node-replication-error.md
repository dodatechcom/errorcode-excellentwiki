---
title: "[Solution] TimescaleDB Access Node Replication Error"
description: "How to fix TimescaleDB access node replication errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Replication lag between access and data nodes
- Replication not working
- Replication slot not created

## How to Fix

```sql
SELECT * FROM pg_stat_replication;
```

## Examples

```sql
SELECT * FROM pg_replication_slots;
```
