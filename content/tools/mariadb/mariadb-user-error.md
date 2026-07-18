---
title: "[Solution] MariaDB User Error — How to Fix"
description: "Fix MariaDB user errors including access denied, missing grants, account lockouts, and plugin authentication issues for database user accounts"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB User Error

User errors relate to account authentication, authorization, and management. They occur when a client cannot log in, the account is locked, or the authentication plugin does not match.

## Why It Happens

- The username or password is incorrect
- The user account is locked (`CREATE USER ... ACCOUNT LOCK`)
- The user can only connect from certain hosts (`'user'@'specific-host'`)
- Authentication plugin mismatch between client and server
- Required privileges were not granted
- `max_user_connections` has been reached

## Common Error Messages

```
ERROR 1045 (28000): Access denied for user 'myuser'@'localhost' (using password: YES)
```

```
ERROR 1820 (HY000): You must reset your password using ALTER USER statement
```

```
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
```

```
ERROR 1129 (HY000): Host '192.168.1.100' is blocked because of many connection errors
```

## How to Fix It

### 1. Reset Forgotten Root Password

```bash
sudo systemctl stop mariadb
sudo mysqld_safe --skip-grant-tables --skip-networking &
mysql -u root
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_strong_password';
sudo killall mysqld
sudo systemctl start mariadb
```

### 2. Fix Remote Access Denied

```sql
SELECT User, Host FROM mysql.user;
CREATE USER 'myuser'@'192.168.1.%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'192.168.1.%';
FLUSH PRIVILEGES;
```

### 3. Fix Authentication Plugin Issues

```sql
SELECT User, Host, plugin FROM mysql.user WHERE User = 'myuser';
ALTER USER 'myuser'@'%' IDENTIFIED VIA mysql_native_password USING PASSWORD('mypass');
```

### 4. Unlock a Locked Account

```sql
SELECT User, Host, account_locked FROM mysql.user WHERE User = 'myuser';
ALTER USER 'myuser'@'%' ACCOUNT UNLOCK;
UPDATE mysql.user SET failed_login_attempts = 0 WHERE User = 'myuser';
FLUSH PRIVILEGES;
```

### 5. Fix max_user_connections

```sql
SET GLOBAL max_user_connections = 100;
ALTER USER 'myuser'@'%' WITH MAX_USER_CONNECTIONS 50;
```

## Common Scenarios

- **New deployment fails with access denied**: Add the new server IP to user's host list.
- **Password policy rejects new password**: Use a stronger password or lower policy level.
- **Locked account after brute-force attempts**: Unlock with `ALTER USER ... ACCOUNT UNLOCK`.

## Prevent It

- Create accounts with specific host patterns instead of `%`
- Store passwords in a secrets manager
- Use connection pooling to surface password issues during deployment

## Related Pages

- [MariaDB Connection Error](/tools/mariadb/mariadb-connection-error)
- [MariaDB SSL Error](/tools/mariadb/mariadb-ssl-error)
- [MySQL Access Denied](/tools/mysql/mysql-access-denied)
