---
title: "[Solution] MariaDB Plugin Not Loaded Error"
description: "Fix MariaDB plugin not loaded error. Resolve plugin loading issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Plugin Not Loaded Error

A MariaDB plugin fails to load. The plugin library is missing or incompatible.

## Common Causes

- Plugin .so file is missing
- Plugin version is incompatible
- Plugin has dependency issues

## How to Fix

### Solution 1

```bash
mysql -e "SHOW PLUGINS;"
```

### Solution 2

```bash
ls /usr/lib/mysql/plugin/
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
