---
title: "[Solution] CouchDB Attachment Compaction Error"
description: "How to fix CouchDB attachment compaction errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Compaction not reclaiming attachment space
- Attachment revisions not cleaned
- Compaction timeout

## How to Fix

```bash
curl -X POST http://localhost:5984/mydb/_compact
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_info | jq '.sizes'
```
