---
title: "[Solution] MariaDB Role Not Found Error"
description: "Fix MariaDB role not found error. Resolve role reference issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Role Not Found Error

The specified role does not exist. The role was never created or was dropped.

## Common Causes

- Role was never created
- Role name is misspelled
- Role was dropped

## How to Fix

### Solution 1

```bash
mysql -e "SELECT * FROM mysql.roles_mapping;"
```

### Solution 2

```bash
mysql -u root -e "CREATE ROLE 'myrole';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
