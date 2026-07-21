---
title: "[Solution] CouchDB Replication Quota Error"
description: "How to fix CouchDB replication quota errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Database quota exceeded
- Replication quota not configured
- Replication exceeding quota

## How to Fix

```ini
[replicator]
db_quota = 0
```

## Examples

```bash
curl -s http://localhost:5984/mydb | jq '.sizes'
```
