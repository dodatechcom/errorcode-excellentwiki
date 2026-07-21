---
title: "[Solution] Vitess Tablet SQL Mode Error"
description: "Fix Vitess SQL mode conflicts between vtgate session and backend MySQL settings"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet SQL Mode Error

SQL mode errors occur when vtgate sets a SQL mode that conflicts with the backend MySQL configuration or query requirements.

## Common Causes

- STRICT_TRANS_TABLES causing silent data truncation failures
- ONLY_FULL_GROUP_BY rejecting valid aggregation queries
- NO_ZERO_DATE rejecting default date values
- sql_mode mismatch between vtgate and tablet

## How to Fix

Check current SQL mode:

```sql
SELECT @@sql_mode;
```

Set compatible SQL mode:

```sql
SET SESSION sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
```

Configure vtgate SQL mode:

```bash
vtgate -mysql_server_mode=STRICT_TRANS_TABLES
```

## Examples

```sql
SHOW VARIABLES LIKE 'sql_mode';
```
