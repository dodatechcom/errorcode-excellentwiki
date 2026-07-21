---
title: "[Solution] CouchDB Replication State Error — How to Fix"
description: "Fix CouchDB replication state errors by resolving stuck replication states, fixing state transitions, and handling replication lifecycle issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication State Error

CouchDB replication state errors occur when replication tasks get stuck in an invalid state or fail to transition between states correctly.

## Why It Happens

- Replication task is stuck in "running" state
- State file is corrupted
- Replication crashed without cleaning up state
- State transition logic has a bug
- Network partition caused inconsistent state
- Replicator database is corrupted

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Replication stuck in state: running" }
```

```
{ "error": "internal_server_error", "reason": "Invalid replication state" }
```

```
{ "error": "internal_server_error", "reason": "Replication state file corrupted" }
```

```
{ "error": "not_found", "reason": "Replication document not found" }
```

## How to Fix It

### 1. Check Replication State

```bash
# Check replication document
curl http://localhost:5984/_replicator/replication_doc_id

# Check replication session
curl http://localhost:5984/_replicator/_changes

# Check active tasks
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication")'
```

### 2. Fix Stuck State

```bash
# Cancel stuck replication
curl -X DELETE http://localhost:5984/_replicator/replication_doc_id?rev=1-abc

# Restart replication
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "continuous": true
  }'
```

### 3. Clean Up Replicator Database

```bash
# Check replicator database
curl http://localhost:5984/_replicator

# Delete corrupted replication documents
curl -X DELETE http://localhost:5984/_replicator/bad_doc?rev=1-xyz

# Compact replicator database
curl -X POST http://localhost:5984/_replicator/_compact
```

### 4. Monitor Replication State

```bash
# Check replication state transitions
curl http://localhost:5984/_replicator/_changes?include_docs=true | jq '.rows[] | {id: .id, state: .doc._replication_state}'

# Watch for state changes
curl http://localhost:5984/_replicator/_changes?feed=continuous
```

## Common Scenarios

- **Replication stuck**: Cancel and restart the replication task.
- **State file corrupted**: Delete the replication document and recreate it.
- **Replication not starting**: Check source and target accessibility.

## Prevent It

- Monitor replication state regularly
- Use continuous replication with retry settings
- Keep replicator database clean

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Replication Conflict Error](/tools/couchdb/couchdb-replication-conflict-error)
- [CouchDB Replicator Error](/tools/couchdb/couchdb-replicator-error)
