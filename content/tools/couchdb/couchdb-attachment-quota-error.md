---
title: "[Solution] CouchDB Attachment Quota Error"
description: "How to fix CouchDB attachment quota and limit errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Database quota exceeded
- Attachment count limit
- Total attachment size limit

## How to Fix

```ini
[replicator]
db_quota = 0
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_info | jq '.sizes'
```
