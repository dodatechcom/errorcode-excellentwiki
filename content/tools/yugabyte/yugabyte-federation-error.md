---
title: "[Solution] YugabyteDB Federation Error — How to Fix"
description: "Fix YugabyteDB cluster federation errors by resolving multi-cluster coordination issues, fixing service discovery, and handling cluster merging"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Federation Error

YugabyteDB federation errors occur when multiple YugabyteDB clusters need to coordinate for multi-region or multi-cloud deployments.

## Why It Happens

- Cluster cannot discover other clusters
- Federation metadata is out of sync
- Service discovery fails across clusters
- Cluster merge operation fails
- Federation controller is not running
- Network partition isolates clusters

## Common Error Messages

```
ERROR: cluster discovery failed
```

```
ERROR: federation metadata out of sync
```

```
ERROR: cannot connect to remote cluster
```

```
ERROR: cluster merge operation failed
```

## How to Fix It

### 1. Check Federation Status

```bash
# Check cluster discovery
curl http://yb-master-1:7000/cluster-config | jq '.cluster_config'

# Check remote cluster connectivity
/home/yugabyte/master/bin/yb-admin list_masters

# Check federation controller logs
grep "federation" /home/yugabyte/yugabyte-data/master/logs/yb-master.INFO | tail -20
```

### 2. Fix Cluster Discovery

```bash
# Configure cluster discovery
# In master.gflags:
--master_addresses=yb-master-1:7100,yb-master-2:7100,yb-master-3:7100
--enable_ondisk_compression=true

# Ensure DNS resolves for all cluster nodes
nslookup yb-master-remote-1
```

### 3. Setup Federation

```bash
# Configure cross-cluster federation
/home/yugabyte/master/bin/yb-admin setup_universe_replication \\
  source_universe_uuid \\
  remote_master_addresses \\
  table_ids

# Check replication status
/home/yugabyte/master/bin/yb-admin get_replication_status
```

### 4. Monitor Federation

```bash
# Check cluster health across federation
for cluster in cluster1 cluster2; do
  echo "=== $cluster ==="
  curl http://$cluster-yb-master-1:7000/healthz
done

# Monitor replication lag
/home/yugabyte/master/bin/yb-admin get_replication_status | grep lag
```

## Common Scenarios

- **Cluster cannot discover peers**: Check DNS and firewall rules.
- **Federation metadata out of sync**: Re-setup replication between clusters.
- **Cluster merge fails**: Ensure compatible versions and schemas.

## Prevent It

- Use consistent configuration across all clusters
- Monitor federation health with automated checks
- Test failover procedures regularly

## Related Pages

- [YugabyteDB DR Error](/tools/yugabyte/yugabyte-dr-error)
- [YugabyteDB XDC Error](/tools/yugabyte/yugabyte-xdc-error)
- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
