---
title: "[Solution] CouchDB Attachment CORS Error"
description: "How to fix CouchDB attachment CORS errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CORS headers missing for attachments
- Preflight request failing
- Origin not whitelisted

## How to Fix

```ini
[cors]
origins = http://localhost:3000
headers = accept, authorization, content-type, origin
methods = GET, PUT, POST, DELETE, HEAD
credentials = true
```

## Examples

```bash
curl -I -H 'Origin: http://localhost:3000' http://localhost:5984/mydb/doc1/file.txt
```
