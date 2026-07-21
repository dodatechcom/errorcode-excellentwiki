---
title: "[Solution] MariaDB Sort Buffer Too Small Error"
description: "Fix MariaDB sort buffer too small error. Resolve sort buffer configuration issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Sort Buffer Too Small Error

The sort buffer is too small for the query. MariaDB allocates additional sort buffers.

## Common Causes

- sort_buffer_size is too low
- Query requires sorting large result set
- ORDER BY on large table

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'sort_buffer_size';"
```

### Solution 2

```bash
mysql -e "SET SESSION sort_buffer_size = 4194304;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
