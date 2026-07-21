---
title: "[Solution] MariaDB aria_chk Error"
description: "Fix MariaDB aria_chk error. Resolve Aria table check issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB aria_chk Error

The aria_chk tool finds errors in Aria tables. The table or log may be corrupted.

## Common Causes

- Aria table has errors
- Aria log file is corrupted
- aria_chk cannot fix the errors

## How to Fix

### Solution 1

```bash
aria_chk --check /var/lib/mysql/mydb/mytable.aria
```

### Solution 2

```bash
aria_chk --recover /var/lib/mysql/mydb/mytable.aria
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
