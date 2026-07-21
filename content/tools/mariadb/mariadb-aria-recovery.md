---
title: "[Solution] MariaDB Aria Recovery Error"
description: "Fix MariaDB Aria recovery error. Resolve Aria crash recovery issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Aria Recovery Error

Aria fails to recover after a crash. The transaction log or table may be inconsistent.

## Common Causes

- Crash during write to Aria table
- Transaction log is corrupted
- Recovery process failed

## How to Fix

### Solution 1

```bash
aria_chk --check /var/lib/mysql/mydb/mytable.aria
```

### Solution 2

```bash
mysql -e "REPAIR TABLE mydb.mytable;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
