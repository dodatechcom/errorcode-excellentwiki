---
title: "[Solution] CouchDB Replication Deleted Docs Error"
description: "How to fix CouchDB replication deleted documents errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Deleted docs not replicated
- Deletion not propagated
- Conflicting deletions

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","doc_ids":["doc1","doc2"]}'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_changes?include_docs=true&style=all_docs | jq '.rows[] | select(.doc._deleted == true)'
```
