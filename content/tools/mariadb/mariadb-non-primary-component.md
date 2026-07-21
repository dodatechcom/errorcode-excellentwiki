---
title: "[Solution] MariaDB Galera Non-Primary Component Error"
description: "Fix MariaDB Galera non-primary component error. Resolve non-primary cluster state."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Galera Non-Primary Component Error

The node is in non-primary state. It cannot serve read-write queries.

## Common Causes

- Node is partitioned from primary
- Quorum is lost on this node
- Cluster is split-brain

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
