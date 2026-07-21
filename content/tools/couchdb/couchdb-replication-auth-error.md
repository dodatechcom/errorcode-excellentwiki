---
title: "[Solution] CouchDB Replication Auth Error"
description: "How to fix CouchDB replication authentication errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication authentication failed
- Replication credentials wrong
- Replication token expired

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":{"url":"http://user:pass@source-host:5984/mydb"},"target":"mydb-replica"}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {error: .info.error}'
```
