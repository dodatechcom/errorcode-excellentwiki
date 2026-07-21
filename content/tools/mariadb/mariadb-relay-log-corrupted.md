---
title: "[Solution] MariaDB Relay Log Corrupted Error"
description: "Fix MariaDB relay log corrupted error. Resolve relay log integrity issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Relay Log Corrupted Error

The relay log file is corrupted. The slave cannot read relay log entries.

## Common Causes

- Relay log file is corrupted
- Disk failure corrupted relay logs
- Incomplete shutdown corrupted logs

## How to Fix

### Solution 1

```bash
ls -la /var/lib/mysql/relay-log*
```

### Solution 2

```bash
mysql -e "SHOW SLAVE STATUS\G"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
