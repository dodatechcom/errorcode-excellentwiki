---
title: "[Solution] MariaDB Galera IST Transfer Error"
description: "Fix MariaDB Galera IST transfer error. Resolve Incremental State Transfer issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Galera IST Transfer Error

The IST transfer fails. The joiner cannot apply incremental writesets from the donor.

## Common Causes

- Donor does not have required gcache
- gcache size is too small
- Network issue during transfer

## How to Fix

### Solution 1

```bash
mysql -e "SHOW STATUS LIKE 'wsrep_ist%';"
```

### Solution 2

```bash
mysql -e "SHOW VARIABLES LIKE 'wsrep_provider_options';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
