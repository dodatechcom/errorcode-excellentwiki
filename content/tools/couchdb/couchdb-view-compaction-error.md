---
title: "[Solution] CouchDB View Compaction Error"
description: "How to fix CouchDB view compaction errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- View compaction taking too long
- View index corrupted
- Disk space insufficient

## How to Fix

```bash
curl -X POST http://localhost:5984/mydb/_compact
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_info | jq '.view_index'
```
