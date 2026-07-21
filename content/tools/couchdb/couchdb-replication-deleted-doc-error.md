---
title: "[Solution] CouchDB Replication Deleted Doc Error — How to Fix"
description: "Fix CouchDB replication deleted doc errors by resolving deleted document replication issues, fixing tombstone handling problems, and handling document deletion sync"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
comments: true
---

# CouchDB Replication Deleted Doc Error

CouchDB replication deleted doc errors occur when deleted documents fail to replicate correctly, causing data inconsistency between source and target.

## Why It Happens

- Deleted document tombstones are not replicated
- Target has document that was deleted on source
- Replication filter excludes deleted documents
- Tombstone purge is too aggressive
- Deleted document revision is missing
- Replication did not process deletion

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Deleted document not replicated" }
```

```
{ "error": "not_found", "reason": "Document deleted but still exists" }
```

```
{ "error": "internal_server_error", "reason": "Tombstone not found" }
```

```
{ "error": "internal_server_error", "reason": "Deletion sync failed" }
```

## How to Fix It

### 1. Check Deleted Documents

```bash
# Check for deleted documents
curl "http://localhost:5984/mydb/_changes?include_docs=true&seqs=true" | jq '.rows[] | select(.doc._deleted)'

# Check if document exists on target
curl http://localhost:5984/target_db/doc123
```

### 2. Fix Deleted Document Replication

```bash
# Replicate deleted documents
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "filter": "_doc_ids",
    "doc_ids": ["doc123"]
  }'
```

### 3. Delete on Target Manually

```bash
# Get current revision on target
curl http://localhost:5984/target_db/doc123 | jq '._rev'

# Delete document on target
curl -X DELETE "http://localhost:5984/target_db/doc123?rev=1-abc"
```

### 4. Monitor Deletion Sync

```bash
# Check changes for deletions
curl "http://localhost:5984/mydb/_changes?include_docs=true" | jq '.rows[] | select(.deleted == true)'

# Compare source and target
curl "http://localhost:5984/source_db/_all_docs" | jq '.total_rows' > source.txt
curl "http://localhost:5984/target_db/_all_docs" | jq '.total_rows' > target.txt
```

## Common Scenarios

- **Deleted doc on target**: Delete manually or reset replication.
- **Tombstone not replicated**: Check replication filter settings.
- **Deletion not synced**: Verify changes feed includes deletions.

## Prevent It

- Monitor deleted document replication
- Ensure replication includes deletions
- Avoid aggressive tombstone purging

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Replication Filter Error](/tools/couchdb/couchdb-replication-filter-error)
