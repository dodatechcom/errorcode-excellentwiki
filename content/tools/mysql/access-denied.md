---
title: "ERROR 1045 (28000): Access denied for user"
description: "MySQL rejects authentication for the specified user"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
tags: ["authentication", "password", "user", "permissions"]
weight: 5
---

This error occurs when MySQL rejects a connection because the username or password is incorrect, or the user lacks permission to connect from the specified host.

## Common Causes

- Incorrect username or password
- User not granted CONNECT privilege
- User trying to connect from unauthorized host
- Authentication plugin mismatch

## How to Fix

1. Reset the user's password:

```sql
ALTER USER 'myuser'@'localhost' IDENTIFIED BY 'newpassword';
FLUSH PRIVILEGES;
```

2. Grant connection privileges:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

3. Check user host restrictions:

```sql
SELECT user, host FROM mysql.user WHERE user = 'myuser';
```

## Examples

```bash
# This will fail if credentials are wrong
mysql -u myuser -p mydb

# Error output:
# ERROR 1045 (28000): Access denied for user 'myuser'@'localhost' (using password: YES)
```

```sql
-- Connection attempt with wrong password
-- mysql -u admin -p
-- Enter password: wrongpassword
-- ERROR 1045 (28000): Access denied for user 'admin'@'localhost'
```

## Related Errors

- [Table Already Exists](/tools/mysql/table-exists)
- [Connection Refused](/tools/postgresql/connection-refused)
