---
title: "[Solution] CouchDB Replication Document Conflict Error — How to Fix"
description: "Fix CouchDB replication document conflict errors by resolving conflicts in replication documents, fixing document version issues, and handling replicator database conflicts"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Document Conflict Error

CouchDB replication document conflict errors occur when replication documents in the `_replicator` database have conflicting revisions, preventing replication from starting or continuing.

## Why It Happens

- Replication document was updated simultaneously from multiple sources
- Replicator database is shared between multiple admin users
- Document was edited while replication was running
- Replicator crashed during document update
- Document conflict was not resolved

## Common Error Messages

```
{ "error": "conflict", "reason": "Document update conflict" }
```

```
{ "error": "conflict", "reason": "Replication document conflict" }
```

```
{ "error": "conflict", "reason": "Conflict on _replicator document" }
```

```
{ "error": "conflict", "reason": "Cannot update replication document" }
```

## How to Fix It

### 1. Check for Conflicts

```bash
# List replication documents with conflicts
curl "http://localhost:5984/_replicator/_all_docs?include_docs=true&conflicts=true"

# Check specific document
curl "http://localhost:5984/_replicator/my_rep?conflicts=true"
```

### 2. Resolve Conflicts

```bash
# Get all conflicting revisions
curl "http://localhost:5984/_replicator/my_rep?open_revs=all"

# Delete losing revision
curl -X DELETE "http://localhost:5984/_replicator/my_rep?rev=2-abc"

# Save winning revision with merged data
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -H "If-Match: 2-def" \
  -d '{
    "_id": "my_rep",
    "_rev": "2-def",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "continuous": true
  }'
```

### 3. Delete and Recreate

```bash
# Delete all conflicting versions
curl -X DELETE "http://localhost:5984/_replicator/my_rep?rev=2-abc"
curl -X DELETE "http://localhost:5984/_replicator/my_rep?rev=2-def"

# Recreate replication document
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "continuous": true
  }'
```

### 4. Prevent Future Conflicts

```bash
# Use unique document IDs
curl -X PUT http://localhost:5984/_replicator/source-target-rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "source-target-rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db"
  }'

# Use exclusive locks during updates
curl -X PUT http://localhost:5984/_replicator/my_rep?new_edits=false \
  -H "Content-Type: application/json" \
  -d '[{"_id": "my_rep", "_rev": "2-abc", "source": "http://source:5984/db", "target": "http://target:5984/db"}]'
```

## Common Scenarios

- **Conflict when updating**: Resolve existing conflict before updating.
- **Multiple admins editing**: Use unique document IDs and coordination.
- **Replicator crash**: Delete corrupted document and recreate.

## Prevent It

- Use unique, descriptive document IDs
- Coordinate replication document changes
- Monitor replicator database for conflicts

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Document Conflict Error](/tools/couchdb/couchdb-document-conflict-error)
- [CouchDB Replicator Error](/tools/couchdb/couchdb-replicator-error)
