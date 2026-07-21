---
title: "[Solution] TiDB DDL Resume Error"
description: "How to fix TiDB DDL resume errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- DDL job not paused
- DDL job cannot be resumed
- DDL job ID not found

## How to Fix

```sql
ADMIN RESUME DDL JOBS 1;
```

## Examples

```sql
SHOW DDL JOBS;
```
