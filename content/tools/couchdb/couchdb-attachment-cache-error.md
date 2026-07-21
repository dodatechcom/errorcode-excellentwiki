---
title: "[Solution] CouchDB Attachment Cache Error"
description: "How to fix CouchDB attachment caching errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Stale attachment served from cache
- Cache not invalidated
- ETag not set properly

## How to Fix

```bash
curl -s -I http://localhost:5984/mydb/doc1/file.txt | grep -i 'etag\|cache-control'
```

## Examples

```bash
curl -s -H 'If-None-Match: "abc"' -o /dev/null -w '%{http_code}' http://localhost:5984/mydb/doc1/file.txt
```
