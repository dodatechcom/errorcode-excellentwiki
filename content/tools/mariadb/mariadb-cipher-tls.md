---
title: "[Solution] MariaDB Cipher TLS Error"
description: "Fix MariaDB cipher TLS error. Resolve TLS cipher configuration issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Cipher TLS Error

The TLS cipher suite is not supported or not allowed. The connection fails cipher negotiation.

## Common Causes

- Cipher is not allowed by server
- Cipher is not supported by client
- TLS version and cipher mismatch

## How to Fix

### Solution 1

```bash
mysql -e "SHOW VARIABLES LIKE 'ssl_cipher';"
```

### Solution 2

```bash
openssl ciphers -v 'ALL'
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
