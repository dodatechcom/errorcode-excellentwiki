---
title: "[Solution] CouchDB Attachment Upload Error"
description: "How to fix CouchDB attachment upload errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Attachment data corrupted
- Content-Length header missing
- Revision conflict on upload

## How to Fix

```bash
curl -X PUT http://localhost:5984/mydb/doc1/file.txt?rev=1-abc -H 'Content-Type: text/plain' -d 'Hello World'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._attachments'
```
