---
title: "[Solution] MariaDB Galera Flow Control Paused Error"
description: "Fix MariaDB Galera flow control paused error. Resolve Galera backpressure issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Galera Flow Control Paused Error

Galera flow control is activated. The cluster is applying writes slower than receiving them.

## Common Causes

- Write set apply is too slow
- Node is overloaded
- Flow control threshold is reached

## How to Fix

### Solution 1

```bash
mysql -e "SHOW STATUS LIKE 'wsrep_flow_control%';"
```

### Solution 2

```bash
mysql -e "SHOW STATUS LIKE 'wsrep_apply_oooe';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
