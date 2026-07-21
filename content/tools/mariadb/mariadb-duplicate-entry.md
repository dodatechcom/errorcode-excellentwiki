---
title: "[Solution] MariaDB Duplicate Entry Error"
description: "Fix MariaDB duplicate entry error. Resolve UNIQUE or PRIMARY KEY constraint violations."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Duplicate Entry Error

A duplicate entry violates a UNIQUE or PRIMARY KEY constraint. The INSERT or UPDATE fails.

## Common Causes

- INSERT tries to add existing unique value
- UPDATE changes value to duplicate
- Multiple rows with same key

## How to Fix

### Solution 1

```bash
mysql -e "SHOW CREATE TABLE mydb.mytable;"
```

### Solution 2

```bash
mysql -e "SELECT * FROM mydb.mytable WHERE unique_col = 'value';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
