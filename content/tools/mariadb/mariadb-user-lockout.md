---
title: "[Solution] MariaDB User Lockout Error"
description: "Fix MariaDB user lockout error. Resolve account lock issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB User Lockout Error

The user account is locked after too many failed login attempts.

## Common Causes

- Too many failed login attempts
- Account was manually locked
- Password validation failed repeatedly

## How to Fix

### Solution 1

```bash
mysql -u root -e "ALTER USER 'myuser'@'%' ACCOUNT UNLOCK;"
```

### Solution 2

```bash
mysql -u root -e "SELECT user, account_locked FROM mysql.user;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
