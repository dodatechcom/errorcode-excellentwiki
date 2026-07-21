---
title: "[Solution] CouchDB Replication SSL Error"
description: "How to fix CouchDB replication SSL errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- SSL not configured for replication
- SSL certificate not trusted
- SSL handshake failing

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"https://source-host:6984/mydb","target":"mydb-replica"}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {status: .status}'
```
