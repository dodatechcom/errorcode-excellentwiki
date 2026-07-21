---
title: "[Solution] CouchDB Attachment Download Error"
description: "How to fix CouchDB attachment download errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Attachment not found
- Revision mismatch
- Content-Encoding issue

## How to Fix

```bash
curl -s http://localhost:5984/mydb/doc1/file.txt -o file.txt
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1/file.txt | head -5
```
