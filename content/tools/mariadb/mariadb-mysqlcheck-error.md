---
title: "[Solution] MariaDB mysqlcheck Error"
description: "Fix MariaDB mysqlcheck error. Resolve table check and repair issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB mysqlcheck Error

The mysqlcheck tool fails. The table is locked or the check encounters errors.

## Common Causes

- Table is locked by another process
- Check encounters corruption
- mysqlcheck cannot access table

## How to Fix

### Solution 1

```bash
mysqlcheck --all-databases
```

### Solution 2

```bash
mysqlcheck --all-databases --check-upgrade
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
