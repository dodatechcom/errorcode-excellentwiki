---
title: "[Solution] YugabyteDB DR Error — How to Fix"
description: "Fix YugabyteDB disaster recovery errors by resolving xCluster DR failures, fixing standby cluster issues, and handling failover procedures"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB DR Error

YugabyteDB disaster recovery errors occur when xCluster DR (Disaster Recovery) replication fails between primary and standby clusters.

## Why It Happens

- Standby cluster is unreachable from primary
- Replication stream is broken
- Failover is attempted while replication lag is high
- Standby cluster schema diverges from primary
- Network partition between clusters
- Replication is not properly configured

## Common Error Messages

```
ERROR: DR replication not active
```

```
ERROR: standby cluster unreachable
```

```
ERROR: replication lag exceeds threshold
```

```
ERROR: schema mismatch between primary and standby
```

## How to Fix It

### 1. Check DR Status

```bash
# Check replication status
/home/yugabyte/master/bin/yb-admin get_replication_status

# Check cluster config for xCluster
curl http://yb-master-primary-1:7000/cluster-config | jq '.cluster_config'

# Check standby cluster status
curl http://yb-master-standby-1:7000/cluster-config | jq '.tablet_servers'
```

### 2. Setup xCluster DR

```bash
# Setup replication from primary to standby
/home/yugabyte/master/bin/yb-admin setup_universe_replication \\
  source_universe_uuid \\
  standby_master_addresses \\
  table_id1,table_id2

# Check replication health
/home/yugabyte/master/bin/yb-admin get_replication_status
```

### 3. Perform Failover

```bash
# When primary is down, promote standby
# 1. Stop replication on standby
/home/yugabyte/master/bin/yb-admin delete_replication source_universe_uuid

# 2. Verify standby is healthy
curl http://yb-master-standby-1:7000/healthz

# 3. Update application connection strings to standby
```

### 4. Monitor DR Health

```bash
# Monitor replication lag
/home/yugabyte/master/bin/yb-admin get_replication_status | grep lag

# Check network between clusters
ping yb-master-standby-1
nc -zv yb-master-standby-1 7100

# Monitor failover readiness
/home/yugabyte/master/bin/yb-admin list_masters
```

## Common Scenarios

- **Replication lag spikes**: Check network bandwidth and cluster load.
- **Failover during high lag**: Wait for lag to reduce or accept potential data loss.
- **Standby cannot be promoted**: Ensure all replication is stopped before promotion.

## Prevent It

- Monitor replication lag continuously
- Test failover procedures regularly
- Keep standby cluster schema in sync with primary

## Related Pages

- [YugabyteDB XDC Error](/tools/yugabyte/yugabyte-xdc-error)
- [YugabyteDB Replication Error](/tools/yugabyte/yugabyte-replication-error)
- [YugabyteDB Backup Error](/tools/yugabyte/yugabyte-backup-error)
