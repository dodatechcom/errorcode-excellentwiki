---
title: "[Solution] MariaDB XtraDB Corruption Error"
description: "Fix MariaDB XtraDB corruption error. Resolve InnoDB/XtraDB data corruption issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB XtraDB Corruption Error

XtraDB (InnoDB) data is corrupted. Tables or tablespaces are unreadable.

## Common Causes

- Disk failure corrupted data files
- Crash during write operation
- Bug in XtraDB version

## How to Fix

### Solution 1

```bash
mysql -e "CHECK TABLE mydb.mytable;"
```

### Solution 2

```bash
mysql -e "SHOW ENGINE INNODB STATUS;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
