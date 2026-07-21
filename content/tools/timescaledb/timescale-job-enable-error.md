---
title: "[Solution] TimescaleDB Job Enable Error"
description: "How to fix TimescaleDB job enable errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Job not found
- Job already enabled
- Job cannot be enabled

## How to Fix

```sql
SELECT alter_job(JOB_ID, scheduled => true);
```

## Examples

```sql
SELECT * FROM timescaledb_information.jobs;
```
