---
title: "[Solution] CouchDB Find Error — How to Fix"
description: "Fix CouchDB _find errors by correcting query selectors, resolving bookmark pagination issues, and fixing sort failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Find Error

CouchDB find errors occur when the `_find` API query fails due to selector issues, missing indexes, or incorrect query parameters. The `_find` endpoint provides Mango query capabilities.

## Why It Happens

- Query selector is malformed or uses invalid operators
- Sort field is not indexed
- Bookmark is invalid or expired
- Fields requested do not exist in the index
- `limit` exceeds the maximum allowed value
- `use_index` references a non-existent design document

## Common Error Messages

```
{ "error": "no_usable_index", "reason": "Query not supported by a defined index" }
```

```
{ "error": "bad_request", "reason": "invalid_json" }
```

```
{ "error": "bad_request", "reason": "sort not supported" }
```

```
{ "error": "not_found", "reason": "missing" }
```

## How to Fix It

### 1. Fix Query Selector

```bash
# Ensure query matches an index
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {
      "type": "user",
      "age": {"$gte": 18}
    },
    "sort": [{"type": "asc"}, {"age": "asc"}],
    "limit": 25,
    "use_index": "_design/type-age-index"
  }'
```

### 2. Use Bookmark Pagination

```bash
# First page
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {"type": "user"},
    "limit": 25,
    "bookmark": "nil"
  }'

# Response includes bookmark:
# {"docs": [...], "bookmark": "g1AAAAB...}

# Next page using returned bookmark
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {"type": "user"},
    "limit": 25,
    "bookmark": "g1AAAAB..."
  }'
```

### 3. Fix Sort Issues

```bash
# Sort fields must be in the index
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {"fields": ["type", "created_at"]},
    "name": "type-date-index",
    "type": "json"
  }'

# Now this sort works
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {"type": "user"},
    "sort": [{"type": "asc"}, {"created_at": "desc"}]
  }'
```

### 4. Use Explain to Debug

```bash
# Check query plan
curl -X POST http://localhost:5984/mydb/_explain \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {"type": "user", "status": "active"},
    "sort": [{"type": "asc"}]
  }'

# Response shows which index is used and if there are warnings
# {
#   "dbname": "mydb",
#   "index": {"ddoc": "_design/type-index", "name": "type-index"},
#   "selector": {...},
#   "limit": 25,
#   "skip": 0,
#   "fields": ["_id", "_rev"]
# }
```

## Common Scenarios

- **Sort returns error**: Add the sort field to a compound Mango index.
- **Bookmark expired after compaction**: Restart the query from the beginning.
- **No usable index**: Create an index covering the selector and sort fields.

## Prevent It

- Always use `explain` to verify your queries use indexes
- Store and reuse bookmarks across requests
- Create compound indexes that cover both selector and sort fields

## Related Pages

- [CouchDB Mango Error](/tools/couchdb/couchdb-mango-error)
- [CouchDB Index Error](/tools/couchdb/couchdb-index-error)
- [CouchDB Stale Error](/tools/couchdb/couchdb-stale-error)
