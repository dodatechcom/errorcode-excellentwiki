---
title: "[Solution] CouchDB Attachment Delete Error"
description: "How to fix CouchDB attachment deletion errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Revision not specified
- Attachment not found
- Conflict on delete

## How to Fix

```bash
curl -X DELETE http://localhost:5984/mydb/doc1/file.txt?rev=2-abc
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._attachments'
```
