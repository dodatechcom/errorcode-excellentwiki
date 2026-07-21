---
title: "[Solution] CouchDB Mango Error — How to Fix"
description: "Fix CouchDB Mango errors by resolving Mango query failures, fixing selector syntax issues, and handling Mango index problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Mango Error

CouchDB Mango errors occur when Mango (JSON Query Language) queries fail due to invalid selector syntax, missing indexes, or query execution issues.

## Why It Happens

- Selector syntax is invalid
- Query references fields without an index
- Query is too complex for available indexes
- Mango query server is not responding
- Query exceeds execution time limit
- Sort fields are not indexed

## Common Error Messages

```
{ "error": "bad_request", "reason": "Invalid selector" }
```

```
{ "error": "internal_server_error", "reason": "No index found" }
```

```
{ "error": "not_found", "reason": "Mango query server not found" }
```

```
{ "error": "bad_request", "reason": "Sort cannot be used with range queries on different index fields" }
```

## How to Fix It

### 1. Fix Selector Syntax

```bash
# Invalid selector - missing operator
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{"selector": {"name": "John"}}'

# Valid selector
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{"selector": {"name": {"$eq": "John"}}}'
```

### 2. Create Appropriate Index

```bash
# Create index for your query
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {
      "fields": ["name", "age"]
    },
    "name": "by-name-age",
    "type": "json"
  }'

# Query using the index
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {"name": {"$eq": "John"}, "age": {"$gt": 25}},
    "sort": [{"name": "asc"}],
    "use_index": "by-name-age"
  }'
```

### 3. Fix Complex Queries

```bash
# Use $and for multiple conditions on different fields
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {
      "$and": [
        {"type": {"$eq": "event"}},
        {"timestamp": {"$gte": "2024-01-01"}}
      ]
    }
  }'

# Use $or with indexed fields
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {
      "$or": [
        {"status": {"$eq": "active"}},
        {"status": {"$eq": "pending"}}
      ]
    }
  }'
```

### 4. Debug Mango Query

```bash
# Explain query plan
curl -X POST http://localhost:5984/mydb/_explain \
  -H "Content-Type: application/json" \
  -d '{"selector": {"type": "event"}, "sort": [{"timestamp": "asc"}]}'

# Check available indexes
curl http://localhost:5984/mydb/_index
```

## Common Scenarios

- **No index found**: Create an index for the fields used in your selector.
- **Invalid selector**: Check Mango selector syntax documentation.
- **Slow query**: Create a composite index matching your query pattern.

## Prevent It

- Create indexes for frequently queried fields
- Use `_explain` to verify query plans
- Keep selectors simple when possible

## Related Pages

- [CouchDB Index Error](/tools/couchdb/couchdb-index-error)
- [CouchDB Query Error](/tools/couchdb/couchdb-query-error)
- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
