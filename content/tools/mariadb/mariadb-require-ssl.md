---
title: "[Solution] MariaDB Require SSL Error"
description: "Fix MariaDB require SSL error. Resolve per-user SSL requirement issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Require SSL Error

The user account requires SSL but the client connects without SSL.

## Common Causes

- REQUIRE SSL is set on the user
- Client does not support SSL
- SSL is not configured on server

## How to Fix

### Solution 1

```bash
mysql -u root -e "SHOW GRANTS FOR 'myuser'@'%';"
```

### Solution 2

```bash
mysql -u root -e "ALTER USER 'myuser'@'%' REQUIRE NONE;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
