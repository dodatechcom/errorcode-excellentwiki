---
title: "[Solution] CouchDB Replication OK Error — How to Fix"
description: "Fix CouchDB replication OK errors by resolving false positive replication status, fixing replication completion detection, and handling replication success verification"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
comments: true
---

# CouchDB Replication OK Error

CouchDB replication OK errors occur when replication reports success but data is actually inconsistent or incomplete.

## Why It Happens

- Replication completed but documents were skipped
- Replication reported OK but target is inconsistent
- Checkpoint saved before all documents processed
- Filter skipped documents without reporting
- Replication completed with warnings
- Partial replication reported as success

## Common Error Messages

```
{ "_replication_stats": {"docs_written": 100, "doc_write_failures": 5} }
```

```
{ "ok": true, "warning": "Some documents were skipped" }
```

```
{ "_replication_state": "completed", "docs_read": 100, "docs_written": 95 }
```

```
{ "ok": true, "docs_written": 100, "doc_write_failures": 10 }
```

## How to Fix It

### 1. Check Replication Stats

```bash
# Check replication document stats
curl http://localhost:5984/_replicator/my_rep | jq '._replication_stats'

# Check active tasks
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {docs_written, doc_write_failures}'
```

### 2. Fix Document Failures

```bash
# Check for failed documents
curl "http://localhost:5984/source_db/_changes?include_docs=true" | \
  jq '.rows[] | select(.doc._conflicts != null)'

# Resolve conflicts on source
curl -X DELETE "http://localhost:5984/source_db/doc123?rev=2-abc"
```

### 3. Verify Replication

```bash
# Compare document counts
curl http://localhost:5984/source_db | jq '.doc_count'
curl http://localhost:5984/target_db | jq '.doc_count'

# Check for missing documents
curl "http://localhost:5984/source_db/_all_docs?limit=100" | jq '.rows[].id' > source_ids.txt
curl "http://localhost:5984/target_db/_all_docs?limit=100" | jq '.rows[].id' > target_ids.txt
comm -23 source_ids.txt target_ids.txt
```

### 4. Resync Data

```bash
# Reset replication to catch all documents
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "since": "0"
  }'
```

## Common Scenarios

- **Doc write failures**: Check for conflicts and permissions on target.
- **Documents skipped**: Reset replication since=0 to reprocess.
- **Partial success**: Verify and resync missing documents.

## Prevent It

- Monitor replication statistics
- Verify data after replication
- Handle document conflicts before replication

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Replication Inconsistent Error](/tools/couchdb/couchdb-replication-inconsistent-error)
