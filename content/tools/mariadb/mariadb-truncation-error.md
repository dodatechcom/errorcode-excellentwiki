---
title: "[Solution] MariaDB Truncation Error"
description: "Fix MariaDB truncation error. Resolve data truncation during insert or update."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Truncation Error

Data is truncated during the insert or update operation. The value does not fit the column.

## Common Causes

- Value is too long for column
- Numeric value is too large
- Date value is out of range

## How to Fix

### Solution 1

```bash
mysql -e "DESCRIBE mydb.mytable;"
```

### Solution 2

```bash
SET sql_mode = '';
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
