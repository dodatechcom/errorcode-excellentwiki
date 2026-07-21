---
title: "[Solution] TiDB DDL Pause Error"
description: "How to fix TiDB DDL pause errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- DDL job cannot be paused
- DDL job already paused
- DDL job ID not found

## How to Fix

```sql
ADMIN PAUSE DDL JOBS 1;
```

## Examples

```sql
SHOW DDL JOBS;
```
