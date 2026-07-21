---
title: "[Solution] MariaDB Galera EVS Suspect Error"
description: "Fix MariaDB Galera EVS suspect error. Resolve Evs (Virtual Synchrony) issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB Galera EVS Suspect Error

The EVS layer suspects a node is down. The node may be partitioned or slow.

## Common Causes

- Node is not responding to EVS heartbeats
- Network latency is high
- Node is overloaded

## How to Fix

### Solution 1

```bash
mysql -e "SHOW STATUS LIKE 'wsrep_evs%';"
```

### Solution 2

```bash
mysql -e "SHOW STATUS LIKE 'wsrep_cluster_status';"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
