---
title: "[Solution] MariaDB Ed25519 Auth Error"
description: "Fix MariaDB Ed25519 auth error. Resolve Ed25519 authentication issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Ed25519 Auth Error

Ed25519 authentication fails. The client or server does not support Ed25519.

## Common Causes

- Ed25519 plugin is not loaded
- Client does not support Ed25519
- Password hash is wrong

## How to Fix

### Solution 1

```bash
mysql -e "SHOW PLUGINS;"
```

### Solution 2

```bash
mysql -u root -e "ALTER USER 'myuser'@'%' IDENTIFIED VIA ed25519 USING PASSWORD('password');"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
