---
title: "[Solution] CouchDB Shard Error — How to Fix"
description: "Fix CouchDB shard errors by recovering from corrupted shards, fixing uneven distribution, and resolving shard conflicts"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Shard Error

CouchDB shard errors occur when individual database shards become corrupted, unbalanced, or unreachable in a clustered deployment. Shards are the fundamental unit of data distribution.

## Why It Happens

- Shard file corruption due to disk I/O errors
- Shard range overlaps after incorrect split
- Node hosting the shard is down
- Shard is not properly replicated across nodes
- Shard range assignment is uneven
- Compaction fails on a specific shard

## Common Error Messages

```
{ "error": "not_found", "reason": "missing" }
```

```
{ "error": "internal_server_error", "reason": "shard_not_available" }
```

```
{ "error": "io_error", "reason": "corrupt shard file" }
```

```
{ "error": "conflict", "reason": "shard range conflict" }
```

## How to Fix It

### 1. Check Shard Status

```bash
# List all shards for a database
curl http://localhost:5984/mydb | jq '.shard_info'

# Check which nodes own which shards
curl http://localhost:5984/_shards/mydb | jq '.shards'

# Example output showing shard ranges
# {
#   "shards": {
#     "00000000-1fffffff": ["node1", "node2", "node3"],
#     "20000000-3fffffff": ["node1", "node2", "node3"],
#     ...
#   }
# }
```

### 2. Repair Corrupted Shard

```bash
# Stop CouchDB
sudo systemctl stop couchdb

# Check shard files integrity
ls -la /opt/couchdb/data/shards*/

# Restore corrupted shard from backup
cp /backup/shards/00000000-1fffffff.mydb.couch \
   /opt/couchdb/data/shards/00000000-1fffffff.mydb.couch

# Fix file permissions
sudo chown couchdb:couchdb /opt/couchdb/data/shards/00000000-1fffffff.mydb.couch

# Restart CouchDB
sudo systemctl start couchdb
```

### 3. Move Shard to Different Node

```bash
# Move a shard from one node to another
curl -X POST http://localhost:5984/_move_shard \
  -H "Content-Type: application/json" \
  -d '{
    "db_name": "mydb",
    "shard": "00000000-1fffffff",
    "from": "couchdb@node1",
    "to": "couchdb@node4"
  }'

# Check active tasks for shard operations
curl http://localhost:5984/_active_tasks
```

### 4. Fix Shard Distribution

```bash
# Check shard range distribution
curl http://localhost:5984/_shards/mydb | jq '.shards | to_entries[] | {range: .key, nodes: (.value | length)}'

# Ensure each shard has correct number of replicas
# With n=3, each shard should be on 3 nodes

# Rebalance by adding/removing nodes
curl -X PUT http://localhost:5984/_nodes/couchdb@node4.example.com \
  -H "Content-Type: application/json" \
  -d '{}'
```

## Common Scenarios

- **Shard corruption after disk failure**: Restore from backup and trigger replication to rebuild replicas.
- **Uneven shard distribution**: Add more nodes and let the balancer redistribute.
- **Shard not found on any node**: Restore the specific shard file from backup.

## Prevent It

- Monitor shard distribution across nodes regularly
- Use RAID for disk redundancy on each node
- Keep backups of shard files, not just logical backups

## Related Pages

- [CouchDB Cluster Error](/tools/couchdb/couchdb-cluster-error)
- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
- [CouchDB Disk Error](/tools/couchdb/couchdb-disk-error)
