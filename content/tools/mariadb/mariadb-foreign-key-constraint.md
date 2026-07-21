---
title: "[Solution] MariaDB Cannot Add Foreign Key Constraint Error"
description: "Fix MariaDB cannot add foreign key constraint error. Resolve foreign key issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Cannot Add Foreign Key Constraint Error

The foreign key constraint cannot be added. The referenced table, column, or index is missing.

## Common Causes

- Referenced table does not exist
- Referenced column is not indexed
- Data type mismatch between columns

## How to Fix

### Solution 1

```bash
mysql -e "SHOW CREATE TABLE mydb.child_table;"
```

### Solution 2

```bash
mysql -e "SHOW CREATE TABLE mydb.parent_table;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
