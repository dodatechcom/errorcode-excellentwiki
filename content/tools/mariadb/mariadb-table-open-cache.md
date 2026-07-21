---
title: "[Solution] MariaDB table_open_cache Error"
description: "Fix MariaDB table_open_cache error. Resolve table cache configuration issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB table_open_cache Error

The table_open_cache is too small. MariaDB has to close and reopen tables frequently.

## Common Causes

- table_open_cache is too low
- Too many tables are open concurrently
- Opened_tables counter is high

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'table_open_cache';"
```

### Solution 2

```bash
mysql -e "SHOW GLOBAL STATUS LIKE 'Opened_tables';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
