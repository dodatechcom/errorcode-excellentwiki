---
title: "[Solution] MariaDB Slave Not Running Error"
description: "Fix MariaDB slave not running error. Resolve replication thread issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Slave Not Running Error

The replication slave threads are not running. Replication is not active.

## Common Causes

- Slave SQL thread encountered an error
- Slave IO thread cannot connect to master
- Replication was manually stopped

## How to Fix

### Solution 1

```bash
mysql -e "SHOW SLAVE STATUS\G"
```

### Solution 2

```bash
mysql -e "START SLAVE;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
