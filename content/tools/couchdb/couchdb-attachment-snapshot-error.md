---
title: "[Solution] CouchDB Attachment Snapshot Error"
description: "How to fix CouchDB attachment snapshot errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Attachment not in snapshot
- Snapshot not including attachments
- Snapshot query wrong

## How to Fix

```bash
curl -s 'http://localhost:5984/mydb/_changes?include_docs=true&attachments=true' | jq '.rows[] | ._attachments'
```

## Examples

```bash
curl -s 'http://localhost:5984/mydb/_all_docs?include_docs=true&attachments=true' | jq '.rows[] | {id: .id, attachments: (._attachments | keys)}'
```
