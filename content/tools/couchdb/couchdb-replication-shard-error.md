---
title: "[Solution] CouchDB Replication Shard Error"
description: "How to fix CouchDB replication shard errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Shard not accessible during replication
- Shard rebalancing during replication
- Shard count mismatch

## How to Fix

```bash
curl -s http://localhost:5984/_membership | jq '.all_nodes'
```

## Examples

```bash
curl -s http://localhost:5984/mydb | jq '.shard_count'
```
