---
title: "[Solution] CouchDB Attachment GZip Error"
description: "How to fix CouchDB attachment compression errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- GZip encoding not accepted
- Compressed attachment corrupted
- Decompression failing

## How to Fix

```bash
curl -s -H 'Accept-Encoding: gzip' http://localhost:5984/mydb/doc1/file.txt -o file.gz
```

## Examples

```bash
gunzip file.gz
```
