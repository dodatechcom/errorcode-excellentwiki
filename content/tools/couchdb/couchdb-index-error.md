---
title: "[Solution] CouchDB Index Error — How to Fix"
description: "Fix CouchDB index errors by resolving index creation failures, fixing Mango index issues, and handling secondary index problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Index Error

CouchDB index errors occur when creating or querying secondary (Mango) indexes due to invalid index definitions, resource constraints, or corruption.

## Why It Happens

- Index definition references non-existent fields
- Index is being built while database is under heavy write load
- Disk space is insufficient for index storage
- Index definition is invalid JSON
- Index name conflicts with existing index
- Database is corrupted

## Common Error Messages

```
{ "error": "bad_request", "reason": "Invalid index definition" }
```

```
{ "error": "conflict", "reason": "Index already exists" }
```

```
{ "error": "internal_server_error", "reason": "Index build failed" }
```

```
{ "error": "not_found", "reason": "Index not found" }
```

## How to Fix It

### 1. Create Mango Index

```bash
# Create index on a single field
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {
      "fields": ["timestamp"]
    },
    "name": "by-timestamp",
    "type": "json"
  }'

# Create compound index
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {
      "fields": ["type", "timestamp"]
    },
    "name": "by-type-and-time",
    "type": "json"
  }'
```

### 2. Query Using Index

```bash
# Query with Mango selector
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {
      "type": "event",
      "timestamp": {"$gt": "2024-01-01"}
    },
    "sort": [{"timestamp": "asc"}],
    "use_index": "by-type-and-time"
  }'

# Check which index is used
curl -X POST http://localhost:5984/mydb/_explain \
  -H "Content-Type: application/json" \
  -d '{"selector": {"type": "event"}}'
```

### 3. Fix Index Build Failure

```bash
# Check disk space
df -h /opt/couchdb/data

# Reduce write load during index build
# Wait for index to complete
curl http://localhost:5984/mydb/_index | jq '.indexes[] | {name, ready}'
```

### 4. Remove and Recreate Index

```bash
# List all indexes
curl http://localhost:5984/mydb/_index

# Delete design document containing index
curl -X DELETE http://localhost:5984/mydb/_design/myindex?rev=1-abc

# Recreate index
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{"index": {"fields": ["name"]}, "name": "by-name", "type": "json"}'
```

## Common Scenarios

- **Index build fails**: Check disk space and reduce write load.
- **Invalid index definition**: Ensure all fields exist in your documents.
- **Index conflict**: Use a different index name.

## Prevent It

- Create indexes before heavy query workloads
- Monitor disk space for index storage
- Use `explain` to verify index usage

## Related Pages

- [CouchDB Query Error](/tools/couchdb/couchdb-query-error)
- [CouchDB Mango Error](/tools/couchdb/couchdb-mango-error)
- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
