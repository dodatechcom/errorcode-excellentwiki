---
title: "[Solution] CouchDB Show Error — How to Fix"
description: "Fix CouchDB show errors by resolving show function failures, fixing document rendering issues, and handling show function compilation errors"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Show Error

CouchDB show errors occur when show functions in design documents fail to compile or execute, preventing document rendering.

## Why It Happens

- Show function contains JavaScript syntax errors
- Show function references undefined variables
- Show function throws an exception during execution
- Show function tries to access fields that do not exist
- Show function is missing from the design document
- Show function exceeds execution time limit

## Common Error Messages

```
{ "error": "compilation_error", "reason": "SyntaxError: ..." }
```

```
{ "error": "not_found", "reason": "Show function not found" }
```

```
{ "error": "internal_server_error", "reason": "Show function failed" }
```

```
{ "error": "bad_request", "reason": "Invalid show function" }
```

## How to Fix It

### 1. Fix Show Function

```bash
# Define correct show function
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "shows": {
      "render_doc": "function(doc, req) { if (!doc) { return { body: \"Not found\" }; } return { body: JSON.stringify(doc), headers: {\"Content-Type\": \"application/json\"} }; }"
    }
  }'
```

### 2. Test Show Function

```bash
# Test show function
curl http://localhost:5984/mydb/_design/app/_show/render_doc/doc123

# Check show function exists
curl http://localhost:5984/mydb/_design/app | jq '.shows'
```

### 3. Handle Missing Document

```bash
# Show function should handle missing doc
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "shows": {
      "safe_render": "function(doc, req) { if (!doc) { return { status: 404, body: JSON.stringify({error: \"not found\"}) }; } return { body: JSON.stringify(doc) }; }"
    }
  }'
```

### 4. Debug Show Function

```bash
# Enable debugging
curl http://localhost:5984/mydb/_design/app/_show/render_doc/doc123?debug=true

# Check show function info
curl http://localhost:5984/mydb/_design/app/_info
```

## Common Scenarios

- **Show function syntax error**: Fix JavaScript syntax in the show function.
- **Document not found**: Add null check in the show function.
- **Show function slow**: Optimize the JavaScript code in the show function.

## Prevent It

- Test show functions with sample data
- Handle null document case in all show functions
- Keep show functions simple and focused

## Related Pages

- [CouchDB Design Doc Error](/tools/couchdb/couchdb-design-doc-error)
- [CouchDB JavaScript Error](/tools/couchdb/couchdb-javascript-error)
- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
