---
title: "[Solution] MariaDB Temporary File Full Error"
description: "Fix MariaDB temporary file full error. Resolve temp space exhaustion issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Temporary File Full Error

MariaDB runs out of temporary file space. Queries that need temp space fail.

## Common Causes

- Disk space for tmpdir is full
- Large sort or GROUP BY needs temp space
- tmpdir is on small partition

## How to Fix

### Solution 1

```bash
df -h /tmp
```

### Solution 2

```bash
mysql -e "SHOW VARIABLES LIKE 'tmpdir';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
