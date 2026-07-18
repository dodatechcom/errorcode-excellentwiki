---
title: "[Solution] CouchDB Cluster Error — How to Fix"
description: "Fix CouchDB cluster errors by recovering from split-brain, fixing shard placement, and resolving quorum issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Cluster Error

CouchDB cluster errors occur when the distributed database cannot maintain proper shard placement, quorum, or consistency across nodes. Cluster issues affect data availability and durability.

## Why It Happens

- Not enough nodes for the configured quorum (n, r, w values)
- Shard placement is uneven across nodes
- Network partition splits the cluster into multiple groups
- Nodes are added or removed without proper shard rebalancing
- Cluster configuration is inconsistent across nodes
- Q (shards per database) is too high for available nodes

## Common Error Messages

```
{ "error": "service_unavailable", "reason": "no_db_topology" }
```

```
{ "error": "internal_server_error", "reason": "Insufficient replicas" }
```

```
{ "error": "conflict", "reason": "quorum not met" }
```

```
{ "error": "nodedown", "reason": "all nodes are down" }
```

## How to Fix It

### 1. Check Cluster Status

```bash
# Check membership
curl http://localhost:5984/_membership

# Check database shards
curl http://localhost:5984/mydb | jq '.shard_info'

# Check cluster configuration
curl http://localhost:5984/_node/_local/_config/cluster
```

### 2. Fix Quorum Settings

```bash
# Default cluster settings
# n=3 (replicas), r=2 (read quorum), w=2 (write quorum), q=8 (shards)

# For a 3-node cluster
curl -X PUT http://localhost:5984/_node/_local/_config/cluster/n \
  -H "Content-Type: application/json" \
  -d '"3"'

curl -X PUT http://localhost:5984/_node/_local/_config/cluster/r \
  -H "Content-Type: application/json" \
  -d '"2"'

curl -X PUT http://localhost:5984/_node/_local/_config/cluster/w \
  -H "Content-Type: application/json" \
  -d '"2"'
```

### 3. Add or Remove Nodes

```bash
# Add a new node to the cluster
curl -X PUT http://node1:5984/_nodes/couchdb@node4.example.com \
  -H "Content-Type: application/json" \
  -d '{
    "cluster_nodes": {
      "n": 3,
      "q": 8,
      "r": 2,
      "w": 2
    }
  }'

# Remove a node from the cluster
curl -X DELETE http://node1:5984/_nodes/couchdb@node4.example.com

# List all cluster nodes
curl http://localhost:5984/_nodes | jq '.rows[].id'
```

### 4. Rebalance Shards

```bash
# Trigger shard rebalancing
# CouchDB automatically rebalances, but you can force it:

# Enable the balancer
curl -X PUT http://localhost:5984/_node/_local/_config/balancer/enable \
  -H "Content-Type: application/json" \
  -d '"true"'

# Check active tasks for rebalancing
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "rebalance")'

# Monitor shard distribution
curl http://localhost:5984/_dbs | jq '.rows[].node'
```

## Common Scenarios

- **Quorum not met after node loss**: Reduce `n` or add more nodes to maintain quorum.
- **Split-brain after network partition**: Ensure only one partition accepts writes.
- **Uneven shard distribution**: Enable the shard balancer and wait for redistribution.

## Prevent It

- Deploy an odd number of nodes (3 or 5) for proper quorum
- Monitor cluster health with `_membership` and `_shards` endpoints
- Use CouchDB 3.x with automatic shard rebalancing

## Related Pages

- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
- [CouchDB Shard Error](/tools/couchdb/couchdb-shard-error)
- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
