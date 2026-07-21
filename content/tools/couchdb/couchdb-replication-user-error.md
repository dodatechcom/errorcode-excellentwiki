---
title: "[Solution] CouchDB Replication User Error"
description: "How to fix CouchDB replication user errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication user not found
- Replication user lacks permissions
- Replication user credentials wrong

## How to Fix

```bash
curl -X PUT http://localhost:5984/_users/org.couchdb.user:repluser -H 'Content-Type: application/json' -d '{"name":"repluser","password":"pass","roles":["_replicator"],"type":"user"}'
```

## Examples

```bash
curl -s http://localhost:5984/_users/org.couchdb.user:repluser | jq '.name'
```
