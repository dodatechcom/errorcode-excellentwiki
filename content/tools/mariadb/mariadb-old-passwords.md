---
title: "[Solution] MariaDB Old Passwords Error"
description: "Fix MariaDB old passwords error. Resolve deprecated password hashing issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Old Passwords Error

The old password hashing format is used. This is insecure and deprecated.

## Common Causes

- old_passwords is set to 1 or 2
- User was created with old hash
- Client does not support new auth

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'old_passwords';"
```

### Solution 2

```bash
mysql -u root -e "ALTER USER 'myuser'@'%' IDENTIFIED VIA mysql_native_password USING PASSWORD('new_password');"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
