---
title: "[Solution] CouchDB Attachment Range Request Error"
description: "How to fix CouchDB attachment range request errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Range header not supported
- Partial content not returned
- Range boundary wrong

## How to Fix

```bash
curl -s -H 'Range: bytes=0-100' http://localhost:5984/mydb/doc1/file.txt
```

## Examples

```bash
curl -s -I -H 'Range: bytes=0-100' http://localhost:5984/mydb/doc1/file.txt | grep -i content-range
```
