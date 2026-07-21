---
title: "[Solution] CouchDB Attachment MD5 Error"
description: "How to fix CouchDB attachment MD5 checksum errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- MD5 mismatch during upload
- Corrupted attachment data
- Encoding issue

## How to Fix

```bash
curl -s http://localhost:5984/mydb/doc1/file.txt | md5sum
```

## Examples

```bash
curl -s -I http://localhost:5984/mydb/doc1/file.txt | grep -i etag
```
