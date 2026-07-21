---
title: "[Solution] MariaDB Galera Primary Component Error"
description: "Fix MariaDB Galera primary component error. Resolve Galera primary/primary election issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Galera Primary Component Error

The cluster cannot elect a primary component. Read-only mode is activated.

## Common Causes

- Cluster is partitioned
- Quorum is lost
- Primary component was manually stopped

## How to Fix

### Solution 1

```bash
mysql -e "SHOW STATUS LIKE 'wsrep_cluster_status';"
```

### Solution 2

```bash
mysql -e "SHOW STATUS LIKE 'wsrep_cluster_size';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
