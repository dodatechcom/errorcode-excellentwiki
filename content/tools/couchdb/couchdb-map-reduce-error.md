---
title: "[Solution] CouchDB Map Reduce Error — How to Fix"
description: "Fix CouchDB map reduce errors by resolving view compilation failures, fixing map/reduce function issues, and handling view performance problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Map Reduce Error

CouchDB map reduce errors occur when map or reduce functions in views fail to compile, execute, or produce correct results.

## Why It Happens

- Map function contains JavaScript syntax errors
- Reduce function is not deterministic
- View references fields that do not exist in documents
- Reduce function produces results that cannot be merged
- View is not yet indexed for the query
- JavaScript function exceeds execution time limit

## Common Error Messages

```
{ "error": "compilation_error", "reason": "..." }
```

```
{ "error": "not_found", "reason": "missing" }
```

```
{ "error": "internal_server_error", "reason": "View function failed" }
```

```
{ "error": "bad_request", "reason": "Invalid reduce function" }
```

## How to Fix It

### 1. Fix Map Function

```bash
# Correct map function
curl -X PUT http://localhost:5984/mydb/_design/stats \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/stats",
    "views": {
      "by_device": {
        "map": "function(doc) { if (doc.device_id && doc.value) { emit(doc.device_id, doc.value); } }"
      }
    }
  }'
```

### 2. Fix Reduce Function

```bash
# Use built-in reduce functions
# _sum, _count, _stats

curl -X PUT http://localhost:5984/mydb/_design/stats \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/stats",
    "views": {
      "device_total": {
        "map": "function(doc) { emit(doc.device_id, doc.value); }",
        "reduce": "_sum"
      }
    }
  }'
```

### 3. Query View Correctly

```bash
# Query view with parameters
curl "http://localhost:5984/mydb/_design/stats/_view/device_total?reduce=true&group=true"

# Query without reduce
curl "http://localhost:5984/mydb/_design/stats/_view/device_total?reduce=false"

# Pagination
curl "http://localhost:5984/mydb/_design/stats/_view/device_total?limit=10&skip=0"
```

### 4. Debug View Functions

```bash
# Enable debugging
curl "http://localhost:5984/mydb/_design/stats/_view/by_device?debug=true"

# Check view index status
curl http://localhost:5984/mydb/_design/stats/_info
```

## Common Scenarios

- **View compilation error**: Fix JavaScript syntax in map/reduce functions.
- **View returns no data**: Ensure documents have the fields referenced in the map function.
- **Reduce function is slow**: Use built-in reduce functions instead of custom ones.

## Prevent It

- Test map/reduce functions with sample data
- Use built-in reduce functions when possible
- Keep view functions simple and focused

## Related Pages

- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
- [CouchDB Design Doc Error](/tools/couchdb/couchdb-design-doc-error)
- [CouchDB JSON Error](/tools/couchdb/couchdb-json-error)
