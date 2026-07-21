---
title: "[Solution] CouchDB Attachment Rate Limit Error"
description: "How to fix CouchDB attachment rate limit errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Too many attachment requests
- Rate limit exceeded
- Concurrent upload limit

## How to Fix

```bash
curl -s --retry 3 --retry-delay 5 http://localhost:5984/mydb/doc1/file.txt
```

## Examples

```bash
curl -s -o /dev/null -w '%{http_code}' http://localhost:5984/mydb/doc1/file.txt
```
