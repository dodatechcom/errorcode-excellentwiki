---
title: "[Solution] MariaDB Lock Wait Timeout Error"
description: "Fix MariaDB lock wait timeout error. Resolve transaction lock timeout issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Lock Wait Timeout Error

A transaction waits too long for a lock. The lock wait timeout expires.

## Common Causes

- Long-running transaction holds locks
- Deadlock between concurrent transactions
- Lock wait timeout is too short

## How to Fix

### Solution 1

```bash
mysql -e "SHOW PROCESSLIST;"
```

### Solution 2

```bash
mysql -e "SHOW ENGINE INNODB STATUS;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
