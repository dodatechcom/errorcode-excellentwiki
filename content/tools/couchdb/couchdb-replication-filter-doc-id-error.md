---
title: "[Solution] CouchDB Replication Filter Doc ID Error — How to Fix"
description: "Fix CouchDB replication filter doc ID errors by resolving document ID filter issues, fixing doc_ids filter problems, and handling selective document replication"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Filter Doc ID Error

CouchDB replication filter doc ID errors occur when using `_doc_ids` filter to replicate specific documents fails.

## Why It Happens

- Document IDs do not exist on source
- Filter format is incorrect
- Document ID contains special characters
- Too many document IDs in filter
- Document is not accessible to replicator user
- Filter syntax is wrong

## Common Error Messages

```
{ "error": "bad_request", "reason": "Invalid doc_ids filter" }
```

```
{ "error": "not_found", "reason": "Document not found" }
```

```
{ "error": "forbidden", "reason": "Document not accessible" }
```

```
{ "error": "bad_request", "reason": "Invalid filter format" }
```

## How to Fix It

### 1. Test Document Access

```bash
# Check if document exists
curl -u user:pass http://source:5984/mydb/doc123

# Check document is accessible
curl -u user:pass http://source:5984/mydb/doc123 | jq '._id, ._rev'
```

### 2. Fix Doc IDs Filter

```bash
# Correct doc_ids filter format
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "filter": "_doc_ids",
    "doc_ids": ["doc1", "doc2", "doc3"]
  }'

# Single document
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "filter": "_doc_ids",
    "doc_ids": ["doc123"]
  }'
```

### 3. Use Custom Filter

```bash
# Create custom filter for complex selection
curl -X PUT http://localhost:5984/mydb/_design/filters \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/filters",
    "filters": {
      "selective": "function(doc, req) { var ids = [\"doc1\", \"doc2\", \"doc3\"]; return ids.indexOf(doc._id) !== -1; }"
    }
  }'

# Use custom filter
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "filter": "filters/selective"
  }'
```

### 4. Debug Filter

```bash
# Check filter function exists
curl http://localhost:5984/mydb/_design/filters | jq '.filters'

# Test filter locally
curl "http://localhost:5984/mydb/_design/filters/_filter/selective"
```

## Common Scenarios

- **Document not found**: Verify document exists on source.
- **Filter syntax error**: Use correct `_doc_ids` format.
- **Access denied**: Check replicator user permissions.

## Prevent It

- Verify document IDs before replication
- Use proper filter syntax
- Test filter with sample documents

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Replication Filter Error](/tools/couchdb/couchdb-replication-filter-error)
- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
