---
title: "[Solution] ClickHouse User Not Found Error"
description: "How to fix ClickHouse user not found errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Username misspelled
- User created in different server
- User not created yet

## How to Fix

List users:

```sql
SHOW USERS;
SELECT name FROM system.users;
```

Create user:

```sql
CREATE USER my_user IDENTIFIED WITH plaintext_password BY 'secret';
```

## Examples

```sql
SHOW USERS;
SELECT name, auth_type FROM system.users;
```
