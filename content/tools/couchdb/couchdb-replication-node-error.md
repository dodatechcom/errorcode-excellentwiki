---
title: "[Solution] CouchDB Replication Node Error"
description: "How to fix CouchDB replication node errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Node not reachable
- Node down during replication
- Node not in cluster

## How to Fix

```bash
curl -s http://localhost:5984/_membership | jq '.all_nodes'
```

## Examples

```bash
curl -s http://localhost:5984/_nodes | jq '.rows[].id'
```
