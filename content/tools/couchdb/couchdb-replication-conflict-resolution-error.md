---
title: "[Solution] CouchDB Replication Conflict Resolution Error"
description: "How to fix CouchDB replication conflict resolution errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication conflict not resolved
- Auto-merge failing
- Conflict resolution strategy wrong

## How to Fix

```bash
curl -s http://localhost:5984/mydb/_conflicts | jq '.rows[] | {_id: ._id}'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_conflicts | jq '.total_rows'
```
