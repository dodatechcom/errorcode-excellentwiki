---
title: "[Solution] CouchDB Replication Batch Error"
description: "How to fix CouchDB replication batch size errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Batch size too large
- Batch size too small
- Batch processing failing

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","batch_size":500}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {status: .status}'
```
