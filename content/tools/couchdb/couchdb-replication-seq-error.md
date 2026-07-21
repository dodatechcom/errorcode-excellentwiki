---
title: "[Solution] CouchDB Replication Sequence Error"
description: "How to fix CouchDB replication sequence errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication sequence too old
- Replication sequence not found
- Replication sequence stale

## How to Fix

```bash
curl -s http://localhost:5984/mydb | jq '.update_seq'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_changes?since=0 | jq '.last_seq'
```
