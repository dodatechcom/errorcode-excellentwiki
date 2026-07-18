---
title: "[Solution] CouchDB Mango Query Error — How to Fix"
description: "Fix CouchDB Mango errors by correcting selector syntax, creating proper indexes, and resolving no_usable_index failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Mango Query Error

CouchDB Mango query errors occur when using the `_find` API with incorrect selector syntax, missing indexes, or unsupported operators. Mango provides a MongoDB-like query interface.

## Why It Happens

- Selector references fields without an appropriate index
- Operator syntax is incorrect (e.g., `$gt` instead of `$gt`)
- Mango index definition conflicts with existing indexes
- Query returns more results than allowed
- Selector uses unsupported operators
- Database does not have any Mango indexes

## Common Error Messages

```
{ "error": "no_usable_index", "reason": "no matching index found" }
```

```
{ "error": "bad_request", "reason": "invalid selector" }
```

```
{ "error": "bad_request", "reason": "too_many_results" }
```

```
{ "error": "not_found", "reason": "missing" }
```

## How to Fix It

### 1. Create Proper Mango Index

```bash
# Create a single-field index
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {"fields": ["type"]},
    "name": "type-index",
    "type": "json"
  }'

# Create a compound index
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {"fields": ["type", "status", "created_at"]},
    "name": "type-status-date",
    "type": "json"
  }'

# Create a text index
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {"fields": ["name"]},
    "name": "name-text",
    "type": "text",
    "analyzer": "english"
  }'
```

### 2. Write Correct Selector Queries

```bash
# Simple equality
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{"selector": {"type": "user"}}'

# Comparison operators
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {
      "age": {"$gte": 18, "$lte": 65},
      "status": "active"
    }
  }'

# Multiple conditions
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {
      "$and": [
        {"type": "order"},
        {"amount": {"$gt": 100}},
        {"status": {"$in": ["pending", "processing"]}}
      ]
    }
  }'
```

### 3. Fix Selector Syntax

```javascript
// Correct Mango operators
const validSelectors = {
  // Equality
  equality: { type: "user" },

  // Comparison
  comparison: { age: { "$gt": 18, "$lt": 65 } },

  // Logical
  logical: { "$and": [{ type: "user" }, { active: true }] },

  // Array
  array: { tags: { "$elemMatch": { "$eq": "important" } } },

  // Existence
  existence: { email: { "$exists": true } },

  // Regex
  regex: { name: { "$regex": "^admin", "$options": "i" } }
};
```

### 4. Use Index Hints

```bash
# Force index usage
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {"type": "user", "status": "active"},
    "use_index": "_design/type-status"
  }'

# List available indexes
curl http://localhost:5984/mydb/_index | jq '.indexes[] | {name, def}'
```

## Common Scenarios

- **Full scan warning**: Create an index for frequently queried fields.
- **Sort fails without index**: The sort field must be included in the index.
- **Large result set OOM**: Use `limit` and pagination with `bookmark`.

## Prevent It

- Create compound indexes for multi-field queries
- Use `explain` to verify index usage: `curl -X POST db/_explain -d '{...}'`
- Monitor slow queries with `bookmark` and pagination

## Related Pages

- [CouchDB Find Error](/tools/couchdb/couchdb-find-error)
- [CouchDB Index Error](/tools/couchdb/couchdb-index-error)
- [CouchDB Query Error](/tools/couchdb/couchdb-query-error)
