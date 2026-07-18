---
title: "[Solution] CouchDB Bulk Error — How to Fix"
description: "Fix CouchDB bulk operation errors by handling partial failures in _bulk_docs, resolving batch size limits, and fixing conflict errors"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Bulk Error

CouchDB bulk errors occur when `_bulk_docs` or `_bulk_get` operations fail partially or completely. Bulk operations are essential for batch inserts and updates.

## Why It Happens

- One document in the batch has a conflict
- Document exceeds the maximum size limit
- Batch contains too many documents
- Missing `_rev` field on update operations
- Invalid JSON in the request body
- All-or-nothing mode fails on any error

## Common Error Messages

```
{ "error": "bad_request", "reason": "invalid_json" }
```

```
{ "error": "conflict", "reason": "Document update conflict." }
```

```
{ "error": "bad_request", "reason": "too_many_ids" }
```

```
[{ "id": "doc1", "error": "conflict" }, { "id": "doc2", "ok": true }]
```

## How to Fix It

### 1. Bulk Insert Documents

```bash
curl -X POST http://localhost:5984/mydb/_bulk_docs \
  -H "Content-Type: application/json" \
  -d '{
    "docs": [
      {"_id": "user1", "name": "Alice", "type": "user"},
      {"_id": "user2", "name": "Bob", "type": "user"},
      {"_id": "user3", "name": "Charlie", "type": "admin"}
    ]
  }'

# Response shows status of each document:
# [
#   {"ok": true, "id": "user1", "rev": "1-abc"},
#   {"ok": true, "id": "user2", "rev": "1-def"},
#   {"ok": true, "id": "user3", "rev": "1-ghi"}
# ]
```

### 2. Handle Partial Failures

```bash
curl -X POST http://localhost:5984/mydb/_bulk_docs \
  -H "Content-Type: application/json" \
  -d '{
    "docs": [
      {"_id": "doc1", "_rev": "1-abc", "name": "Updated"},
      {"_id": "doc2", "_rev": "wrong-rev", "name": "Conflict"}
    ]
  }'

# Check response for errors
# [
#   {"ok": true, "id": "doc1", "rev": "2-xyz"},
#   {"id": "doc2", "error": "conflict", "reason": "Document update conflict."}
# ]

# Retry failed documents with correct revisions
```

### 3. Use All-or-Nothing Mode

```bash
# All documents must succeed or all fail
curl -X POST http://localhost:5984/mydb/_bulk_docs \
  -H "Content-Type: application/json" \
  -d '{
    "all_or_nothing": true,
    "docs": [
      {"_id": "doc1", "name": "First"},
      {"_id": "doc2", "name": "Second"}
    ]
  }'
```

### 4. Optimize Bulk Operations

```bash
# For large imports, batch into chunks
# Good batch size: 500-1000 documents

# Example: import from CSV
python3 -c "
import json, requests

docs = []
for i in range(10000):
    docs.append({'_id': f'doc_{i}', 'value': i, 'type': 'data'})
    
    if len(docs) == 500:
        resp = requests.post('http://localhost:5984/mydb/_bulk_docs',
            json={'docs': docs})
        result = resp.json()
        errors = [r for r in result if 'error' in r]
        print(f'Batch: {len(docs)} docs, errors: {len(errors)}')
        docs = []

# Final batch
if docs:
    requests.post('http://localhost:5984/mydb/_bulk_docs',
        json={'docs': docs})
"
```

## Common Scenarios

- **Insert fails with conflict**: Check if documents already exist and use correct `_rev`.
- **Large batch times out**: Reduce batch size and add delays between batches.
- **Mixed inserts and updates**: Use `all_or_nothing` if atomicity is required.

## Prevent It

- Always check the response array for individual document errors
- Use `all_or_nothing: true` when atomicity matters
- Batch large imports in chunks of 500-1000 documents

## Related Pages

- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Conflict Error](/tools/couchdb/couchdb-conflict-error)
- [CouchDB JSON Error](/tools/couchdb/couchdb-json-error)
