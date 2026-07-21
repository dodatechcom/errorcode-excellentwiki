---
title: "[Solution] MariaDB Pool of Threads Error"
description: "Fix MariaDB pool of threads error. Resolve thread pooling plugin issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Pool of Threads Error

The pool-of-threads (XtraDB) plugin encounters errors. Worker threads are not functioning.

## Common Causes

- Plugin is not installed or enabled
- Pool size is too small
- Plugin configuration is wrong

## How to Fix

### Solution 1

```bash
mysql -e "SHOW PLUGINS;"
```

### Solution 2

```bash
mysql -e "SHOW VARIABLES LIKE 'thread_pool%';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
