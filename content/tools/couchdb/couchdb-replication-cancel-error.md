---
title: "[Solution] CouchDB Replication Cancel Error"
description: "How to fix CouchDB replication cancel errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication cannot be cancelled
- Replication already stopped
- Replication ID wrong

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"replication_id":"REPLICATION_ID","cancel":true}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | .id'
```
