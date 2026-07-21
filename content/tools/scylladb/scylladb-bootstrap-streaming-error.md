---
title: "[Solution] ScyllaDB Bootstrap Streaming Error — How to Fix"
description: "Fix ScyllaDB bootstrap streaming errors when new nodes fail to join the cluster and stream data"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Bootstrap Streaming Error

Bootstrap streaming errors occur when a new ScyllaDB node fails to stream data from existing nodes during the bootstrap (join) process.

## Why It Happens

- Existing nodes are too overloaded to serve streaming requests
- Network bandwidth is insufficient for the data transfer
- Token range assignments conflict with existing nodes
- Schema disagreement prevents streaming from starting
- SSTable files are corrupted on existing nodes

## Common Error Messages

```
Streaming error: failed to stream data from existing nodes
```

```
error: bootstrap: unable to get ranges from existing nodes
```

```
ERROR: Streaming failed for keyspace mykeyspace
```

## How to Fix It

### 1. Check Cluster Status Before Bootstrap

```bash
nodetool status
nodetool describecluster
```

### 2. Reduce Load on Existing Nodes

```bash
# Pause compaction on existing nodes during bootstrap
nodetool compaction -p -d mykeyspace
```

### 3. Use Throttled Streaming

```yaml
# In scylla.yaml on the new node
streaming_throughput_mb_per_sec: 256
```

### 4. Retry Bootstrap After Fixing Issues

```bash
# If bootstrap fails, decommission and restart
nodetool decommission
# Fix issues on existing nodes, then restart bootstrap
scylla --join-cluster
```

## Examples

```
INFO  [main] 2024-01-15 10:30:00,001 [StreamSession] Stream session completed for keyspace mykeyspace
ERROR [main] 2024-01-15 10:35:00,001 [StreamSession] Stream failed with errors: Connection refused
```

## Prevent It

- Ensure all existing nodes are healthy before adding a new node
- Monitor streaming progress with nodetool netstats
- Schedule node additions during maintenance windows

## Related Pages

- [ScyllaDB Bootstrap Error](/tools/scylladb/scylladb-bootstrap-error)
- [ScyllaDB Bootstrap Failed](/tools/scylladb/scylladb-bootstrap-failed)
- [ScyllaDB Streaming Error](/tools/scylladb/scylladb-streaming-error)
