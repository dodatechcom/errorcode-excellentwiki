---
title: "[Solution] TiDB TSO Error — How to Fix"
description: "Fix TiDB TSO errors by resolving Timestamp Oracle failures, fixing PD clock synchronization, and handling TSO timeout issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB TSO Error

TiDB TSO (Timestamp Oracle) errors occur when the PD server cannot allocate timestamps, causing transaction failures. TSO is critical for distributed transaction ordering.

## Why It Happens

- PD server is down or unreachable
- PD clock is not synchronized
- TSO allocation rate exceeds capacity
- Network latency causes TSO timeout
- PD disk is full or slow
- Too many concurrent transactions request TSO

## Common Error Messages

```
ERROR: PD timeout: cannot get TSO
```

```
ERROR: TSO allocation failed
```

```
FATAL: PD is not reachable
```

```
ERROR: TSO lease expired
```

## How to Fix It

### 1. Check PD Status

```bash
# Check PD cluster status
curl http://pd1:2379/pd/api/v1/cluster/status

# Check PD members
curl http://pd1:2379/pd/api/v1/members

# Check TSO statistics
curl http://pd1:2379/pd/api/v1/stats/region
```

### 2. Fix PD Connectivity

```bash
# Restart PD server
sudo systemctl restart pd-server

# Check PD logs for TSO errors
grep -i "tso\|timestamp" /var/log/pd/pd.log | tail -20

# Verify PD is serving TSO
curl http://pd1:2379/pd/api/v1/tso
```

### 3. Fix Clock Synchronization

```bash
# Install and configure NTP
sudo apt install chrony
sudo systemctl enable chrony
sudo systemctl start chrony

# Check time on all nodes
for node in pd1 tidb1 tikv1; do
  echo "$node: $(ssh $node date)"
done

# Verify NTP sync
chronyc tracking
```

### 4. Optimize TSO Performance

```bash
# Increase TSO count (for high throughput)
# In pd.toml:
[lease]
enable-transfer-leader = true

# Monitor TSO allocation rate
curl http://pd1:2379/pd/api/v1/metrics | grep tso
```

## Common Scenarios

- **PD down causes TSO failure**: Ensure PD quorum (2 of 3) is maintained.
- **TSO timeout during peak**: Add more PD servers or increase TSO batch size.
- **Clock skew causes TSO issues**: Ensure NTP is running on all nodes.

## Prevent It

- Use odd number of PD nodes (3 or 5)
- Ensure NTP synchronization on all nodes
- Monitor PD health and TSO allocation rate

## Related Pages

- [TiDB PD Error](/tools/tidb/tidb-pd-error)
- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
- [TiDB Connection Error](/tools/tidb/tidb-connection-error)
