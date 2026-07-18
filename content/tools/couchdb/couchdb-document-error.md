---
title: "[Solution] CouchDB Document Error — How to Fix"
description: "Fix CouchDB document errors including missing rev conflicts, invalid JSON payloads, and document size limit violations"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Document Error

CouchDB document errors occur when creating, reading, updating, or deleting documents fails. CouchDB requires correct revisions and valid JSON for all document operations.

## Why It Happens

- Missing or incorrect `_rev` field during updates
- Document body is not valid JSON
- Document exceeds the maximum size limit
- Document ID contains invalid characters
- Attempting to delete a document without the current revision
- Attachment content-type mismatch

## Common Error Messages

```
{ "error": "conflict", "reason": "Document update conflict." }
```

```
{ "error": "bad_request", "reason": "invalid JSON" }
```

```
{ "error": "bad_request", "reason": "Document too large" }
```

```
{ "error": "not_found", "reason": "missing" }
```

## How to Fix It

### 1. Always Include _rev on Updates

```bash
# First, get the current revision
curl http://localhost:5984/mydb/doc123
# Returns: { "_id": "doc123", "_rev": "2-abc123", ... }

# Update with correct _rev
curl -X PUT http://localhost:5984/mydb/doc123 \
  -H "Content-Type: application/json" \
  -d '{"_rev": "2-abc123", "name": "Updated Name", "value": 42}'
```

### 2. Validate JSON Before Writing

```bash
# Validate JSON with jq
echo '{"name": "test", "value": 42}' | jq .

# Fix common issues: trailing commas, unquoted keys
# BAD:  { name: "test", }
# GOOD: { "name": "test" }
```

```python
# Python validation
import json
try:
    doc = json.loads(payload)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

### 3. Handle Large Documents

```bash
# Check document size
curl http://localhost:5984/mydb/doc123 | wc -c

# Default max_document_size is 500MB in local.ini
# Increase if needed:
```

```ini
; In local.ini
[couchdb]
max_document_size = 1000000000  ; 1GB in bytes
```

### 4. Use Batch API for Bulk Operations

```bash
# Bulk save to reduce per-document overhead
curl -X POST http://localhost:5984/mydb/_bulk_docs \
  -H "Content-Type: application/json" \
  -d '{
    "docs": [
      {"_id": "doc1", "name": "First"},
      {"_id": "doc2", "name": "Second"}
    ]
  }'
```

## Common Scenarios

- **Replication conflict on document**: Delete conflicting revisions or use `_purge` to clean up history.
- **Bulk insert fails partially**: Check `_bulk_docs` response for individual document errors.
- **Binary attachment rejected**: Ensure `content_type` matches the actual attachment data.

## Prevent It

- Always fetch the latest `_rev` before updating documents
- Use application-level JSON validation before sending to CouchDB
- Implement retry logic with exponential backoff for conflict errors

## Related Pages

- [CouchDB Conflict Error](/tools/couchdb/couchdb-conflict-error)
- [CouchDB Bulk Error](/tools/couchdb/couchdb-bulk-error)
- [CouchDB Attachment Error](/tools/couchdb/couchdb-attachment-error)
