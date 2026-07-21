---
title: "[Solution] CouchDB Attachment Redirect Error"
description: "How to fix CouchDB attachment redirect errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Attachment URL redirects
- Redirect loop detected
- Redirect not followed

## How to Fix

```bash
curl -L -s http://localhost:5984/mydb/doc1/file.txt -o file.txt
```

## Examples

```bash
curl -v http://localhost:5984/mydb/doc1/file.txt 2>&1 | grep -i location
```
