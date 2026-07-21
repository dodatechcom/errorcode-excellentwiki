---
title: "[Solution] MariaDB Unix Socket Auth Error"
description: "Fix MariaDB unix socket auth error. Resolve unix socket authentication issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Unix Socket Auth Error

Unix socket authentication fails. The client user does not match the MariaDB user.

## Common Causes

- System user does not match MariaDB user
- Socket file path is wrong
- Socket permissions are restricted

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'socket';"
```

### Solution 2

```bash
mysql -e "SELECT user, plugin FROM mysql.user WHERE user = CURRENT_USER();"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
