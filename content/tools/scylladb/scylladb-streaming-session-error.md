---
title: "[Solution] ScyllaDB Streaming Session Error — How to Fix"
description: "Fix ScyllaDB streaming session errors when data streaming between nodes during repair or bootstrap fails"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Streaming Session Error

Streaming session errors occur when ScyllaDB fails to establish or maintain a streaming session for data transfer between nodes during operations like repair, bootstrap, or decommission.

## Why It Happens

- Target node is unreachable for streaming
- Streaming bandwidth is saturated
- SSTable files are corrupted on the source node
- Timeout exceeded during large data transfers
- Connection was interrupted by network failure

## Common Error Messages

```
StreamSession: error during streaming from node2
```

```
Streaming failed: connection reset by peer
```

```
error: stream session timed out, transferred 5GB of 10GB
```

## How to Fix It

### 1. Check Network Between Nodes

```bash
nc -zv node2 7000
ping -c 4 node2
```

### 2. Reduce Streaming Bandwidth

```bash
nodetool setstreamthroughput -t 200
```

### 3. Monitor Streaming Progress

```bash
nodetool netstats
```

### 4. Retry Streaming Operation

```bash
# For repair streaming
nodetool repair mykeyspace

# For bootstrap retry
nodetool decommission
scylla --join-cluster
```

## Examples

```
$ nodetool netstats
Mode: STREAMING
Connection: node2 (10.0.0.2)
  Streaming from: 10.0.0.2 (5.2GB / 10GB, 52%)
  Time elapsed: 120s
```

## Prevent It

- Ensure reliable network between nodes
- Schedule large streaming operations during maintenance windows
- Monitor streaming progress and adjust timeouts

## Related Pages

- [ScyllaDB Streaming Error](/tools/scylladb/scylladb-streaming-error)
- [ScyllaDB Bootstrap Streaming Error](/tools/scylladb/scylladb-bootstrap-streaming-error)
- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
