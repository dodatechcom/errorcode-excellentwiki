---
title: "[Solution] MariaDB Unknown Database Error"
description: "Fix MariaDB unknown database error. Resolve missing database issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Unknown Database Error

The specified database does not exist. The database was never created or was dropped.

## Common Causes

- Database was never created
- Database was dropped
- Database name is misspelled

## How to Fix

### Solution 1

```bash
mysql -e "SHOW DATABASES;"
```

### Solution 2

```bash
mysql -e "CREATE DATABASE mydb;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
