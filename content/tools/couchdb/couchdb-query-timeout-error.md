---
title: "[Solution] CouchDB Query Timeout Error — How to Fix"
description: "Fix CouchDB query timeout errors by resolving view query timeouts, fixing Mango query timeouts, and handling long-running query issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Query Timeout Error

CouchDB query timeout errors occur when view or Mango queries exceed the configured timeout limit before completing.

## Why It Happens

- Query is too complex for available resources
- View index is not up to date
- Database is under heavy load
- Query returns too many results
- Timeout setting is too low
- Network latency causes slow responses

## Common Error Messages

```
{ "error": "timeout", "reason": "Query timed out" }
```

```
{ "error": "internal_server_error", "reason": "View update exceeded timeout" }
```

```
{ "error": "timeout", "reason": "Mango query timeout" }
```

```
{ "error": "internal_server_error", "reason": "Request timeout" }
```

## How to Fix It

### 1. Increase Timeout Settings

```bash
# Increase view timeout
curl -X PUT http://localhost:5984/_node/_local/_config/httpd/view_timeout \
  -H "Content-Type: text/plain" \
  -d '"60000"'

# Increase query server timeout
curl -X PUT http://localhost:5984/_node/_local/_config/query_server/reduce_limit \
  -H "Content-Type: text/plain" \
  -d '"false"'
```

### 2. Optimize Query

```bash
# Add limit to reduce result set
curl "http://localhost:5984/mydb/_design/app/_view/by_type?limit=100"

# Use pagination
curl "http://localhost:5984/mydb/_design/app/_view/by_type?limit=50&skip=50"

# Use startkey/endkey to narrow results
curl "http://localhost:5984/mydb/_design/app/_view/by_type?startkey=\"event\"&endkey=\"event\""
```

### 3. Ensure View is Up to Date

```bash
# Check view info
curl http://localhost:5984/mydb/_design/app/_info

# Wait for view to be updated
curl http://localhost:5984/mydb/_design/app/_view/by_type?stale=false
```

### 4. Use Indexes for Mango Queries

```bash
# Create index for query fields
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {"fields": ["type", "timestamp"]},
    "name": "by-type-time",
    "type": "json"
  }'

# Query with index
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {"type": "event", "timestamp": {"$gt": "2024-01-01"}},
    "use_index": "by-type-time"
  }'
```

## Common Scenarios

- **Query timeout on large database**: Use pagination and startkey/endkey.
- **View update timeout**: Wait for view indexing to complete.
- **Mango query timeout**: Create appropriate indexes.

## Prevent It

- Create indexes for frequently queried fields
- Use pagination for large result sets
- Monitor query performance

## Related Pages

- [CouchDB Query Error](/tools/couchdb/couchdb-query-error)
- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
- [CouchDB Mango Error](/tools/couchdb/couchdb-mango-error)
