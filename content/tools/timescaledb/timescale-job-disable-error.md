---
title: "[Solution] TimescaleDB Job Disable Error"
description: "How to fix TimescaleDB job disable errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Job not found
- Job cannot be disabled
- Job already disabled

## How to Fix

```sql
SELECT alter_job(JOB_ID, scheduled => false);
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs;
```
