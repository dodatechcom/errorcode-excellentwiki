---
title: "[Solution] CouchDB Index Error — How to Fix"
description: "Fix CouchDB index errors by rebuilding mango indexes, correcting index definitions, and resolving index fragmentation issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Index Error

CouchDB index errors occur when creating or querying Mango indexes or custom views that serve as indexes. Index corruption or incorrect definitions can cause query failures.

## Why It Happens

- Mango index definition references fields not present in documents
- Index building fails due to insufficient disk space or memory
- Index file corruption after unclean shutdown
- Duplicate index definitions with conflicting options
- Index exceeds the maximum number of fields
- Using unsupported operators in index selector

## Common Error Messages

```
{ "error": "bad_request", "reason": "invalid_url" }
```

```
{ "error": "error", "reason": "no_usable_index" }
```

```
{ "error": "not_found", "reason": "missing" }
```

```
{ "error": "invalid_index_def", "reason": "too_many_index_fields" }
```

## How to Fix It

### 1. Create Correct Mango Index

```bash
# Create a single-field index
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {
      "fields": ["email"]
    },
    "name": "email-index",
    "type": "json"
  }'

# Create a compound index
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {
      "fields": ["type", "created_at"]
    },
    "name": "type-date-index",
    "type": "json"
  }'
```

### 2. Verify Index Exists and Use It

```bash
# List all indexes
curl http://localhost:5984/mydb/_index

# Query with index hint
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {
      "email": "user@example.com"
    },
    "use_index": "_design/email-index"
  }'
```

### 3. Rebuild Broken Index

```bash
# Delete and recreate the index
curl -X DELETE http://localhost:5984/mydb/_index/design-doc/index-name

# Rebuild by recreating
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {"fields": ["email"]},
    "name": "email-index",
    "type": "json"
  }'

# Force index build by running a query
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{"selector": {"email": {"$gt": null}}}'
```

### 4. Fix Index Definition Issues

```bash
# Check index metadata
curl http://localhost:5984/mydb/_design/app

# Compact the database to clean up index files
curl -X POST http://localhost:5984/mydb/_compact

# Force full compaction including views
curl -X POST http://localhost:5984/mydb/_view_compact \
  -H "Content-Type: application/json" \
  -d '{"stale": false}'
```

## Common Scenarios

- **Mango query falls back to full scan**: Create an appropriate index for the selector fields.
- **Index build fails with OOM**: Reduce batch size or increase available memory.
- **Stale index returns old data**: Use `stale=false` in queries to ensure up-to-date results.

## Prevent It

- Always specify `use_index` in `_find` queries to force index usage
- Monitor index size with `_index` endpoint
- Clean up unused indexes to reduce storage overhead

## Related Pages

- [CouchDB Mango Error](/tools/couchdb/couchdb-mango-error)
- [CouchDB Find Error](/tools/couchdb/couchdb-find-error)
- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
