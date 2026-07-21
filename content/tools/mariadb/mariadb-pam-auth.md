---
title: "[Solution] MariaDB PAM Auth Error"
description: "Fix MariaDB PAM auth error. Resolve PAM authentication issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB PAM Auth Error

PAM authentication fails. The PAM module is not configured or the PAM backend is unavailable.

## Common Causes

- PAM plugin is not installed
- PAM service is not configured
- PAM backend is not accessible

## How to Fix

### Solution 1

```bash
mysql -e "SHOW PLUGINS;"
```

### Solution 2

```bash
cat /etc/pam.d/mysql
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
