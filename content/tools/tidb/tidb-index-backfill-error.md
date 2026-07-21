---
title: "[Solution] TiDB Index Backfill Error"
description: "How to fix TiDB index backfill errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Backfill taking too long
- Backfill conflicting with DML
- Backfill memory limit exceeded

## How to Fix

```sql
SHOW DDL JOB WHERE table_name = 'mytable';
```

## Examples

```sql
ADMIN SHOW DDL JOBS;
```
