---
title: "[Solution] CouchDB Replication Document Error — How to Fix"
description: "Fix CouchDB replication document errors by resolving replication document issues, fixing document format problems, and handling replication doc conflicts"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Document Error

CouchDB replication document errors occur when replication configuration documents in the `_replicator` database are invalid, corrupted, or have conflicts.

## Why It Happens

- Replication document has invalid JSON
- Required fields are missing (source, target)
- Replication document has conflicts
- Document is corrupted
- Document references non-existent database
- Document contains invalid configuration

## Common Error Messages

```
{ "error": "bad_request", "reason": "Invalid replication document" }
```

```
{ "error": "bad_request", "reason": "Missing required field: source" }
```

```
{ "error": "conflict", "reason": "Replication document conflict" }
```

```
{ "error": "internal_server_error", "reason": "Replication document corrupted" }
```

## How to Fix It

### 1. Check Replication Documents

```bash
# List all replication documents
curl http://localhost:5984/_replicator/_all_docs?include_docs=true

# Check specific replication document
curl http://localhost:5984/_replicator/my_rep | jq .
```

### 2. Fix Invalid Document

```bash
# Valid replication document
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "continuous": true
  }'
```

### 3. Fix Document Conflicts

```bash
# Check for conflicts
curl "http://localhost:5984/_replicator/my_rep?conflicts=true"

# Delete conflicting revision
curl -X DELETE "http://localhost:5984/_replicator/my_rep?rev=2-abc"

# Recreate replication document
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db"
  }'
```

### 4. Clean Up Corrupted Documents

```bash
# Delete corrupted replication document
curl -X DELETE "http://localhost:5984/_replicator/bad_rep?rev=1-xyz"

# Recreate with correct configuration
curl -X PUT http://localhost:5984/_replicator/good_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "good_rep",
    "source": {
      "url": "http://source:5984/db",
      "auth": {
        "basic": {"username": "user", "password": "pass"}
      }
    },
    "target": "http://target:5984/db"
  }'
```

## Common Scenarios

- **Invalid document format**: Fix JSON syntax and required fields.
- **Document conflict**: Resolve conflicts and recreate document.
- **Corrupted document**: Delete and recreate the replication document.

## Prevent It

- Validate replication documents before saving
- Use proper JSON formatting
- Monitor replicator database for conflicts

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Replicator Error](/tools/couchdb/couchdb-replicator-error)
