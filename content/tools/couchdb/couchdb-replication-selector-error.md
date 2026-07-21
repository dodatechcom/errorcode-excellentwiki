---
title: "[Solution] CouchDB Replication Selector Error"
description: "How to fix CouchDB replication selector filter errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Selector syntax wrong
- Selector not matching any docs
- Selector too complex

## How to Fix

```bash
curl -X POST http://localhost:5984/_replicate -H 'Content-Type: application/json' -d '{"source":"mydb","target":"mydb-replica","filter":"_selector","selector":{"type":"public"}}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {status: .status}'
```
