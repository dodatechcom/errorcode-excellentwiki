---
title: "[Solution] xCluster Replication Error — How to Fix"
description: "Fix YugabyteDB xCluster replication errors by resolving cross-cluster replication failures, fixing CDC issues, and handling bidirectional sync"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# xCluster Replication Error

xCluster replication errors occur when replicating data between two independent YugabyteDB clusters for disaster recovery or multi-region deployments.

## Why It Happens

- Replication stream is broken between clusters
- Network connectivity between clusters is lost
- Target cluster is not reachable
- Replication lag exceeds acceptable threshold
- Table schemas diverge between clusters
- Replication is not enabled for the table

## Common Error Messages

```
ERROR: xCluster replication stream not found
```

```
ERROR: cannot replicate to unreachable cluster
```

```
ERROR: schema mismatch between source and target
```

```
ERROR: replication lag too high
```

## How to Fix It

### 1. Check xCluster Status

```bash
# Check replication status
/home/yugabyte/master/bin/yb-admin setup_universe_replication \\
  source_universe_uuid target_master_addresses

# List replication streams
/home/yugabyte/master/bin/yb-admin list_replication_statss
```

### 2. Setup Replication

```bash
# Setup xCluster replication
/home/yugabyte/master/bin/yb-admin setup_universe_replication \\
  source_universe_uuid \\
  target_master_addresses \\
  table_id1,table_id2

# Check replication health
/home/yugabyte/master/bin/yb-admin get_replication_status
```

### 3. Fix Replication Stream

```bash
# Remove broken replication
/home/yugabyte/master/bin/yb-admin delete_replication \\
  source_universe_uuid

# Re-setup replication
/home/yugabyte/master/bin/yb-admin setup_universe_replication \\
  source_universe_uuid \\
  target_master_addresses \\
  table_ids
```

### 4. Monitor xCluster

```bash
# Check replication lag
/home/yugabyte/master/bin/yb-admin get_replication_status | grep lag

# Monitor network between clusters
ping target-cluster-yb-master-1
nc -zv target-cluster-yb-master-1 7100
```

## Common Scenarios

- **Replication lag spikes**: Check network bandwidth between clusters.
- **Schema mismatch**: Ensure DDL changes are applied to both clusters.
- **Replication stream broken**: Remove and re-setup replication.

## Prevent It

- Monitor replication lag continuously
- Apply DDL changes to both clusters
- Use automated failover for disaster recovery

## Related Pages

- [YugabyteDB DR Error](/tools/yugabyte/yugabyte-dr-error)
- [YugabyteDB XDC Error](/tools/yugabyte/yugabyte-xdc-error)
- [YugabyteDB Replication Error](/tools/yugabyte/yugabyte-replication-error)