---
title: "[Solution] ScyllaDB Streaming Error — How to Fix"
description: "Fix ScyllaDB streaming errors by resolving bootstrap failures, fixing streaming timeouts, and recovering from failed decommission operations"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Streaming Error

ScyllaDB streaming errors occur when data transfer between nodes fails during operations like bootstrap, decommission, repair, or range movements.

## Why It Happens

- Bootstrap fails because the new node cannot receive data
- Decommission fails due to insufficient node capacity
- Streaming timeout is too low for large data transfers
- Network bandwidth is saturated during streaming
- Target node runs out of disk space during streaming
- Streaming page size is too large for available memory

## Common Error Messages

```
StreamingError: Stream failed for table mykeyspace.mytable
```

```
StreamingTimeout: Streaming operation timed out
```

```
BootstrapFailure: Failed to bootstrap node - streaming failed
```

```
DecommissionFailure: Node decommission failed
```

## How to Fix It

### 1. Check Streaming Status

```bash
# Monitor active streams
nodetool netstats

# Check streaming progress
nodetool status

# View streaming page statistics
nodetool tablestats mykeyspace.mytable | grep -i streaming
```

### 2. Increase Streaming Timeouts

```yaml
# In scylla.yaml
streaming_timeout_in_ms: 86400000  # 24 hours
streaming_keep_alive_period_in_secs: 300
```

```bash
# Monitor streaming progress
watch -n 5 'nodetool netstats | head -20'

# Check streaming throughput
iostat -x 1
```

### 3. Fix Bootstrap Failure

```bash
# Check bootstrap status
nodetool status | grep -i "boot\|join"

# If bootstrap failed, clear and retry
nodetool resetlocalinfo
nodetool cleanup

# Bootstrap with specific tokens
# In scylla.yaml:
# initial_token: <calculated_token>
# listen_address: 10.0.0.4
```

### 4. Optimize Streaming Performance

```yaml
# In scylla.yaml - increase streaming bandwidth
streaming_keep_alive_period_in_secs: 300
streaming_timeout_in_ms: 86400000

# Reduce concurrent streams to avoid I/O saturation
# Default: 4 concurrent streams per table
```

```bash
# Limit streaming throughput during business hours
nodetool setstreamthroughput 200  # MB/s

# Increase for maintenance windows
nodetool setstreamthroughput 400
```

## Common Scenarios

- **Bootstrap times out**: Increase `streaming_timeout_in_ms` and ensure sufficient bandwidth.
- **Decommission fails**: Ensure target nodes have enough capacity to receive data.
- **Streaming I/O saturated**: Reduce `streaming_throughput_mb_per_sec` during peak hours.

## Prevent It

- Monitor streaming metrics during topology changes
- Schedule node additions during low-traffic periods
- Ensure adequate network bandwidth between nodes

## Related Pages

- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
- [ScyllaDB Replication Error](/tools/scylladb/scylladb-replication-error)
- [ScyllaDB Disk Error](/tools/scylladb/scylladb-disk-error)
