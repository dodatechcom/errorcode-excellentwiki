---
title: "[Solution] YugabyteDB XDC Error — How to Fix"
description: "Fix YugabyteDB cross-datacenter replication errors by resolving XDC failures, fixing multi-region issues, and handling latency problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB XDC Error

YugabyteDB cross-datacenter (XDC) errors occur when replicating data between YugabyteDB clusters in different datacenters or cloud regions.

## Why It Happens

- Network latency between datacenters is too high
- Replication stream breaks due to network issues
- Clock skew between datacenters exceeds threshold
- Schema changes are not propagated to all datacenters
- Replication factor exceeds available nodes in remote DC
- Firewall blocks inter-datacenter traffic

## Common Error Messages

```
ERROR: cross-datacenter replication failed
```

```
ERROR: replication lag too high between DCs
```

```
ERROR: network timeout between datacenters
```

```
ERROR: clock skew between datacenters
```

## How to Fix It

### 1. Check XDC Status

```bash
# Check replication status between DCs
/home/yugabyte/master/bin/yb-admin get_replication_status

# Check network latency
ping -c 10 yb-master-dc2-1

# Check clock synchronization
chronyc tracking
```

### 2. Fix Network Issues

```bash
# Open inter-datacenter ports
# Primary DC:
sudo ufw allow from 10.1.0.0/16 to any port 7100
sudo ufw allow from 10.1.0.0/16 to any port 9100

# Test connectivity
nc -zv yb-master-dc2-1 7100
nc -zv yb-tserver-dc2-1 9100
```

### 3. Configure XDC Replication

```bash
# Setup cross-datacenter replication
/home/yugabyte/master/bin/yb-admin setup_universe_replication \\
  dc1_universe_uuid \\
  dc2_master_addresses \\
  table_ids

# Monitor replication lag
/home/yugabyte/master/bin/yb-admin get_replication_status | grep lag
```

### 4. Optimize for Latency

```bash
# Increase timeout for high-latency links
# In tserver.gflags:
--retryable_rpc_single_message_timeout_ms=60000
--retryable_rpc_max_message_size=104857600

# Use LOCAL_QUORUM for low-latency reads
SET yb_read_from_restart = false;
```

## Common Scenarios

- **Replication lag between DCs**: Check network bandwidth and reduce write throughput.
- **Clock skew causes issues**: Ensure NTP is configured on all nodes in all DCs.
- **Firewall blocks replication**: Open required ports between datacenters.

## Prevent It

- Monitor inter-datacenter latency continuously
- Use appropriate consistency levels for cross-DC operations
- Ensure clock synchronization across all datacenters

## Related Pages

- [YugabyteDB DR Error](/tools/yugabyte/yugabyte-dr-error)
- [YugabyteDB Replication Error](/tools/yugabyte/yugabyte-replication-error)
- [YugabyteDB Clock Error](/tools/yugabyte/yugabyte-clock-error)
