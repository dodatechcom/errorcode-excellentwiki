---
title: "[Solution] MariaDB mysql_native_password Error"
description: "Fix MariaDB mysql_native_password error. Resolve native password authentication issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB mysql_native_password Error

The mysql_native_password authentication fails. The password hash is wrong or the plugin is disabled.

## Common Causes

- Password hash is corrupted
- Plugin is not loaded
- Client does not support the plugin

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'default_authentication_plugin';"
```

### Solution 2

```bash
mysql -u root -e "ALTER USER 'myuser'@'%' IDENTIFIED BY 'password';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
