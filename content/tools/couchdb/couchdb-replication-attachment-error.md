---
title: "[Solution] CouchDB Replication Attachment Error"
description: "How to fix CouchDB replication attachment errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Attachment not replicated
- Attachment too large for replication
- Attachment replication failing

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","att_encoding_info":true}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {status: .status}'
```
