---
title: "[Solution] ScyllaDB Partitioner Error — How to Fix"
description: "Fix ScyllaDB partitioner errors by correcting token range configuration, resolving uneven data distribution, and fixing partitioner mismatches"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Partitioner Error

ScyllaDB partitioner errors occur when the token partitioner configuration causes uneven data distribution, hotspots, or query routing failures across the cluster.

## Why It Happens

- Partitioner class is not consistent across all nodes
- Token ranges overlap or leave gaps
- Data is unevenly distributed causing hotspots
- Initial tokens are not properly calculated
- Virtual nodes (vnodes) configuration is inconsistent
- Partitioner cannot calculate tokens for new node

## Common Error Messages

```
InvalidTokenRange: Token range not owned by this node
```

```
PartitionerError: Cannot locate partition for key
```

```
UnevenDistribution: Data distribution is severely unbalanced
```

```
TokenRangeError: Overlapping token ranges detected
```

## How to Fix It

### 1. Check Partitioner Configuration

```bash
# Check current partitioner
nodetool describecluster | grep Partitioner

# View token ring
nodetool ring

# Check tokens per node
nodetool ring | awk '{print $1, $4}' | sort -u
```

### 2. Fix Uneven Data Distribution

```bash
# Check data distribution per node
nodetool tablestats mykeyspace.mytable | grep -E "(Owner|Live|SSTables)"

# Move token to balance data
nodetool movetoken <new_token>

# Rebalance with vnodes
# In scylla.yaml:
# num_tokens: 256  (default)
# allocate_tokens_for_local_replication_factor: 3
```

### 3. Configure Vnodes Properly

```yaml
# In scylla.yaml on ALL nodes
num_tokens: 256
allocate_tokens_for_local_replication_factor: 3

# For new clusters, use more tokens for better distribution
num_tokens: 256

# For existing clusters, do NOT change num_tokens
# This requires rebuilding the cluster
```

### 4. Verify Token Assignment

```bash
# List all tokens
nodetool ring | grep -E "^(IP|Datacenter)" -A 100

# Check for gaps in token ring
nodetool ring | awk 'NR>4 {print $4}' | sort -n | uniq -c

# Verify each node owns its ranges
nodetool ownership mykeyspace
```

## Common Scenarios

- **New node has most of the data**: Allow time for streaming to complete or rebalance manually.
- **Token ring has gaps**: Use vnodes for automatic token distribution.
- **Partitioner mismatch**: Ensure all nodes use the same partitioner class.

## Prevent It

- Use vnodes (num_tokens: 256) for automatic token management
- Monitor data distribution across nodes regularly
- Use `allocate_tokens_for_local_replication_factor` for optimal placement

## Related Pages

- [ScyllaDB Range Error](/tools/scylladb/scylladb-range-error)
- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
- [ScyllaDB Streaming Error](/tools/scylladb/scylladb-streaming-error)
