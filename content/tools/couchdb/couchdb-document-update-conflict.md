---
title: "[Solution] CouchDB Document Update Conflict"
description: "How to fix CouchDB document update conflicts"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Stale revision used
- Concurrent update to same document
- Missing _rev field

## How to Fix

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._rev'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._rev'
```
