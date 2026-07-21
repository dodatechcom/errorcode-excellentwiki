---
title: "[Solution] MariaDB Proxy User Error"
description: "Fix MariaDB proxy user error. Resolve proxy user and authentication issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Proxy User Error

The proxy user cannot impersonate another user. The proxy privilege is missing.

## Common Causes

- PROXY privilege is not granted
- Proxy user mapping is wrong
- Authentication plugin mismatch

## How to Fix

### Solution 1

```bash
mysql -u root -e "SHOW GRANTS FOR 'proxy_user'@'%';"
```

### Solution 2

```bash
mysql -u root -e "GRANT PROXY ON 'target_user'@'%' TO 'proxy_user'@'%';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
