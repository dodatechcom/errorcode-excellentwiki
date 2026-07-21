---
title: "[Solution] MariaDB Secure Transport Error"
description: "Fix MariaDB secure transport error. Resolve SSL/TLS connection requirement issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Secure Transport Error

The connection requires SSL/TLS but the client is not using it. The server rejects the connection.

## Common Causes

- require_secure_transport is ON
- Client does not use SSL/TLS
- SSL certificate is not configured

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'require_secure_transport';"
```

### Solution 2

```bash
mysql -e "SHOW VARIABLES LIKE '%ssl%';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
