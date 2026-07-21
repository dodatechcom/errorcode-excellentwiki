---
title: "[Solution] MariaDB MyISAM Crash Error"
description: "Fix MariaDB MyISAM crash error. Resolve MyISAM crash recovery issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB MyISAM Crash Error

MyISAM tables are inconsistent after a crash. The crash recovery did not complete.

## Common Causes

- Server crashed during MyISAM write
- Crash recovery was interrupted
- Table was open during crash

## How to Fix

### Solution 1

```bash
mysqlcheck --all-databases --check
```

### Solution 2

```bash
mysqlcheck --all-databases --repair
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
