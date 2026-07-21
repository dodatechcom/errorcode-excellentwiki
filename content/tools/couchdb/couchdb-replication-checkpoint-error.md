---
title: "[Solution] CouchDB Replication Checkpoint Error"
description: "How to fix CouchDB replication checkpoint errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication checkpoint not created
- Replication checkpoint too old
- Replication checkpoint corrupted

## How to Fix

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {checkpoint: .checkpointed_source_seq}'
```

## Examples

```bash
curl -s http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","checkpoint_interval":60000}'
```
