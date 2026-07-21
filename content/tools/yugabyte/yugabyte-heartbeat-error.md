---
title: "[Solution] YugabyteDB Heartbeat Error — How to Fix"
description: "Fix YugabyteDB heartbeat errors by resolving raft heartbeat failures, fixing inter-node communication issues, and handling heartbeat timeout problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Heartbeat Error

YugabyteDB heartbeat errors occur when raft heartbeat communication between tablet servers fails, causing leader elections, tablet unavailability, or cluster instability.

## Why It Happens

- Network partition isolates nodes from each other
- Heartbeat timeout is too short for the network latency
- Tablet server is overloaded and cannot respond to heartbeats
- Clock skew between nodes causes heartbeat validation failures
- Firewall rules block heartbeat traffic on internal ports
- DNS resolution fails for inter-node communication

## Common Error Messages

```
ERROR: heartbeat timeout for tablet
```

```
WARNING: missed heartbeat from peer
```

```
ERROR: raft consensus lost for tablet
```

```
FATAL: node unreachable
```

## How to Fix It

### 1. Check Heartbeat Status

```sql
-- Check tablet leader status
yb-admin -master_addresses yugabyte:7100 list_tablets mydb.sensor_data

-- Check tablet server health
yb-admin -master_addresses yugabyte:7100 list_tablet_servers
```

### 2. Fix Network Issues

```bash
# Test connectivity between nodes
ping yugabyte2
nc -zv yugabyte2 9100

# Check DNS resolution
nslookup yugabyte2

# Verify firewall rules
sudo firewall-cmd --list-all
```

### 3. Adjust Heartbeat Configuration

```bash
# Increase heartbeat timeout in tserver gflags
--raft_heartbeat_interval_ms=1000
--leader_failure_max_missed_heartbeat_periods=5

# Increase consensus timeout
--consensus_rpc_timeout_ms=10000
```

### 4. Fix Clock Skew

```bash
# Check clock synchronization
chronyc tracking

# Sync clocks
sudo chronyc makestep

# Check time difference between nodes
for node in yugabyte yugabyte2 yugabyte3; do
  echo "$node: $(ssh $node date)"
done
```

## Common Scenarios

- **Frequent leader elections**: Increase heartbeat timeout or fix network latency.
- **Heartbeat timeout under load**: Add more tablet servers to distribute load.
- **Clock skew causes failures**: Ensure NTP is configured on all nodes.

## Prevent It

- Use low-latency networks between nodes
- Configure NTP on all cluster nodes
- Set appropriate heartbeat timeouts for the network

## Related Pages

- [YugabyteDB Raft Error](/tools/yugabyte/yugabyte-raft-error)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
