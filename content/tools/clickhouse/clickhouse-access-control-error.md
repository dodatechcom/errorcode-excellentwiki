---
title: "[Solution] ClickHouse Access Control Error"
description: "How to fix ClickHouse role-based access control errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- User does not have required role
- Role not granted
- Row-level security blocking access
- Column-level permissions missing

## How to Fix

Create and assign role:

```sql
CREATE ROLE analyst;
GRANT SELECT ON analytics.* TO analyst;
GRANT analyst TO my_user;
```

## Examples

```sql
SELECT * FROM system.roles;
SHOW GRANTS FOR my_user;
```
