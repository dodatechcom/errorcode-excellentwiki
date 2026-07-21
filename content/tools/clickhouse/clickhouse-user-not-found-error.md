---
title: "[Solution] ClickHouse User Not Found Error"
description: "Fix ClickHouse user not found errors when authentication targets non-existent user"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse User Not Found Error

User not found errors occur when ClickHouse cannot find the specified user account.

## Common Causes

- User was dropped
- Typo in username
- User created on different cluster node
- Config file changed without reload

## How to Fix

List all users:

```sql
SELECT name, auth_type FROM system.users;
```

Create user:

```sql
CREATE USER myuser IDENTIFIED WITH sha256_password BY 'password';
```

Check user in config:

```bash
cat /etc/clickhouse-server/users.d/*.xml | grep -A5 '<myuser>'
```

## Examples

```sql
SELECT name, default_database, auth_type FROM system.users WHERE name = 'myuser';
```
