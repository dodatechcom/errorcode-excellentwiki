---
title: "[Solution] MariaDB Query Cache Disabled Error"
description: "Fix MariaDB query cache disabled error. Resolve query cache configuration issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Query Cache Disabled Error

The query cache is disabled. It was removed in MariaDB 10.1.7+.

## Common Causes

- Query cache was removed in MariaDB 10.1.7
- query_cache_type is set to OFF
- Query cache is deprecated

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'query_cache%';"
```

### Solution 2

```bash
mysql -e "SELECT VERSION();"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
