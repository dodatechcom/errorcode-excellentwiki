---
title: "[Solution] CouchDB Shard Distribution Error — How to Fix"
description: "Fix CouchDB shard distribution errors by resolving uneven shard placement, fixing shard migration issues, and handling cluster rebalancing problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Shard Distribution Error

CouchDB shard distribution errors occur when database shards are unevenly distributed across cluster nodes, causing performance bottlenecks or unavailability.

## Why It Happens

- Cluster was not properly balanced during setup
- Node was added or removed without rebalancing
- Shard ranges are overlapping
- Some nodes have more shards than others
- Shard placement does not match node capabilities
- Network partitions caused inconsistent shard maps

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Shard distribution uneven" }
```

```
{ "error": "not_found", "reason": "No shard available for range" }
```

```
{ "error": "internal_server_error", "reason": "Shard migration failed" }
```

```
{ "error": "internal_server_error", "reason": "Cluster rebalance failed" }
```

## How to Fix It

### 1. Check Shard Distribution

```bash
# View shard map
curl http://localhost:5984/_node/_local/_shards | jq .

# Count shards per node
curl http://localhost:5984/_node/_local/_shards | jq '
  to_entries | map(.value | to_entries) | flatten | group_by(.value) | map({node: .[0].value, count: length})
'
```

### 2. Check Cluster Membership

```bash
# List all cluster nodes
curl http://localhost:5984/_membership | jq '.all_nodes, .cluster_nodes'

# Check node status
curl http://localhost:5984/_node/_all | jq '.nodes'
```

### 3. Rebalance Shards

```bash
# Add a new node
curl -X PUT http://localhost:5984/_nodes/node2@node2.example.com \
  -H "Content-Type: application/json" \
  -d '{"cluster_n": 3, "cluster_q": 2, "cluster_r": 2}'

# Trigger rebalance via Fauxton or API
curl -X POST http://localhost:5984/_cluster_setup \
  -H "Content-Type: application/json" \
  -d '{"action": "rebalance"}'
```

### 4. Fix Shard Range Issues

```bash
# Check for overlapping shards
curl http://localhost:5984/_node/_local/_shards | jq '
  to_entries | map(select(.key | startswith("shards/"))) | map(.value | keys) | flatten | sort
'

# Recreate database if shard map is corrupted
# WARNING: This destroys data - restore from backup first
curl -X DELETE http://localhost:5984/mydb
curl -X PUT http://localhost:5984/mydb
```

## Common Scenarios

- **Uneven shard distribution**: Run cluster rebalance operation.
- **Shard migration fails**: Check network connectivity between nodes.
- **No shard available**: Ensure all nodes are running and reachable.

## Prevent It

- Use automatic shard rebalancing tools
- Monitor shard distribution regularly
- Add nodes during low-traffic periods

## Related Pages

- [CouchDB Shard Error](/tools/couchdb/couchdb-shard-error)
- [CouchDB Cluster Error](/tools/couchdb/couchdb-cluster-error)
- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
