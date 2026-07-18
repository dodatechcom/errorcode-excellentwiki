---
title: "[Solution] Cassandra Range Mapping Error - Fix Token Ring Issues"
description: "Fix Cassandra range mapping and token ring errors. Resolve token allocation, partitioner configuration, and range scan issues."
tools: ["cassandra"]
error-types: ["range-mapping"]
severities: ["error"]
weight: 5
---

This error means Cassandra's token ring or range mapping is incorrect. Nodes may own overlapping token ranges, or range queries may return unexpected results.

## What This Error Means

When token ring issues occur, you see:

```
AssertionError: Token ranges are not contiguous
# or
InvalidRequestException: Range query failed
# or
nodetool ring shows unbalanced token distribution
```

The token ring determines which node owns which data. Incorrect range mapping causes data to be misplaced or inaccessible.

## Why It Happens

- Nodes have overlapping token ranges after topology changes
- The partitioner changed between cluster versions
- A node was added without proper token allocation
- Virtual nodes (vnodes) are misconfigured
- The cluster was upgraded from a pre-vnode version incorrectly
- Nodes were restarted with different tokens

## How to Fix It

### Check the token ring

```bash
nodetool ring
```

Verify tokens are evenly distributed and no ranges overlap.

### Check token ownership

```bash
nodetool describering keyspace_name
```

This shows the actual token ranges and their owners.

### Enable virtual nodes (vnodes)

```yaml
# cassandra.yaml
num_tokens: 256
allocate_tokens_for_keyspace: my_keyspace
```

Vnodes distribute tokens more evenly automatically.

### Rebalance with vnode

```bash
# With vnodes enabled, restart nodes one at a time
sudo systemctl restart cassandra
```

Each restart regenerates tokens for better distribution.

### Check partitioner configuration

```yaml
# cassandra.yaml
partitioner: org.apache.cassandra.dht.Murmur3Partitioner
```

All nodes must use the same partitioner.

### Repair after topology changes

```bash
nodetool repair keyspace_name table_name
```

Repair ensures data is on the correct nodes after range changes.

### Check for range scan failures

```cql
-- Ensure range queries include the partition key
SELECT * FROM users WHERE user_id >= 100 AND user_id <= 200 ALLOW FILTERING;
```

### Monitor data distribution

```bash
nodetool tablestats keyspace_name.table_name
```

Check if data is evenly distributed across nodes.

### Use nodetool for ring inspection

```bash
nodetool ring | grep -E "UN|DN|UJ"
```

Focus on Up Normal (UN) and Down Normal (DN) nodes.

### Verify token allocation after adding nodes

```bash
nodetool ring | awk '{print $1, $4, $5}'
```

Each node should own roughly 1/N of the token range.

## Common Mistakes

- Not using virtual nodes (vnodes) which simplify token management
- Changing the partitioner without understanding the impact
- Not running repair after adding or removing nodes
- Assuming token distribution is even without checking
- Mixing vnodes and single-token nodes in the same cluster

## Related Pages

- [Cassandra Gossip Error]({{< relref "/tools/cassandra/cassandra-gossip-error" >}}) -- gossip issues
- [Cassandra Joins Leave]({{< relref "/tools/cassandra/cassandra-joins-leave" >}}) -- node membership
- [Cassandra Nodetool Error]({{< relref "/tools/cassandra/cassandra-nodetool-error" >}}) -- management issues
