---
title: "[Solution] YugabyteDB Replication Error — How to Fix"
description: "Fix YugabyteDB replication errors by resolving Raft consensus issues, fixing tablet replica placement, and recovering from replication lag"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Replication Error

YugabyteDB replication errors occur when tablet replicas fail to replicate data across nodes. YugabyteDB uses Raft consensus for replication.

## Why It Happens

- Tablet replicas cannot reach quorum
- Raft leader is not elected
- Replication factor exceeds available nodes
- Network partition isolates replicas
- Replica falls too far behind and needs to be removed
- TServer hosting replicas is down

## Common Error Messages

```
ERROR: tablet not found
```

```
ERROR: not enough replicas for tablet
```

```
ERROR: raft consensus lost
```

```
ERROR: replication failed - replica unavailable
```

## How to Fix It

### 1. Check Replication Status

```bash
# List tablet servers
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers

# Check tablet status
/home/yugabyte/tserver/bin/yb-admin list_tables

# Check Master leader
/home/yugabyte/master/bin/yb-admin list_masters
```

### 2. Fix Raft Quorum

```bash
# Check tablet replicas
/home/yugabyte/tserver/bin/yb-admin get_tablet_replicas <tablet_id>

# If replica is lost, add new replica
/home/yugabyte/tserver/bin/yb-admin add_tablet_replica <tablet_id> <tserver_id>

# Move tablet if needed
/home/yugabyte/tserver/bin/yb-admin move_tablet <tablet_id> <dest_tserver>
```

### 3. Configure Replication Factor

```bash
# Set default replication factor
# In master.gflags:
--replication_factor=3

# Per-table replication factor
CREATE TABLE my_table (
  id SERIAL PRIMARY KEY,
  data TEXT
) WITH (replicas = 3);
```

### 4. Monitor Replication Health

```bash
# Check replication lag
curl http://yb-tserver-1:9000/metrics | grep replication

# Monitor tablet leader elections
grep "leader" /home/yugabyte/yugabyte-data/tserver/logs/yb-tserver.INFO | tail -20
```

## Common Scenarios

- **Replica lost after node failure**: Ensure enough nodes for RF quorum, then rebalance.
- **Replication lag increases**: Check network bandwidth and TServer load.
- **Cannot write to table**: Verify tablet leader exists and Raft quorum is maintained.

## Prevent It

- Use replication factor of 3 for production
- Monitor tablet health with yb-admin
- Ensure odd number of Masters for proper quorum

## Related Pages

- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
- [YugabyteDB Master Error](/tools/yugabyte/yugabyte-master-error)
