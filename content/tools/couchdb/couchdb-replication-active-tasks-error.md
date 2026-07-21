---
title: "[Solution] CouchDB Replication Active Tasks Error"
description: "How to fix CouchDB replication active tasks errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Active tasks not showing replication
- Active tasks not updating
- Active tasks query failing

## How to Fix

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication")'
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {_id: .id, status: .status}'
```
