---
title: "[Solution] CouchDB Replication Rate Limit Error"
description: "How to fix CouchDB replication rate limit errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Replication rate limited
- Too many replications running
- Rate limit exceeded

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","batch_size":100}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {_id: .id, status: .status}'
```
