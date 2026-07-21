---
title: "[Solution] CouchDB Attachment Revision Error"
description: "How to fix CouchDB attachment revision errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Wrong revision used
- Revision not incremented
- Old revision referenced

## How to Fix

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._rev'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '.["_rev"]'
```
