---
title: "[Solution] MariaDB Out of Memory Error"
description: "Fix MariaDB out of memory error. Resolve memory exhaustion issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Out of Memory Error

MariaDB runs out of memory. A query or operation requires more memory than available.

## Common Causes

- Query requires too much memory
- max_heap_table_size is too low
- Too many concurrent connections

## How to Fix

### Solution 1

```bash
mysql -e "SHOW GLOBAL STATUS LIKE 'Threads_connected';"
```

### Solution 2

```bash
mysql -e "SHOW VARIABLES LIKE 'max_heap_table_size';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
