---
title: "[Solution] CouchDB Replication Filter Syntax Error"
description: "How to fix CouchDB replication filter syntax errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Filter function syntax wrong
- Missing quotes in filter name
- Filter function not registered

## How to Fix

```bash
curl -X PUT http://localhost:5984/mydb/_design/myfilter -H 'Content-Type: application/json' -d '{"filters":{"myfilter":"function(doc){return doc.type==\"public\"}"}}'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_design/myfilter/_filter/myfilter
```
