---
title: "[Solution] CouchDB Stale Error — How to Fix"
description: "Fix CouchDB stale view errors by configuring stale parameters, rebuilding view indexes, and resolving stale read issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Stale Error

CouchDB stale errors occur when querying views that return outdated data or when the stale parameter is misconfigured. Views may lag behind the latest database changes.

## Why It Happens

- View index has not been updated since the last database change
- `stale=ok` returns outdated data without rebuilding
- `stale=update_after` triggers rebuild but returns stale data first
- View compaction interrupted the index build
- Large databases take a long time to update view indexes
- View function produces inconsistent results

## Common Error Messages

```
{ "error": "timeout", "reason": "view generation timed out" }
```

```
{ "error": "internal_server_error", "reason": "view stale" }
```

```
{ "error": "bad_request", "reason": "invalid_stale_value" }
```

```
{ "error": "not_found", "reason": "missing_named_view" }
```

## How to Fix It

### 1. Use Correct Stale Parameter

```bash
# Force fresh results (may be slow)
curl 'http://localhost:5984/mydb/_design/app/_view/by_name?stale=false'

# Return immediately with potentially stale data
curl 'http://localhost:5984/mydb/_design/app/_view/by_name?stale=ok'

# Return stale data immediately, update in background
curl 'http://localhost:5984/mydb/_design/app/_view/by_name?stale=update_after'
```

### 2. Rebuild Stale View Index

```bash
# Check if view needs updating
curl 'http://localhost:5984/mydb/_design/app/_view/by_name?stale=false' \
  -w "\nHTTP Code: %{http_code}\nTime: %{time_total}s\n"

# Force view rebuild by compacting views
curl -X POST http://localhost:5984/mydb/_view_compact \
  -H "Content-Type: application/json" \
  -d '{"design": "app"}'

# Or query with stale=update_after to trigger background rebuild
curl 'http://localhost:5984/mydb/_design/app/_view/by_name?stale=update_after&limit=1'
```

### 3. Configure View Update Threshold

```ini
; In local.ini
[couchdb]
; How often to update views (in milliseconds)
; view_update_after = 5000
```

```bash
# Check view update status
curl http://localhost:5984/_active_tasks | jq '.[] | select(.type == "indexer")'

# Monitor view build progress
curl http://localhost:5984/_node/_local/_stats | jq '.couchdb'
```

### 4. Optimize View Performance

```javascript
// Use reduce for efficient queries
{
  "views": {
    "count_by_type": {
      "map": "function(doc) { if (doc.type) emit(doc.type, 1); }",
      "reduce": "_sum"
    },
    "recent_docs": {
      "map": "function(doc) { if (doc.created_at) emit(doc.created_at, doc._id); }"
    }
  }
}
```

```bash
# Use reduce to avoid fetching all rows
curl 'http://localhost:5984/mydb/_design/app/_view/count_by_type?reduce=true&group=true'

# Paginate with startkey/endkey instead of skip
curl 'http://localhost:5984/mydb/_design/app/_view/recent_docs?startkey="2024-01-01"&limit=25'
```

## Common Scenarios

- **Dashboard shows old data**: Use `stale=update_after` for non-critical reads.
- **View rebuild takes hours**: Compact the database first, then rebuild views.
- **stale=ok returns wrong counts**: Accept eventual consistency or use `stale=false`.

## Prevent It

- Use `stale=update_after` for background view updates
- Monitor view lag with `_active_tasks`
- Design views with reduce functions to minimize index size

## Related Pages

- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
- [CouchDB Index Error](/tools/couchdb/couchdb-index-error)
- [CouchDB Find Error](/tools/couchdb/couchdb-find-error)
