---
title: "[Solution] CouchDB Update Handler Error — How to Fix"
description: "Fix CouchDB update handler errors by correcting HTTP method usage, validating request body parsing, and fixing document creation logic"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Update Handler Error

CouchDB update handler errors occur when design document update handlers fail to create or modify documents. Update handlers provide a REST-like API for document mutations.

## Why It Happens

- Update handler function throws a JavaScript error
- Request body is not properly parsed as JSON
- Handler tries to create a document with an existing _id without _rev
- Missing or invalid `send()` response
- Handler does not return the correct response format
- Database read/write permissions are insufficient

## Common Error Messages

```
{ "error": "not_found", "reason": "missing_named_update" }
```

```
{ "error": "internal_server_error", "reason": "update handler error" }
```

```
{ "error": "conflict", "reason": "Document update conflict." }
```

```
{ "error": "bad_request", "reason": "invalid request body" }
```

## How to Fix It

### 1. Create Valid Update Handler

```bash
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "language": "javascript",
    "updates": {
      "create_user": "function(doc, req) { if (!doc) { var newDoc = JSON.parse(req.body); newDoc._id = req.uuid; return [newDoc, JSON.stringify({ok: true, id: newDoc._id})]; } return [doc, \"exists\"]; }",
      "increment_counter": "function(doc, req) { if (!doc) { return [null, JSON.stringify({error: \"not_found\"})]; } doc.count = (doc.count || 0) + 1; return [doc, JSON.stringify({ok: true, count: doc.count})]; }"
    }
  }'
```

### 2. Handle Request Body Correctly

```javascript
// Update handler that creates a document
function(doc, req) {
  if (!doc) {
    // New document creation
    try {
      var body = JSON.parse(req.body);
      var newDoc = {
        _id: req.uuid,
        name: body.name || "Untitled",
        type: body.type || "default",
        created_at: new Date().toISOString()
      };
      return [newDoc, JSON.stringify({ok: true, id: newDoc._id})];
    } catch (e) {
      return [null, JSON.stringify({error: "invalid_json", reason: e.message})];
    }
  }
  return [doc, JSON.stringify({error: "already_exists"})];
}
```

### 3. Use Correct HTTP Method

```bash
# Update handlers are accessed via PUT
curl -X PUT http://localhost:5984/mydb/_design/app/_update/create_user \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "type": "admin"}'

# GET to read current state
curl http://localhost:5984/mydb/_design/app/_update/increment_counter/counter1
```

### 4. Return Proper Response Format

```javascript
// Update handler response format
function(doc, req) {
  if (!doc) {
    // Create new document: [newDoc, responseString]
    var newDoc = JSON.parse(req.body);
    newDoc._id = req.uuid;
    return [newDoc, JSON.stringify({ok: true, id: newDoc._id})];
  }

  // Update existing document
  doc.updated = true;
  doc.updated_at = new Date().toISOString();

  // Return [modifiedDoc, responseString]
  return [doc, JSON.stringify({ok: true, rev: doc._rev})];

  // Or return null to not save: [null, responseString]
  // return [null, JSON.stringify({error: "no_update_needed"})];
}
```

## Common Scenarios

- **Update handler creates duplicate documents**: Use `req.uuid` for unique IDs or check for existing docs.
- **Request body is null**: Ensure `Content-Type: application/json` header is set.
- **Handler does not save changes**: Return `[doc, response]` not just the response.

## Prevent It

- Always validate request body before parsing
- Use `req.uuid` for generating unique document IDs
- Return proper `[doc, response]` tuple from all update handlers

## Related Pages

- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Design Doc Error](/tools/couchdb/couchdb-design-doc-error)
- [CouchDB Show Error](/tools/couchdb/couchdb-show-error)
