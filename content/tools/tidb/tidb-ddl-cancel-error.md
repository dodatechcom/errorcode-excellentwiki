---
title: "[Solution] TiDB DDL Cancel Error"
description: "How to fix TiDB DDL cancel errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- DDL job cannot be canceled
- DDL job already completed
- DDL job ID not found

## How to Fix

```sql
ADMIN CANCEL DDL JOBS 1;
```

## Examples

```sql
SHOW DDL JOBS;
```
