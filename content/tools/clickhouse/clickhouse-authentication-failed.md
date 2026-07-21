---
title: "[Solution] ClickHouse Authentication Failed Error"
description: "How to fix ClickHouse authentication failures"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Wrong username or password
- User does not exist
- User locked or disabled
- Default user has no password set

## How to Fix

Check users:

```sql
SELECT name, auth_type FROM system.users;
```

Create user:

```sql
CREATE USER my_user IDENTIFIED BY 'password';
GRANT SELECT ON my_database.* TO my_user;
```

## Examples

```sql
SELECT * FROM system.users;
SELECT * FROM system.grants WHERE user_name = 'my_user';
```
