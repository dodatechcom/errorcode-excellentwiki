---
title: "[Solution] MariaDB Master Info Corrupted Error"
description: "Fix MariaDB master info corrupted error. Resolve replication metadata issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Master Info Corrupted Error

The master.info file is corrupted. The slave cannot determine replication coordinates.

## Common Causes

- master.info file is corrupted
- File was manually edited
- Disk failure corrupted the file

## How to Fix

### Solution 1

```bash
ls -la /var/lib/mysql/master.info
```

### Solution 2

```bash
mysql -e "SHOW SLAVE STATUS\G"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
