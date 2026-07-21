---
title: "[Solution] CouchDB Replication Lag Error"
description: "How to fix CouchDB replication lag errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication lag too high
- Source database too large
- Network latency

## How to Fix

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {lag: .docs_pending, source: .source}'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication")'
```
