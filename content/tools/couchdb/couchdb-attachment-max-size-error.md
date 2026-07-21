---
title: "[Solution] CouchDB Attachment Max Size Error"
description: "How to fix CouchDB attachment size limit errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Attachment exceeds max_document_size
- Attachment too large for HTTP body
- Disk space insufficient

## How to Fix

```ini
[max_document_size]
max_document_size = 50000000
```

## Examples

```bash
curl -s http://localhost:5984/ | jq '.couchdb'
```
