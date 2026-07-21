---
title: "[Solution] TimescaleDB Job Config Error"
description: "How to fix TimescaleDB job configuration errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Job config wrong
- Job interval too short
- Job function not found

## How to Fix

```sql
SELECT alter_job(JOB_ID, config => '{"key": "value"}');
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs;
```
