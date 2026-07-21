---
title: "[Solution] CouchDB Replication ID Error"
description: "How to fix CouchDB replication ID errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication ID not found
- Replication ID format wrong
- Replication ID not tracked

## How to Fix

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | .id'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {_id: .id, status: .status}'
```
