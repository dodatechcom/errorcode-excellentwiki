---
title: "[Solution] CouchDB Attachment Move Error"
description: "How to fix CouchDB attachment move errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Cannot move attachment between documents
- Must copy and delete
- Revision conflict during move

## How to Fix

```bash
curl -s http://localhost:5984/mydb/doc1/file.txt -o temp.txt
curl -X PUT http://localhost:5984/mydb/doc2/file.txt -H 'Content-Type: text/plain' -d @temp.txt
curl -X DELETE http://localhost:5984/mydb/doc1/file.txt?rev=2-abc
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc2 | jq '._attachments'
```
