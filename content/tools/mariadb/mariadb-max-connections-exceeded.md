---
title: "[Solution] MariaDB Max Connections Exceeded Error"
description: "Fix MariaDB max connections exceeded error. Resolve connection limit issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Max Connections Exceeded Error

MariaDB has reached the max_connections limit. New connections are refused.

## Common Causes

- Applications are not closing connections
- Connection pool is too small
- max_connections needs to be increased

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'max_connections';"
```

### Solution 2

```bash
mysql -e "SHOW GLOBAL STATUS LIKE 'Max_used_connections';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
