---
title: "[Solution] MariaDB IO Thread Error"
description: "Fix MariaDB IO thread error. Resolve slave IO thread issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB IO Thread Error

The slave IO thread encounters an error. The slave cannot fetch binary logs from master.

## Common Causes

- Cannot connect to master
- Master binary logs are purged
- Network connectivity issue

## How to Fix

### Solution 1

```bash
mysql -e "SHOW SLAVE STATUS\G"
```

### Solution 2

```bash
mysql -e "SHOW MASTER STATUS;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
