---
title: "[Solution] ClickHouse Readonly User Error"
description: "How to fix ClickHouse readonly user permission errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- User has SELECT-only grants
- Trying to INSERT with readonly user
- Default readonly profile applied

## How to Fix

Grant write permissions:

```sql
GRANT INSERT, UPDATE, DELETE ON my_database.* TO my_user;
```

Check grants:

```sql
SHOW GRANTS FOR my_user;
```

## Examples

```sql
SHOW GRANTS FOR my_user;
GRANT ALL ON my_database.* TO my_user;
```
