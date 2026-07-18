---
title: "[Solution] CouchDB Conflict Error — How to Fix"
description: "Fix CouchDB document conflicts by merging revisions, using conflict resolution strategies, and cleaning up lost branches"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Conflict Error

CouchDB conflict errors occur when concurrent updates create multiple revisions of the same document. CouchDB uses MVCC and requires explicit conflict resolution.

## Why It Happens

- Two clients update the same document simultaneously
- Replication creates conflicting revisions between databases
- Application does not include the current `_rev` on updates
- Bulk operations create conflicting writes
- Delete conflicts are not resolved

## Common Error Messages

```
{ "error": "conflict", "reason": "Document update conflict." }
```

```
{ "error": "conflict", "reason": "Document update conflict. (409)" }
```

```
{ "error": "conflict", "reason": "missing" }
```

```
{ "_id": "doc123", "_rev": "3-abc", "_conflicts": ["2-def", "2-ghi"] }
```

## How to Fix It

### 1. Detect and List Conflicts

```bash
# Query with conflicts parameter
curl 'http://localhost:5984/mydb/doc123?conflicts=true'

# Response shows conflicting revisions
{
  "_id": "doc123",
  "_rev": "3-abc123",
  "name": "Current Value",
  "_conflicts": ["2-def456", "2-ghi789"]
}

# Find all documents with conflicts
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {"_conflicts": {"$gt": null}}
  }'
```

### 2. Resolve Conflicts by Deleting Non-Winning Revisions

```bash
# Get the losing revision
curl 'http://localhost:5984/mydb/doc123?rev=2-def456'

# Delete the losing revision
curl -X DELETE "http://localhost:5984/mydb/doc123?rev=2-def456"

# Repeat for other conflicting revisions
curl -X DELETE "http://localhost:5984/mydb/doc123?rev=2-ghi789"

# Verify conflicts are resolved
curl 'http://localhost:5984/mydb/doc123?conflicts=true&deleted_conflicts=true'
```

### 3. Merge Conflicting Revisions

```bash
# Get both conflicting revisions
curl 'http://localhost:5984/mydb/doc123?rev=2-def456'
# Returns: {"_id": "doc123", "_rev": "2-def456", "field_a": "value1"}

curl 'http://localhost:5984/mydb/doc123?rev=3-abc123'
# Returns: {"_id": "doc123", "_rev": "3-abc123", "field_b": "value2"}

# Merge and update winning revision
curl -X PUT http://localhost:5984/mydb/doc123 \
  -H "Content-Type: application/json" \
  -d '{"_rev": "3-abc123", "field_a": "value1", "field_b": "value2"}'

# Then delete losing revisions
curl -X DELETE "http://localhost:5984/mydb/doc123?rev=2-def456"
```

### 4. Prevent Conflicts with Application Logic

```javascript
// Use retry with exponential backoff
async function updateDoc(db, docId, updates) {
  for (let attempt = 0; attempt < 5; attempt++) {
    try {
      const doc = await db.get(docId);
      const updated = { ...doc, ...updates };
      return await db.put(updated);
    } catch (err) {
      if (err.status === 409) {
        await sleep(Math.pow(2, attempt) * 100);
        continue;
      }
      throw err;
    }
  }
  throw new Error('Max retries exceeded');
}
```

## Common Scenarios

- **Replication conflict after offline edits**: Merge changes or use `conflicts=true` in replication filters.
- **Bulk insert with overlapping IDs**: Use `_bulk_docs` with explicit `_rev` for each document.
- **Delete conflict after replication**: Delete all non-winning revisions first, then the winning one.

## Prevent It

- Always fetch `_rev` before updating documents
- Implement application-level conflict resolution (last-write-wins or merge)
- Use `_bulk_docs` with correct revisions for batch operations

## Related Pages

- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Bulk Error](/tools/couchdb/couchdb-bulk-error)
