---
title: "[Solution] CouchDB Replication Timeout Error"
description: "How to fix CouchDB replication timeout errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication timeout too short
- Source or target too slow
- Network latency causing timeout

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","connection_timeout":30000,"timeout":60000}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {status: .status}'
```
