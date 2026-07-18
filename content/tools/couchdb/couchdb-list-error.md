---
title: "[Solution] CouchDB List Error — How to Fix"
description: "Fix CouchDB list function errors by debugging view iteration, fixing header output, and resolving missing view references"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB List Error

CouchDB list errors occur when list functions that transform view output fail. Lists iterate over view rows and produce custom output formats like CSV, XML, or HTML pages.

## Why It Happens

- List function throws a JavaScript runtime error
- Referenced view does not exist or has no data
- List function does not call `getRow()` to iterate
- Missing or invalid header/footer output
- List function accesses properties not present in view rows
- Infinite loop in list function

## Common Error Messages

```
{ "error": "not_found", "reason": "missing_named_list" }
```

```
{ "error": "internal_server_error", "reason": "list function error" }
```

```
{ "error": "bad_request", "reason": "missing_view" }
```

```
{ "error": "internal_server_error", "reason": "timeout" }
```

## How to Fix It

### 1. Create Valid List Function

```bash
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "language": "javascript",
    "lists": {
      "csv_export": "function(head, req) { send(\"Name,Email\\n\"); while(row = getRow()) { send(row.key + \",\" + row.value + \"\\n\"); } }"
    },
    "views": {
      "by_name": {
        "map": "function(doc) { if (doc.name && doc.email) emit(doc.name, doc.email); }"
      }
    }
  }'
```

### 2. Handle Empty View Results

```javascript
// List function with empty result handling
function(head, req) {
  send('<html><body>\n');
  send('<table>\n');

  var count = 0;
  while (row = getRow()) {
    if (count === 0) {
      send('<tr><th>Name</th><th>Email</th></tr>\n');
    }
    send('<tr><td>' + row.key + '</td><td>' + row.value + '</td></tr>\n');
    count++;
  }

  if (count === 0) {
    send('<tr><td colspan="2">No results found</td></tr>\n');
  }

  send('</table>\n');
  send('</body></html>');
}
```

### 3. Use Provides for Multiple Formats

```javascript
function(head, req) {
  provides('csv', function() {
    send('Name,Email\n');
    while (row = getRow()) {
      send(row.key + ',' + row.value + '\n');
    }
  });

  provides('json', function() {
    var results = [];
    while (row = getRow()) {
      results.push({name: row.key, email: row.value});
    }
    send(JSON.stringify(results));
  });

  provides('html', function() {
    send('<ul>\n');
    while (row = getRow()) {
      send('<li>' + row.key + ': ' + row.value + '</li>\n');
    }
    send('</ul>\n');
  });
}
```

### 4. Debug List Function

```bash
# Test list with view
curl 'http://localhost:5984/mydb/_design/app/_list/csv_export/by_name'

# Check list function exists
curl http://localhost:5984/mydb/_design/app | jq '.lists'

# View the list function source
curl http://localhost:5984/mydb/_design/app | jq -r '.lists.csv_export'
```

## Common Scenarios

- **List returns empty**: Ensure the referenced view has data and emits key-value pairs.
- **CSV export missing header**: Call `send()` before the `getRow()` loop for header row.
- **List times out on large view**: Use pagination with `startkey`/`endkey` on the view.

## Prevent It

- Always call `getRow()` in a while loop to consume all rows
- Handle the empty result case explicitly
- Use `provides` for content negotiation instead of multiple list functions

## Related Pages

- [CouchDB Show Error](/tools/couchdb/couchdb-show-error)
- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
- [CouchDB Design Doc Error](/tools/couchdb/couchdb-design-doc-error)
