---
title: "[Solution] YugabyteDB Shuffle Error — How to Fix"
description: "Fix YugabyteDB data shuffle errors by resolving tablet movement failures, fixing data redistribution issues, and handling load balancing problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Shuffle Error

YugabyteDB shuffle errors occur when data movement or load balancing between TServers fails. Data shuffle redistributes tablets for even load distribution.

## Why It Happens

- Tablet movement fails due to insufficient disk space
- Load balancer cannot find suitable destination
- Too many concurrent tablet movements
- Destination TServer is overloaded
- Tablet leader cannot be transferred
- Network between TServers is degraded

## Common Error Messages

```
ERROR: tablet move failed
```

```
ERROR: load balancer cannot find destination
```

```
ERROR: tablet leader transfer failed
```

```
WARNING: too many concurrent tablet moves
```

## How to Fix It

### 1. Check Load Balancer Status

```bash
# Check tablet distribution
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers

# Check load balancer status
curl http://yb-master-1:7000/cluster-config | jq '.cluster_config'

# Monitor tablet movement
grep "tablet.*move\|load.*balanc" /home/yugabyte/yugabyte-data/master/logs/yb-master.INFO | tail -20
```

### 2. Fix Tablet Movement

```bash
# Check tablet replicas
/home/yugabyte/tserver/bin/yb-admin get_tablet_replicas <tablet_id>

# Manually move tablet if needed
/home/yugabyte/tserver/bin/yb-admin move_tablet <tablet_id> <dest_tserver>

# Check available capacity on TServers
for ts in yb-tserver-1 yb-tserver-2 yb-tserver-3; do
  echo "$ts: $(ssh $ts df -h /home/yugabyte/yugabyte-data/tserver | tail -1)"
done
```

### 3. Configure Load Balancer

```bash
# In master.gflags:
--load_balancer_max_overreplicated_tablets=10
--load_balancer_max_concurrent_moves=1

# Monitor balance
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers
```

### 4. Monitor Shuffle Operations

```bash
# Check active tablet movements
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers

# Monitor data distribution
curl http://yb-tserver-1:9000/metrics | grep tablet

# Check disk usage per TServer
for ts in yb-tserver-1 yb-tserver-2 yb-tserver-3; do
  echo "$ts disk usage:"
  ssh $ts "du -sh /home/yugabyte/yugabyte-data/tserver/"
done
```

## Common Scenarios

- **Tablet movement fails**: Check destination TServer has enough disk space.
- **Load is uneven**: Allow time for automatic rebalancing or manually move tablets.
- **Too many concurrent moves**: Reduce max_concurrent_moves setting.

## Prevent It

- Monitor tablet distribution across TServers
- Ensure adequate disk space on all nodes
- Configure appropriate load balancer settings

## Related Pages

- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
- [YugabyteDB Split Error](/tools/yugabyte/yugabyte-split-error)
