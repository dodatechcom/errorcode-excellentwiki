---
title: "[Solution] CouchDB Attachment Rename Error"
description: "How to fix CouchDB attachment rename errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Cannot rename attachment directly
- Must re-upload with new name
- Old attachment not deleted

## How to Fix

```bash
curl -X PUT http://localhost:5984/mydb/doc1/newname.txt?rev=2-abc -H 'Content-Type: text/plain' -d 'content'
curl -X DELETE http://localhost:5984/mydb/doc1/oldname.txt?rev=3-def
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._attachments | keys'
```
