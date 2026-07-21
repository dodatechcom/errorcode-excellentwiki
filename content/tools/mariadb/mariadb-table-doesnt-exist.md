---
title: "[Solution] MariaDB Table Does Not Exist Error"
description: "Fix MariaDB table does not exist error. Resolve missing table issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Table Does Not Exist Error

The specified table does not exist in the database. The table was never created or was dropped.

## Common Causes

- Table was never created
- Table was dropped
- Table name is misspelled or wrong database

## How to Fix

### Solution 1

```bash
mysql -e "SHOW TABLES FROM mydb;"
```

### Solution 2

```bash
mysql -e "DESCRIBE mydb.mytable;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
