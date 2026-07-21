---
title: "[Solution] CouchDB Replication Conflict Error — How to Fix"
description: "Fix CouchDB replication conflict errors by resolving document conflicts during replication, fixing conflict resolution strategies, and handling conflicting revisions"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
comments: true
---

# CouchDB Replication Conflict Error

CouchDB replication conflict errors occur when the same document is modified on both source and target databases during replication, creating conflicting revisions.

## Why It Happens

- Same document modified on source and target simultaneously
- No conflict resolution strategy defined
- Manual conflict resolution is required
- Replication filter allows conflicting writes
- Document is updated faster than replication can keep up

## Common Error Messages

```
{ "error": "conflict", "reason": "Document update conflict" }
```

```
{ "_conflicts": ["2-abc123", "2-def456"] }
```

```
{ "error": "conflict", "reason": "Replication conflict on document" }
```

```
WARNING: Conflicting revisions detected
```

## How to Fix It

### 1. Check for Conflicts

```bash
# Query document with conflicts
curl "http://localhost:5984/mydb/doc123?conflicts=true"

# List all conflicting revisions
curl "http://localhost:5984/mydb/doc123?conflicts=true&open_revs=all"
```

### 2. Resolve Conflicts Manually

```bash
# Get all conflicting versions
curl "http://localhost:5984/mydb/doc123?open_revs=all"

# Delete losing revision
curl -X DELETE "http://localhost:5984/mydb/doc123?rev=2-abc123"

# Or merge and save
curl -X PUT http://localhost:5984/mydb/doc123 \
  -H "Content-Type: application/json" \
  -H "If-Match: 2-abc123" \
  -d '{"_id": "doc123", "field1": "merged_value"}'
```

### 3. Use Automatic Conflict Resolution

```bash
# Create replication with conflict resolution
curl -X PUT http://localhost:5984/_replicator/auto_resolve \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "auto_resolve",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "continuous": true,
    "create_target": true
  }'

# Use conflict resolution filter
curl -X PUT http://localhost:5984/mydb/_design/resolve \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/resolve",
    "filters": {
      "conflict_resolve": "function(doc) { if (doc._conflicts) { return false; } return true; }"
    }
  }'
```

### 4. Prevent Future Conflicts

```bash
# Use _replicate with specific document IDs
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "doc_ids": ["doc123", "doc456"]
  }'

# Use replication filters
curl -X PUT http://localhost:5984/mydb/_design/filters \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/filters",
    "filters": {
      "my_filter": "function(doc, req) { return doc.type === 'important'; }"
    }
  }'
```

## Common Scenarios

- **Conflict during replication**: Resolve by choosing winning revision.
- **Conflicts keep occurring**: Use one-way replication or change application logic.
- **Automatic resolution needed**: Implement custom conflict resolution logic.

## Prevent It

- Use one-way replication when possible
- Implement application-level conflict avoidance
- Monitor replication for conflicts regularly

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Document Conflict Error](/tools/couchdb/couchdb-document-conflict-error)
- [CouchDB Replication State Error](/tools/couchdb/couchdb-replication-state-error)
