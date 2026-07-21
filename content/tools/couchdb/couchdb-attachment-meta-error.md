---
title: "[Solution] CouchDB Attachment Metadata Error"
description: "How to fix CouchDB attachment metadata errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Metadata fields missing
- Wrong metadata format
- Metadata not preserved

## How to Fix

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._attachments | to_entries[] | {name: .key, length: .value.length, digest: .value.digest}'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1 | jq '._attachments'
```
