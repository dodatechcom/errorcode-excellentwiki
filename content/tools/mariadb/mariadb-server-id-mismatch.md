---
title: "[Solution] MariaDB Server ID Mismatch Error"
description: "Fix MariaDB server ID mismatch error. Resolve replication server ID issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Server ID Mismatch Error

The server_id is not unique across replication topology. Replication fails due to ID conflict.

## Common Causes

- Server IDs are the same on master and slave
- Server ID was changed without restart
- Multiple slaves have same ID

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'server_id';"
```

### Solution 2

```bash
mysql -e "SHOW SLAVE STATUS\G"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
