---
title: "[Solution] SQL Access Denied Fix"
description: "Fix 'Access denied for user X' when a database user lacks required permissions."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when a database user does not have the required privileges to perform the requested operation. The message reads: `Access denied for user 'X'@'host'`.

## What This Error Means

The database server rejected the operation because the authenticated user does not have sufficient privileges. This can happen for connection failures, query execution, or administrative operations.

## Common Causes

- User does not have SELECT, INSERT, UPDATE, or DELETE privileges
- Password is incorrect or has been changed
- User is connecting from a host not in the user's host list
- Account is locked or expired
- Missing GRANT OPTION for granting privileges to others

## How to Fix

### Fix 1: Grant required privileges

```sql
-- Grant all privileges on a database
GRANT ALL PRIVILEGES ON my_database.* TO 'app_user'@'localhost';

-- Grant specific privileges
GRANT SELECT, INSERT, UPDATE ON my_database.users TO 'app_user'@'%';

FLUSH PRIVILEGES;
```

### Fix 2: Check user privileges

```sql
SHOW GRANTS FOR 'app_user'@'localhost';
```

### Fix 3: Create a new user with correct permissions

```sql
CREATE USER 'app_user'@'%' IDENTIFIED BY 'secure_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON my_database.* TO 'app_user'@'%';
FLUSH PRIVILEGES;
```

## Examples

```sql
DELETE FROM users WHERE id = 1;
-- ERROR 1142: DELETE command denied to user 'reader'@'localhost' for table 'users'
```

## Related Errors

- [No Database Selected](sql-no-database.md) — missing database context
- [Connection Refused](sql-connection-refused.md) — cannot reach the server
