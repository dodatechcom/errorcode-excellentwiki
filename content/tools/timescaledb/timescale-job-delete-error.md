---
title: "[Solution] TimescaleDB Job Delete Error"
description: "How to fix TimescaleDB job delete errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Job not found
- Job cannot be deleted
- Job still running

## How to Fix

```sql
SELECT delete_job(JOB_ID);
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs;
```
