---
title: "[Solution] MariaDB Deadlock Found Error"
description: "Fix MariaDB deadlock found error. Resolve transaction deadlock issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Deadlock Found Error

A deadlock is detected. Two or more transactions are waiting for each other to release locks.

## Common Causes

- Transactions lock resources in different order
- Long-running queries hold locks
- InnoDB detects cycle

## How to Fix

### Solution 1

```bash
mysql -e "SHOW ENGINE INNODB STATUS;"
```

### Solution 2

```bash
mysql -e "SHOW PROCESSLIST;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
