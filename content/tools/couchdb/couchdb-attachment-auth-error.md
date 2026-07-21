---
title: "[Solution] CouchDB Attachment Auth Error"
description: "How to fix CouchDB attachment authentication errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Attachment requires auth
- Wrong credentials
- Session expired

## How to Fix

```bash
curl -s -u admin:password http://localhost:5984/mydb/doc1/file.txt
```

## Examples

```bash
curl -s -b cookies.txt http://localhost:5984/mydb/doc1/file.txt -o file.txt
```
