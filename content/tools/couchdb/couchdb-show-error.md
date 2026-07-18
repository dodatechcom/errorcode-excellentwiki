---
title: "[Solution] CouchDB Show Error — How to Fix"
description: "Fix CouchDB show function errors by debugging JavaScript rendering functions, fixing MIME types, and resolving missing document references"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Show Error

CouchDB show errors occur when design document show functions fail to render documents. Shows are used to transform document output into custom formats like HTML or XML.

## Why It Happens

- Show function throws a JavaScript runtime error
- Document referenced by show does not exist
- MIME type is not set in the response
- Show function accesses undefined document fields
- Missing `provides` function for content negotiation
- Show function returns invalid format

## Common Error Messages

```
{ "error": "not_found", "reason": "missing" }
```

```
{ "error": "internal_server_error", "reason": "show function error" }
```

```
{ "error": "bad_request", "reason": "invalid MIME type" }
```

```
{ "error": "not_found", "reason": "missing_named_show" }
```

## How to Fix It

### 1. Create Valid Show Function

```bash
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "language": "javascript",
    "shows": {
      "profile_page": "function(doc, req) { if (!doc) return {body: \"Not found\"}; return {body: \"<h1>\" + doc.name + \"</h1>\", headers: {\"Content-Type\": \"text/html\"}}; }"
    },
    "views": {
      "by_id": {
        "map": "function(doc) { emit(doc._id, null); }"
      }
    }
  }'
```

### 2. Handle Missing Documents

```javascript
// Show function with null doc handling
function(doc, req) {
  if (!doc) {
    return {
      body: JSON.stringify({error: "not_found", reason: "Document does not exist"}),
      headers: {"Content-Type": "application/json"},
      code: 404
    };
  }

  // Safe access with defaults
  var name = doc.name || "Unknown";
  var email = doc.email || "No email";

  return {
    body: JSON.stringify({name: name, email: email}),
    headers: {"Content-Type": "application/json"}
  };
}
```

### 3. Use Provides for Content Negotiation

```javascript
// Show function with multiple formats
function(doc, req) {
  provides('html', function() {
    return '<html><body><h1>' + doc.name + '</h1></body></html>';
  });

  provides('json', function() {
    return JSON.stringify(doc);
  });

  provides('xml', function() {
    return '<user><name>' + doc.name + '</name></user>';
  });
}
```

### 4. Debug Show Function Errors

```bash
# Test show with a specific document
curl 'http://localhost:5984/mydb/_design/app/_show/profile_page/doc123'

# Check error logs
tail -100 /opt/couchdb/log/couch.log | grep -i "show"

# Access the show function definition
curl http://localhost:5984/mydb/_design/app | jq '.shows'
```

## Common Scenarios

- **Show returns blank page**: Check that the document exists and the function does not throw.
- **Wrong MIME type in browser**: Set `Content-Type` header in the show function response.
- **Show function slow**: Minimize computation in shows; pre-compute with views.

## Prevent It

- Always handle null `doc` parameter in show functions
- Set explicit `Content-Type` headers in responses
- Use `provides` for content negotiation instead of hardcoding MIME types

## Related Pages

- [CouchDB List Error](/tools/couchdb/couchdb-list-error)
- [CouchDB Design Doc Error](/tools/couchdb/couchdb-design-doc-error)
- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
