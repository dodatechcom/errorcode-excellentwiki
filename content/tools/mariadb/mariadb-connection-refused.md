---
title: "[Solution] MariaDB Connection Refused Error"
description: "Fix MariaDB connection refused error. Resolve TCP connection issues to the database server."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Connection Refused Error

The client cannot connect to the MariaDB server. The connection is actively refused.

## Common Causes

- MariaDB service is not running
- Bind address is set to 127.0.0.1 for remote access
- Firewall blocks port 3306

## How to Fix

### Solution 1

```bash
sudo systemctl status mariadb
```

### Solution 2

```bash
mysql -e "SHOW VARIABLES LIKE 'bind-address';"
```

### Solution 3

```bash
ss -tlnp | grep 3306
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
