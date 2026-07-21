---
title: "[Solution] TimescaleDB Access Node Stream Error"
description: "How to fix TimescaleDB access node streaming errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Streaming replication not working
- WAL sender failing
- Streaming lag too high

## How to Fix

```sql
SELECT * FROM pg_stat_replication;
```

## Examples

```sql
SELECT * FROM pg_stat_wal_receiver;
```
