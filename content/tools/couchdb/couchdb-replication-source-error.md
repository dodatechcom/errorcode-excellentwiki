---
title: "[Solution] CouchDB Replication Source Error"
description: "How to fix CouchDB replication source errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Source database not found
- Source database not accessible
- Source database authentication failed

## How to Fix

```bash
curl -s http://localhost:5984/mydb | jq '.db_name'
```

## Examples

```bash
curl -s http://localhost:5984/mydb | jq '.doc_count'
```
