---
title: "[Solution] MariaDB Xpand Plugin Error"
description: "Fix MariaDB Xpand plugin error. Resolve Xpand storage engine plugin issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Xpand Plugin Error

The Xpand plugin encounters errors. Distributed queries are not functioning.

## Common Causes

- Xpand plugin is not installed
- Xpand cluster is not connected
- Plugin version is incompatible

## How to Fix

### Solution 1

```bash
mysql -e "SHOW PLUGINS;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
