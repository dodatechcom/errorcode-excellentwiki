---
title: "[Solution] CouchDB Replication Target Error"
description: "How to fix CouchDB replication target errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Target database not found
- Target database not accessible
- Target database authentication failed

## How to Fix

```bash
curl -X PUT http://localhost:5984/mydb-replica
```

## Examples

```bash
curl -s http://localhost:5984/mydb-replica | jq '.db_name'
```
