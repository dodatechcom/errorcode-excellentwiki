---
title: "[Solution] CouchDB Replication Design Doc Error — How to Fix"
description: "Fix CouchDB replication design doc errors by resolving design document replication failures, fixing design doc sync issues, and handling design doc conflicts"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Design Doc Error

CouchDB replication design doc errors occur when design documents fail to replicate between databases, causing views and functions to be missing on the target.

## Why It Happens

- Design document is too large
- Design document contains invalid JavaScript
- Design document conflicts during replication
- Target database rejects design document
- Design document references non-existent fields
- Design document validation fails

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Design doc replication failed" }
```

```
{ "error": "conflict", "reason": "Design document conflict" }
```

```
{ "error": "bad_request", "reason": "Invalid design document" }
```

```
{ "error": "internal_server_error", "reason": "Design doc too large" }
```

## How to Fix It

### 1. Check Design Documents

```bash
# List design documents
curl "http://localhost:5984/mydb/_all_docs?startkey=\"_design/\"&endkey=\"_design/\ufff0\"&include_docs=true"

# Get specific design document
curl http://localhost:5984/mydb/_design/app | jq '._id, .views, .shows, .filters'
```

### 2. Fix Design Document Conflicts

```bash
# Check for conflicts
curl "http://localhost:5984/mydb/_design/app?conflicts=true"

# Resolve conflict
curl -X DELETE "http://localhost:5984/mydb/_design/app?rev=2-abc"

# Recreate design document
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "views": {
      "by_type": {
        "map": "function(doc) { emit(doc.type, 1); }",
        "reduce": "_count"
      }
    }
  }'
```

### 3. Fix Invalid Design Document

```bash
# Validate design document
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "views": {
      "valid_view": {
        "map": "function(doc) { if (doc.type) { emit(doc.type, 1); } }",
        "reduce": "_count"
      }
    }
  }'
```

### 4. Replicate Design Documents

```bash
# Create replication with design doc support
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "doc_ids": ["_design/app", "_design/stats"]
  }'
```

## Common Scenarios

- **Design doc conflict**: Resolve conflicts before replication.
- **Invalid design doc**: Fix JavaScript syntax and logic.
- **Design doc too large**: Split into smaller design documents.

## Prevent It

- Test design documents before replication
- Resolve conflicts proactively
- Use version control for design documents

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Design Doc Error](/tools/couchdb/couchdb-design-doc-error)
- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
