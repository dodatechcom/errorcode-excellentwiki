---
title: "[Solution] MariaDB Slow Query Log Error"
description: "Fix MariaDB slow query log error. Resolve slow query logging issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Slow Query Log Error

The slow query log is not being written. Logging configuration is wrong.

## Common Causes

- Slow query log is not enabled
- Log file is not writable
- log_output is set to NONE

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'slow_query_log%';"
```

### Solution 2

```bash
mysql -e "SET GLOBAL slow_query_log = ON;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
