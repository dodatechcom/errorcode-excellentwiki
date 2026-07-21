---
title: "[Solution] CouchDB Replication Network Error"
description: "How to fix CouchDB replication network errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Network unreachable
- DNS resolution failing
- Firewall blocking replication

## How to Fix

```bash
curl -s http://source-host:5984/_up
```

## Examples

```bash
curl -s http://localhost:5984/_active_tasks | jq '.[] | select(.type == "replication") | {status: .status}'
```
