---
title: "[Solution] TimescaleDB Job Run Error"
description: "How to fix TimescaleDB job run errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Job not scheduled
- Job failing
- Job timeout

## How to Fix

```sql
SELECT run_job(JOB_ID);
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs;
```
