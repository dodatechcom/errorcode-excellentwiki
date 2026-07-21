---
title: "[Solution] MariaDB OQGraph Engine Error"
description: "Fix MariaDB OQGraph engine error. Resolve graph query issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB OQGraph Engine Error

The OQGraph storage engine encounters errors. Graph queries fail.

## Common Causes

- OQGraph plugin is not installed
- Graph data is malformed
- Plugin has bugs

## How to Fix

### Solution 1

```bash
mysql -e "SHOW PLUGINS;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
