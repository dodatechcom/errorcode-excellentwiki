---
title: "[Solution] CouchDB Replication Shallow Error — How to Fix"
description: "Fix CouchDB replication shallow errors by resolving shallow replication issues, fixing lightweight replication problems, and handling shallow copy replication failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
comments: true
---

# CouchDB Replication Shallow Error

CouchDB replication shallow errors occur when shallow (lightweight) replication fails to copy documents correctly.

## Why It Happens

- Shallow replication is not supported in CouchDB version
- Shallow copy requires specific configuration
- Target database does not support shallow copies
- Document metadata is incomplete for shallow copy
- Shallow replication is too fast for target to handle
- Revision history is not preserved in shallow copy

## Common Error Messages

```
{ "error": "bad_request", "reason": "Shallow replication not supported" }
```

```
{ "error": "internal_server_error", "reason": "Shallow copy failed" }
```

```
{ "error": "internal_server_error", "reason": "Incomplete metadata for shallow copy" }
```

```
{ "error": "not_found", "reason": "Shallow replication not available" }
```

## How to Fix It

### 1. Check CouchDB Version

```bash
# Check CouchDB version
curl http://localhost:5984/ | jq '.version'

# Shallow replication requires CouchDB 3.x+
```

### 2. Use Standard Replication

```bash
# Use standard replication instead
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db"
  }'
```

### 3. Configure Shallow Replication

```bash
# For CouchDB 3.x, use shallow replication
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "create_target": true,
    "batch_size": 1000
  }'
```

### 4. Monitor Shallow Replication

```bash
# Check replication status
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication")'

# Check document count
curl http://localhost:5984/source_db | jq '.doc_count'
curl http://localhost:5984/target_db | jq '.doc_count'
```

## Common Scenarios

- **Shallow not supported**: Use standard replication for older versions.
- **Metadata incomplete**: Ensure all documents have proper metadata.
- **Target overload**: Reduce batch size for shallow replication.

## Prevent It

- Check CouchDB version before using shallow replication
- Monitor replication performance
- Use appropriate batch sizes

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Version Error](/tools/couchdb/couchdb-version-error)
- [CouchDB Configuration Error](/tools/couchdb/couchdb-config-error)
