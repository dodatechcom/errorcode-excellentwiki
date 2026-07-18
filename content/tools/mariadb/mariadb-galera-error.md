---
title: "[Solution] MariaDB Galera Cluster Error — How to Fix"
description: "Fix MariaDB Galera Cluster errors including node desync, SST failures, quorum loss, and certificate conflicts in your Galera replication setup"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Galera Cluster Error

Galera Cluster provides synchronous multi-master replication for MariaDB. Errors occur when nodes lose synchronization, state snapshot transfers fail, the cluster loses quorum, or write conflicts arise.

## Why It Happens

- A node falls too far behind and cannot apply write-sets
- SST fails due to network or authentication problems
- The cluster loses quorum because majority of nodes are down
- Concurrent writes on different nodes cause certification conflicts
- The galera.cache file is too small for missed write-sets
- Firewall blocks Galera ports (4567 TCP/UDP, 4444 TCP, 4568 TCP)

## Common Error Messages

```
[ERROR] WSREP: Failed to prepare for 'rsync' SST, error: 110
[ERROR] WSREP: SST failed: 110 (Connection timed out)
```

```
[ERROR] WSREP: gcache page size too small (< write-set size)
[ERROR] WSREP: Cannot prepare IST sender: gcache error
```

```
[ERROR] WSREP: Consistency check failed: node is in non-prim state
[ERROR] WSREP: Node is not in primary component
```

```
[ERROR] WSREP: Certification failed for write-set: seqno 12345678
```

## How to Fix It

### 1. Restart a Failed SST

```bash
# Check Galera status
mysql -e "SHOW STATUS LIKE 'wsrep_%';"

# Set correct SST method in my.cnf
# [mysqld]
# wsrep_sst_method = mariabackup
# wsrep_sst_auth = root:password

# Restart the failed node
sudo systemctl restart mariadb
```

### 2. Increase Galera Cache Size

```bash
# In my.cnf on all nodes
[mysqld]
wsrep_provider_options = "gcache.size=2G; gcache.mem_size=1G"
```

### 3. Recover From Quorum Loss

```sql
-- On surviving nodes
SHOW STATUS LIKE 'wsrep_cluster_size';

-- Force new primary
SET GLOBAL wsrep_provider_options = 'pc.boostrap=YES';

-- Bring other nodes back one at a time
```

### 4. Fix IST/GCache Errors

```bash
# If gcache too small for IST, force SST
rm -rf /var/lib/mysql/*
sudo systemctl restart mariadb
```

## Common Scenarios

- **Node rejoins after long downtime**: gcache rotated past the node's position. Force SST.
- **Split brain after network partition**: Restore network, then `pc.boostrap=YES` on most authoritative node.
- **SST fails with auth error**: Set `wsrep_sst_auth` correctly in my.cnf.

## Prevent It

- Size `gcache.size` to hold write-sets from longest expected downtime
- Use at least 3 nodes for quorum tolerance
- Monitor `wsrep_cluster_size` and `wsrep_local_state_comment` continuously

## Related Pages

- [MariaDB Replication Error](/tools/mariadb/mariadb-replication-error)
- [MariaDB Connection Error](/tools/mariadb/mariadb-connection-error)
- [MySQL Galera Error](/tools/mysql/mysql-galera-error)
