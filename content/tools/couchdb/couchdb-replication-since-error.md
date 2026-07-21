---
title: "[Solution] CouchDB Replication Since Error"
description: "How to fix CouchDB replication since parameter errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Since parameter wrong
- Since sequence not found
- Since too old

## How to Fix

```bash
curl -s http://localhost:5984/mydb/_changes?since=0 | jq '.last_seq'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_changes?since=NOW | jq '.last_seq'
```
