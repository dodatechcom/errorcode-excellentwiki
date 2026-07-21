---
title: "[Solution] CouchDB Replication CORS Error"
description: "How to fix CouchDB replication CORS errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CORS not configured for replication
- Origin not whitelisted
- Preflight request failing

## How to Fix

```ini
[cors]
origins = *
credentials = true
```

## Examples

```bash
curl -I -H 'Origin: http://localhost:3000' http://localhost:5984/_replicate
```
