---
title: "[Solution] CouchDB Compaction Daemon Error"
description: "How to fix CouchDB automatic compaction errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Compaction daemon not running
- Compaction threshold not met
- Compaction failing due to disk space

## How to Fix

```ini
[compaction]
daemon = true
interval = 600
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_info | jq '.db_size'
```
