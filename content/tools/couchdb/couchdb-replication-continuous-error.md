---
title: "[Solution] CouchDB Continuous Replication Error"
description: "How to fix CouchDB continuous replication errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Continuous replication stopped
- Replication feed lost
- Replication timeout

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","continuous":true}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.continuous == true)'
```
