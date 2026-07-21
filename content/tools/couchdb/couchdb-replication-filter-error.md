---
title: "[Solution] CouchDB Replication Filter Error — How to Fix"
description: "Fix CouchDB replication filter errors by resolving filter function failures, fixing filter syntax issues, and handling filter-related replication problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Filter Error

CouchDB replication filter errors occur when replication filter functions fail, causing replication to stop or skip documents unexpectedly.

## Why It Happens

- Filter function contains JavaScript errors
- Filter function is missing from design document
- Filter function references non-existent fields
- Filter function throws exceptions
- Filter function is too restrictive (rejects all docs)
- Design document containing filter is deleted

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Filter function failed" }
```

```
{ "error": "not_found", "reason": "Filter function not found" }
```

```
{ "error": "compilation_error", "reason": "SyntaxError in filter function" }
```

```
{ "error": "internal_server_error", "reason": "Replication filter error" }
```

## How to Fix It

### 1. Fix Filter Function

```bash
# Create correct filter function
curl -X PUT http://localhost:5984/mydb/_design/filters \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/filters",
    "filters": {
      "important_docs": "function(doc, req) { return doc.type === \"important\"; }"
    }
  }'
```

### 2. Test Filter Function

```bash
# Test filter locally
curl "http://localhost:5984/mydb/_design/filters/_filter/important_docs"

# Check filter function exists
curl http://localhost:5984/mydb/_design/filters | jq '.filters'
```

### 3. Use Filter in Replication

```bash
# Create replication with filter
curl -X PUT http://localhost:5984/_replicator/filtered_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "filtered_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "filter": "filters/important_docs",
    "continuous": true
  }'
```

### 4. Debug Filter Function

```bash
# Enable debugging
curl -X PUT http://localhost:5984/mydb/_design/filters \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/filters",
    "filters": {
      "debug_filter": "function(doc, req) { log(\"Filtering doc: \" + doc._id); return doc.type === \"important\"; }"
    }
  }'

# Check filter function info
curl http://localhost:5984/mydb/_design/filters/_info
```

## Common Scenarios

- **Filter function syntax error**: Fix JavaScript syntax in filter function.
- **No documents replicated**: Check filter logic - may be too restrictive.
- **Filter function not found**: Verify design document exists and contains the filter.

## Prevent It

- Test filter functions with sample documents
- Log filter decisions for debugging
- Ensure design document with filter is deployed before replication

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Design Doc Error](/tools/couchdb/couchdb-design-doc-error)
- [CouchDB JavaScript Error](/tools/couchdb/couchdb-javascript-error)
