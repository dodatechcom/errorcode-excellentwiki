---
title: "[Solution] CouchDB Replication Cluster Error"
description: "How to fix CouchDB replication cluster errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Cluster not configured for replication
- Cluster node down
- Cluster not initialized

## How to Fix

```bash
curl -s http://localhost:5984/_cluster_setup | jq '.state'
```

## Examples

```bash
curl -s http://localhost:5984/_membership | jq '.all_nodes'
```
