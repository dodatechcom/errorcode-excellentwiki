---
title: "[Solution] CouchDB Replication Doc IDs Error"
description: "How to fix CouchDB replication doc_ids filter errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Doc IDs not found
- Doc IDs format wrong
- Doc IDs filter not matching

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","doc_ids":["doc1","doc2"]}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {status: .status}'
```
