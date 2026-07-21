---
title: "[Solution] MariaDB Audit Log Error"
description: "Fix MariaDB audit log error. Resolve audit logging plugin issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Audit Log Error

The audit log plugin encounters errors. Audit events are not being recorded.

## Common Causes

- Audit plugin is not installed or enabled
- Log file is not writable
- Plugin configuration is wrong

## How to Fix

### Solution 1

```bash
mysql -e "SHOW PLUGINS;"
```

### Solution 2

```bash
mysql -e "SHOW VARIABLES LIKE 'server_audit%';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
