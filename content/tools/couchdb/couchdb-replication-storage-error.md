---
title: "[Solution] CouchDB Replication Storage Error"
description: "How to fix CouchDB replication storage errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Storage backend error
- Disk full during replication
- Storage I/O error

## How to Fix

```bash
df -h /var/lib/couchdb/
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {status: .status}'
```
