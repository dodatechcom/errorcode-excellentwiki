---
title: "[Solution] MariaDB Galera Node Not Synced Error"
description: "Fix MariaDB Galera node not synced error. Resolve Galera synchronization issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Galera Node Not Synced Error

A Galera node is not synchronized with the cluster. The node is in DONOR or JOINER state.

## Common Causes

- Node is in state transfer (SST/IST)
- Node is too far behind
- Network is slow between nodes

## How to Fix

### Solution 1

```bash
mysql -e "SHOW STATUS LIKE 'wsrep_cluster_status';"
```

### Solution 2

```bash
mysql -e "SHOW STATUS LIKE 'wsrep_local_state_comment';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
