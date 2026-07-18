---
title: "[Solution] MySQL Access Denied for User - Fix Authentication Errors"
description: "Fix MySQL access denied errors by resetting passwords, granting privileges, fixing host restrictions, and verifying authentication plugins"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Access Denied for User

This error means MySQL rejected the connection because the username, password, or connecting host does not match any valid user account in the `mysql.user` table.

## What This Error Means

MySQL returns this error when authentication fails:

```
ERROR 1045 (28000): Access denied for user 'myuser'@'localhost' (using password: YES)
```

The `(using password: YES)` or `(using password: NO)` part tells you whether a password was provided. MySQL authentication depends on three factors: the username, the host from which the connection originates, and the password. All three must match a row in the `mysql.user` table.

## Why It Happens

- The username or password is incorrect
- The user account does not exist in `mysql.user`
- The user is connecting from a host not listed in the `Host` column
- The authentication plugin does not match (e.g., `mysql_native_password` vs `caching_sha2_password`)
- The user account is locked
- `FLUSH PRIVILEGES` was not run after modifying privileges
- The MySQL server was restored from a backup that did not include user accounts

## How to Fix It

### 1. Check If the User Exists

```sql
SELECT user, host, plugin, account_locked
FROM mysql.user
WHERE user = 'myuser';
```

### 2. Create the User If Missing

```sql
-- Create a user for any host
CREATE USER 'myuser'@'%' IDENTIFIED BY 'secure_password';

-- Create a user for localhost only
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'secure_password';
```

### 3. Reset the Password

```sql
-- For MySQL 5.7+
ALTER USER 'myuser'@'localhost' IDENTIFIED BY 'new_password';

-- For older versions
SET PASSWORD FOR 'myuser'@'localhost' = PASSWORD('new_password');

-- Apply changes
FLUSH PRIVILEGES;
```

### 4. Fix Host Restrictions

```sql
-- Check which hosts are allowed
SELECT user, host FROM mysql.user WHERE user = 'myuser';

-- Grant access from a new host
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'192.168.1.%' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

### 5. Fix Authentication Plugin

```sql
-- Check the current plugin
SELECT user, plugin FROM mysql.user WHERE user = 'myuser';

-- Switch to mysql_native_password for compatibility
ALTER USER 'myuser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
FLUSH PRIVILEGES;
```

## Common Mistakes

- Forgetting that MySQL usernames include the host -- `'myuser'@'localhost'` and `'myuser'@'%'` are different accounts
- Not running `FLUSH PRIVILEGES` after modifying `mysql.user` directly
- Using the wrong authentication plugin when connecting with older client libraries
- Assuming `GRANT` automatically creates the user -- in MySQL 5.7+ you must create the user first
- Not checking whether the account is locked (`account_locked = 'Y'`)

## Related Pages

- [MySQL Connection Refused](/tools/mysql/mysql-connection-refused)
- [MySQL User Limit](/tools/mysql/mysql-user-limit)
- [MySQL SSL Error](/tools/mysql/mysql-ssl-error)
- [PostgreSQL Role Does Not Exist](/tools/postgresql/pg-role-does-not-exist)
