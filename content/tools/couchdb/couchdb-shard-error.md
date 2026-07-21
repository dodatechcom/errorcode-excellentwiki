---
title: "[Solution] CouchDB Shard Error — How to Fix"
description: "Fix CouchDB shard errors by resolving shard distribution problems, fixing shard corruption, and handling shard reassignment issues in clusters"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Shard Error

CouchDB shard errors occur when database shards are not properly distributed across cluster nodes, are corrupted, or cannot be accessed.

## Why It Happens

- Shard is not reachable on its assigned node
- Shard corruption due to disk errors
- Shard range overlaps with another shard
- Node failure left orphaned shards
- Shard reassignment failed during cluster rebalance
- Shard file permissions are incorrect

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Shard not found" }
```

```
{ "error": "not_found", "reason": "No shards found for range" }
```

```
{ "error": "internal_server_error", "reason": "Shard is corrupted" }
```

```
{ "error": "internal_server_error", "reason": "Shard unreachable" }
```

## How to Fix It

### 1. Check Shard Distribution

```bash
# Check shard map
curl http://localhost:5984/_node/_local/_shards | jq .

# Check specific database shards
curl http://localhost:5984/_node/_local/_shards/mydb
```

### 2. Fix Unreachable Shards

```bash
# Check shard ownership
curl http://localhost:5984/_node/_local/_shards | jq '."shards/mydb"'

# Ensure all nodes are running
curl http://localhost:5984/_membership

# Restart problematic node
sudo systemctl restart couchdb
```

### 3. Repair Corrupted Shards

```bash
# Check shard integrity
ls -la /opt/couchdb/data/shards/

# Recreate shard from replica
curl -X DELETE http://localhost:5984/_dbs/mydb_shard_00000000
```

### 4. Rebalance Shards

```bash
# Trigger shard rebalance
curl -X POST http://localhost:5984/_cluster_setup \
  -H "Content-Type: application/json" \
  -d '{"action": "rebalance"}'
```

## Common Scenarios

- **Shard not found**: Check shard map and ensure all nodes are running.
- **Shard corruption**: Restore from replica or backup.
- **Shard unreachable**: Verify node connectivity and restart if needed.

## Prevent It

- Monitor shard distribution regularly
- Ensure sufficient replica nodes
- Use automated shard rebalancing

## Related Pages

- [CouchDB Cluster Error](/tools/couchdb/couchdb-cluster-error)
- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
