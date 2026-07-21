---
title: "[Solution] CouchDB Attachment Content-Type Error"
description: "How to fix CouchDB attachment content type errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Content-Type not set
- Wrong Content-Type for file
- Browser not rendering file

## How to Fix

```bash
curl -X PUT http://localhost:5984/mydb/doc1/image.png -H 'Content-Type: image/png' -d @image.png
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._attachments | to_entries[] | {name: .key, content_type: .value.content_type}'
```
