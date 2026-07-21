---
title: "[Solution] MariaDB Galera Donor Not Found Error"
description: "Fix MariaDB Galera donor not found error. Resolve Galera state transfer donor issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Galera Donor Not Found Error

No donor node is available for state transfer. A new node cannot join the cluster.

## Common Causes

- All donor nodes are busy
- Donor node is not in synced state
- Donor node is down

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
