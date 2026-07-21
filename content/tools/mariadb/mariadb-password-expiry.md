---
title: "[Solution] MariaDB Password Expiry Error"
description: "Fix MariaDB password expiry error. Resolve password expiration issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Password Expiry Error

The user password has expired. The user must change the password before logging in.

## Common Causes

- Password has expired per policy
- password_lifetime has been exceeded
- Password was never changed

## How to Fix

### Solution 1

```bash
mysql -u root -e "ALTER USER 'myuser'@'%' PASSWORD EXPIRE NEVER;"
```

### Solution 2

```bash
mysql -u root -e "ALTER USER 'myuser'@'%' IDENTIFIED BY 'new_password';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
