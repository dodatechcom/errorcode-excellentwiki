---
title: "[Solution] MySQL Access Denied for User Error — How to Fix"
description: "Fix MySQL access denied errors by verifying credentials, resetting passwords, fixing host permissions, and resolving authentication plugin mismatches"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 10
comments: true
---

# MySQL Access Denied for User Error

This error means MySQL rejected your connection attempt because the username, password, or connecting host does not match a valid user account. MySQL requires all three components — user, host, and password — to match exactly.

## Why It Happens

- Incorrect username or password supplied
- The user account does not exist in `mysql.user`
- Connecting from a host not listed in the user's `Host` column
- Authentication plugin mismatch between client and server
- The account is locked (`account_locked = 'Y'`)
- Password has expired
- SSL is required but the client does not provide a certificate
- `FLUSH PRIVILEGES` was not run after direct table edits

## Common Error Messages

```
ERROR 1045 (28000): Access denied for user 'myuser'@'localhost' (using password: YES)
```

```
ERROR 1045 (28000): Access denied for user 'myuser'@'%' (using password: NO)
```

```
ERROR 1045 (28000): Access denied for user 'root'@'192.168.1.50' (using password: YES)
```

## How to Fix It

### 1. Verify the User Exists and Check Permissions

```sql
SELECT user, host, plugin, account_locked, password_expired
FROM mysql.user
WHERE user = 'myuser';
```

### 2. Reset the Password

```sql
-- MySQL 8.0+
ALTER USER 'myuser'@'localhost' IDENTIFIED BY 'new_secure_password';

-- MySQL 5.7
SET PASSWORD FOR 'myuser'@'localhost' = PASSWORD('new_secure_password');

FLUSH PRIVILEGES;
```

### 3. Fix Host Restrictions

```sql
-- Grant access from a specific IP
GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'192.168.1.%';

-- Or allow connections from any host
GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'%';

FLUSH PRIVILEGES;
```

### 4. Fix Authentication Plugin

```sql
-- Check the current plugin
SELECT user, plugin FROM mysql.user WHERE user = 'myuser';

-- Switch to native password for compatibility
ALTER USER 'myuser'@'localhost'
    IDENTIFIED WITH mysql_native_password BY 'password';

-- Or use caching_sha2_password for MySQL 8.0+
ALTER USER 'myuser'@'localhost'
    IDENTIFIED WITH caching_sha2_password BY 'password';

FLUSH PRIVILEGES;
```

### 5. Recover Root Access

```bash
# Stop MySQL
sudo systemctl stop mysql

# Start in safe mode with skip-grant-tables
sudo mysqld_safe --skip-grant-tables &

# Connect without password
mysql -u root

# Reset root password
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_root_password';
FLUSH PRIVILEGES;

# Restart MySQL normally
sudo systemctl restart mysql
```

## Common Scenarios

- **Application credentials outdated**: The DBA rotated the password but the application config was not updated. Use environment variables or a secrets manager.
- **Connecting from a new server**: Your app moved to a new IP address but the MySQL user only allows the old IP. Update the host grant or use `%`.
- **Plugin mismatch after upgrade**: MySQL 8.0 defaults to `caching_sha2_password` but older clients only support `mysql_native_password`. Switch the user's plugin.

## Prevent It

- Store database credentials in environment variables or a secrets manager rather than hardcoding them
- Grant access with specific IP ranges rather than `%` whenever possible
- Test credential changes in a staging environment before applying to production

## Related Pages

- [MySQL Connection Refused](/tools/mysql/mysql-connection-refused)
- [MySQL Too Many Connections](/tools/mysql/mysql-too-many-connections)
- [PostgreSQL Role Does Not Exist](/tools/postgresql/pg-role-does-not-exist)
