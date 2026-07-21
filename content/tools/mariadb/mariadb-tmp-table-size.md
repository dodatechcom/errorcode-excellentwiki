---
title: "[Solution] MariaDB tmp_table_size Error"
description: "Fix MariaDB tmp_table_size error. Resolve internal temporary table limit issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB tmp_table_size Error

The internal temporary table exceeds tmp_table_size. MariaDB converts to disk table.

## Common Causes

- tmp_table_size is too low
- Query generates large temporary result
- GROUP BY or DISTINCT on many rows

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'tmp_table_size';"
```

### Solution 2

```bash
mysql -e "SHOW GLOBAL STATUS LIKE 'Created_tmp_disk_tables';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
