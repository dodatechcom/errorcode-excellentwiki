---
title: "[Solution] TimescaleDB Query OOM Error"
description: "How to fix TimescaleDB query out of memory errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query result set too large
- Continuous aggregate refresh too big
- Work memory too high

## How to Fix

```sql
SET work_mem = '32MB';
```

## Examples

```sql
SELECT * FROM timescaledb_information.hypertables;
```
