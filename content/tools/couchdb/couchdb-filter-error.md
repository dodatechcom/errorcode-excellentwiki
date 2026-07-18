---
title: "[Solution] CouchDB Filter Error — How to Fix"
description: "Fix CouchDB filter errors by correcting filter function syntax, resolving missing design document references, and fixing selector filters"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Filter Error

CouchDB filter errors occur when filter functions used in changes feeds or replication fail. Filters determine which documents are included in replication or change notifications.

## Why It Happens

- Filter function references a non-existent design document
- Filter function throws a JavaScript runtime error
- Mango selector syntax is incorrect
- Filter function is not defined in the design document
- Request parameter format is wrong for selector-based filters
- Filter function accesses undefined document properties

## Common Error Messages

```
{ "error": "bad_request", "reason": "invalid_filter" }
```

```
{ "error": "not_found", "reason": "missing_named_filter" }
```

```
{ "error": "internal_server_error", "reason": "filter function error" }
```

```
{ "error": "bad_request", "reason": "invalid_selector" }
```

## How to Fix It

### 1. Define Filter in Design Document

```bash
curl -X PUT http://localhost:5984/mydb/_design/filters \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/filters",
    "language": "javascript",
    "filters": {
      "my_filter": "function(doc, req) { return doc.type === req.query.type; }",
      "by_owner": "function(doc) { return doc.owner === \"admin\"; }",
      "recent": "function(doc) { return doc.timestamp > Date.now() - 86400000; }"
    }
  }'
```

### 2. Use Filter with Changes Feed

```bash
# Using built-in filter
curl 'http://localhost:5984/mydb/_changes?filter=_doc_ids&ids=doc1,doc2'

# Using custom filter
curl 'http://localhost:5984/mydb/_changes?filter=filters/my_filter&type=user'

# Using Mango selector filter
curl 'http://localhost:5984/mydb/_changes?filter=_selector' \
  -H "Content-Type: application/json" \
  -d '{"selector": {"type": "user", "active": true}}'
```

### 3. Use Filter with Replication

```json
{
  "source": "http://localhost:5984/source_db",
  "target": "http://localhost:5984/target_db",
  "filter": "filters/my_filter",
  "query_params": {
    "type": "user"
  }
}
```

```bash
# Mango selector-based replication filter
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://localhost:5984/source_db",
    "target": "http://localhost:5984/target_db",
    "filter": "_selector",
    "selector": {"type": "important"}
  }'
```

### 4. Debug Filter Function

```javascript
// Test filter function logic
function testFilter(doc, req) {
  // Simulate filter behavior
  const mockReq = { query: { type: "user" } };
  return doc.type === mockReq.query.type;
}

// Test with sample documents
const docs = [
  { type: "user", name: "Alice" },
  { type: "admin", name: "Bob" },
  { type: "user", name: "Charlie" }
];

docs.forEach(doc => {
  console.log(doc.name + ":", testFilter(doc, {}));
});
```

```bash
# Verify filter exists in design doc
curl http://localhost:5984/mydb/_design/filters | jq '.filters'

# Test changes feed with filter
curl 'http://localhost:5984/mydb/_changes?filter=filters/my_filter&type=user&limit=5'
```

## Common Scenarios

- **Replication filter not applied**: Ensure the filter is defined in the design document and the `filter` parameter includes the design doc prefix.
- **Selector filter returns nothing**: Check the Mango selector syntax and field values.
- **Filter slows down changes feed**: Optimize filter function to minimize per-document computation.

## Prevent It

- Test filter functions with `_changes` before using in replication
- Use `_selector` filter for simple Mango queries instead of custom JavaScript
- Cache filter results when possible to reduce computation

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Changes Error](/tools/couchdb/couchdb-changes-error)
- [CouchDB Mango Error](/tools/couchdb/couchdb-mango-error)
