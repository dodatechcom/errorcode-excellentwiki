---
title: "[Solution] CouchDB Attachment Sync Error"
description: "How to fix CouchDB attachment replication sync errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Attachment not synced during replication
- Sync conflict on attachment
- Attachment size mismatch

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","create_target":true}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication")'
```
