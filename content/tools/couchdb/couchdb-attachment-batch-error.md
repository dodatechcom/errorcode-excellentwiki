---
title: "[Solution] CouchDB Attachment Batch Upload Error"
description: "How to fix CouchDB attachment batch upload errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Multiple attachments failing
- Partial upload success
- Timeout on batch

## How to Fix

```bash
for f in file1.txt file2.txt file3.txt; do
curl -X PUT "http://localhost:5984/mydb/doc1/$f" -H 'Content-Type: text/plain' -d @$f
done
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._attachments | keys'
```
