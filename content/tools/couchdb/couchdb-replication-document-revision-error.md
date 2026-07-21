---
title: "[Solution] CouchDB Replication Document Revision Error — How to Fix"
description: "Fix CouchDB replication document revision errors by resolving revision conflicts, fixing revision handling issues, and managing revision history during replication"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Document Revision Error

CouchDB replication document revision errors occur when document revisions conflict or are handled incorrectly during replication.

## Why It Happens

- Document was modified on both source and target
- Revision history is too long
- Document revision is missing
- Revision does not match expected value
- Document was deleted but revision still referenced
- Concurrent updates caused revision conflicts

## Common Error Messages

```
{ "error": "conflict", "reason": "Document update conflict" }
```

```
{ "error": "conflict", "reason": "Revision conflict" }
```

```
{ "error": "bad_request", "reason": "Invalid revision" }
```

```
{ "error": "not_found", "reason": "Revision not found" }
```

## How to Fix It

### 1. Check Document Revisions

```bash
# Get document with revision
curl http://localhost:5984/mydb/doc123 | jq '._rev'

# Get all revisions
curl "http://localhost:5984/mydb/doc123?open_revs=all"

# Check for conflicts
curl "http://localhost:5984/mydb/doc123?conflicts=true"
```

### 2. Fix Revision Conflict

```bash
# Delete conflicting revision
curl -X DELETE "http://localhost:5984/mydb/doc123?rev=2-abc"

# Save with correct revision
curl -X PUT http://localhost:5984/mydb/doc123 \
  -H "Content-Type: application/json" \
  -H "If-Match: 1-def" \
  -d '{"_id": "doc123", "field": "value"}'
```

### 3. Reset Revision History

```bash
# Compact document revisions
curl -X POST http://localhost:5984/mydb/_compact

# Limit revision history
curl -X PUT http://localhost:5984/mydb/_revs_limit \
  -H "Content-Type: text/plain" \
  -d '"100"'
```

### 4. Resolve Revision Issues

```bash
# Use all-or-nothing update
curl -X POST http://localhost:5984/mydb/_bulk_docs \
  -H "Content-Type: application/json" \
  -d '{
    "all_or_nothing": true,
    "docs": [
      {"_id": "doc123", "_rev": "1-abc", "field": "value"}
    ]
  }'

# Delete and recreate if needed
curl -X DELETE "http://localhost:5984/mydb/doc123?rev=1-abc"
curl -X PUT http://localhost:5984/mydb/doc123 \
  -H "Content-Type: application/json" \
  -d '{"_id": "doc123", "field": "new_value"}'
```

## Common Scenarios

- **Revision conflict**: Delete conflicting revision and retry.
- **Invalid revision**: Check current revision before update.
- **Too many revisions**: Compact document to reduce history.

## Prevent It

- Always use latest revision for updates
- Handle conflicts gracefully in application
- Monitor revision history size

## Related Pages

- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Document Conflict Error](/tools/couchdb/couchdb-document-conflict-error)
- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
