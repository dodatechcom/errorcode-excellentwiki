---
title: "[Solution] MariaDB Thread Cache Error"
description: "Fix MariaDB thread cache error. Resolve thread caching configuration issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Thread Cache Error

The thread cache is too small. New threads are created for each connection instead of being cached.

## Common Causes

- thread_cache_size is too low
- Too many connections are created
- Thread creation overhead is high

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'thread_cache_size';"
```

### Solution 2

```bash
mysql -e "SHOW GLOBAL STATUS LIKE 'Threads_created';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
