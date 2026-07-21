---
title: "[Solution] MariaDB General Log Error"
description: "Fix MariaDB general log error. Resolve general query logging issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB General Log Error

The general query log is not being written or is causing performance issues.

## Common Causes

- General log is not enabled
- Log file is too large
- General log impacts performance

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'general_log%';"
```

### Solution 2

```bash
mysql -e "SET GLOBAL general_log = ON;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
