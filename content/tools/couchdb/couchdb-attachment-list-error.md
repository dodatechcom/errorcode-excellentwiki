---
title: "[Solution] CouchDB Attachment List Error"
description: "How to fix CouchDB attachment list errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- No attachments on document
- Attachments not returned in listing
- Query parameter wrong

## How to Fix

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._attachments | keys'
```

## Examples

```bash
curl -s 'http://localhost:5984/mydb/_all_docs?include_docs=true&attachments=true' | jq '.rows[] | ._attachments'
```
