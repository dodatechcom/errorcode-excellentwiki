---
title: "[Solution] CouchDB Replication Backoff Error"
description: "How to fix CouchDB replication backoff errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication retrying too frequently
- Replication backoff not configured
- Replication failing repeatedly

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","backoff":10}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {backoff: .backoff_period}'
```
