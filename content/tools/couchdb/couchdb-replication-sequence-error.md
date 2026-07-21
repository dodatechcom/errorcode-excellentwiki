---
title: "[Solution] CouchDB Replication Sequence Error — How to Fix"
description: "Fix CouchDB replication sequence errors by resolving sequence number issues, fixing sequence tracking problems, and handling sequence-based replication failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Sequence Error

CouchDB replication sequence errors occur when the replicator fails to track or use sequence numbers correctly during replication.

## Why It Happens

- Sequence number is invalid or corrupted
- Sequence number is too old and purged
- Sequence tracking is out of sync
- Changes feed returns invalid sequence
- Sequence number format changed between versions
- Sequence database is corrupted

## Common Error Messages

```
{ "error": "bad_request", "reason": "Invalid sequence number" }
```

```
{ "error": "not_found", "reason": "Sequence not found" }
```

```
{ "error": "internal_server_error", "reason": "Sequence tracking failed" }
```

```
{ "error": "bad_request", "reason": "Sequence number too old" }
```

## How to Fix It

### 1. Check Sequence Numbers

```bash
# Get current sequence
curl "http://localhost:5984/mydb/_changes?limit=1" | jq '.last_seq'

# Check replication checkpoint sequence
curl http://localhost:5984/_replicator/my_rep | jq '._replication_id, ._replication_state_time'
```

### 2. Reset Sequence

```bash
# Reset replication to start from beginning
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "since": "0"
  }'

# Start from specific sequence
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "since": "5-g1AAAABXeJzLYWBgYMpgSmJwSxKMWwE1IGRgFOeKkU5JTc7PS8nMS8"
  }'
```

### 3. Fix Sequence Database

```bash
# Check sequence database
curl http://localhost:5984/_local/replication_checkpoint

# Delete corrupted checkpoint
curl -X DELETE "http://localhost:5984/_local/replication_checkpoint?rev=1-abc"

# Restart replication
curl -X DELETE http://localhost:5984/_replicator/my_rep?rev=2-def
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db"
  }'
```

### 4. Monitor Sequence Tracking

```bash
# Watch sequence changes
curl "http://localhost:5984/mydb/_changes?feed=continuous&heartbeat=10000"

# Check replication sequence progress
curl http://localhost:5984/_replicator/my_rep | jq '._replication_stats'
```

## Common Scenarios

- **Invalid sequence**: Reset replication to start from beginning.
- **Sequence too old**: Use since=0 to re-replicate from start.
- **Sequence corrupted**: Delete checkpoint and restart replication.

## Prevent It

- Monitor sequence numbers regularly
- Avoid deleting old revisions too aggressively
- Use proper sequence tracking in custom replications

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Changes Feed Error](/tools/couchdb/couchdb-changes-feed-error)
- [CouchDB Replication State Error](/tools/couchdb/couchdb-replication-state-error)
