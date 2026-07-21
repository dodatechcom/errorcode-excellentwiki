---
title: "[Solution] CouchDB Attachment Retry Error"
description: "How to fix CouchDB attachment retry errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Upload retry failing
- Network interruption
- Timeout on retry

## How to Fix

```bash
curl -s --retry 5 --retry-delay 3 http://localhost:5984/mydb/doc1/file.txt
```

## Examples

```bash
curl -v --retry 3 http://localhost:5984/mydb/doc1/file.txt 2>&1 | grep -i retry
```
