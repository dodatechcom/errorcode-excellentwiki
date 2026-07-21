---
title: "[Solution] CouchDB Replication Conflict Error"
description: "How to fix CouchDB replication conflicts"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Concurrent writes to same document
- Replication filter mismatch
- Document revision mismatch

## How to Fix

```bash
curl -s http://localhost:5984/mydb/_conflicts?revs=true | jq .
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_conflicts?revs=true | jq '.rows[] | {_id: ._id}'
```
