---
title: "[Solution] CouchDB Replication Connection Error"
description: "How to fix CouchDB replication connection errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication connection refused
- Replication connection timeout
- Replication connection reset

## How to Fix

```bash
curl -s http://localhost:5984/_up | jq .
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {status: .status, source: .source}'
```
