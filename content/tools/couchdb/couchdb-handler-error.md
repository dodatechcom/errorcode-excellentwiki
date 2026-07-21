---
title: "[Solution] CouchDB Handler Error — How to Fix"
description: "Fix CouchDB handler errors by resolving show/list/update handler failures, fixing HTTP handler issues, and handling custom handler problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Handler Error

CouchDB handler errors occur when custom HTTP handlers (show, list, update) in design documents fail to execute due to JavaScript errors or configuration issues.

## Why It Happens

- Show handler function contains JavaScript errors
- List handler receives invalid data from view
- Update handler modifies document incorrectly
- Handler function times out
- Handler references a view that does not exist
- Handler returns invalid HTTP response

## Common Error Messages

```
{ "error": "not_found", "reason": "missing" }
```

```
{ "error": "internal_server_error", "reason": "Handler execution failed" }
```

```
{ "error": "compilation_error", "reason": "..." }
```

```
{ "error": "bad_request", "reason": "Invalid handler response" }
```

## How to Fix It

### 1. Create Show Handler

```bash
# Add show handler to design document
curl -X PUT http://localhost:5984/mydb/_design/handlers \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/handlers",
    "shows": {
      "hello": "function(doc, req) { return {body: \"Hello \" + doc.name}; }"
    }
  }'

# Use show handler
curl http://localhost:5984/mydb/doc123/_show/hello
```

### 2. Create Update Handler

```bash
# Add update handler
curl -X PUT http://localhost:5984/mydb/_design/handlers \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/handlers",
    "updates": {
      "increment": "function(doc, req) { doc.count = (doc.count || 0) + 1; return [doc, \"ok\"]; }"
    }
  }'

# Use update handler
curl -X PUT http://localhost:5984/mydb/doc123/_update/increment
```

### 3. Fix Handler Errors

```bash
# Test handler with debug
curl http://localhost:5984/mydb/doc123/_show/hello?debug=true

# Check handler logs
grep -i "handler" /opt/couchdb/log/couch.log
```

### 4. Create List Handler

```bash
# Add list handler
curl -X PUT http://localhost:5984/mydb/_design/handlers \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/handlers",
    "lists": {
      "items": "function(head, req) { var row; while (row = getRow()) { send(JSON.stringify(row) + \"\\n\"); } }"
    }
  }'
```

## Common Scenarios

- **Handler not found**: Ensure the handler exists in the design document.
- **Handler execution fails**: Check JavaScript syntax and debug output.
- **Handler returns wrong format**: Ensure the handler returns the correct HTTP response.

## Prevent It

- Test handlers with sample data before deployment
- Use try/catch in handler functions
- Log handler execution for debugging

## Related Pages

- [CouchDB Design Doc Error](/tools/couchdb/couchdb-design-doc-error)
- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
- [CouchDB HTTP Error](/tools/couchdb/couchdb-http-error)
