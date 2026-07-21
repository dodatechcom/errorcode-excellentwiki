---
title: "[Solution] CouchDB Disk Full Error"
description: "How to fix CouchDB disk space errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Database partition full
- Compaction not freeing space
- View index consuming disk

## How to Fix

```bash
du -sh /var/lib/couchdb/*.couch
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_info | jq '.db_size'
```
