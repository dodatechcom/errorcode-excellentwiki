---
title: "[Solution] MariaDB Encountered Error"
description: "Fix MariaDB encountered error. Resolve generic server error issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Encountered Error

MariaDB encounters an internal error. The error may be caused by a bug or misconfiguration.

## Common Causes

- Internal server error occurred
- Configuration is wrong
- Bug in MariaDB version

## How to Fix

### Solution 1

```bash
mysql -e "SHOW ERRORS;"
```

### Solution 2

```bash
mysql -e "SHOW WARNINGS;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
