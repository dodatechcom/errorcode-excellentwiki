---
title: "[Solution] CouchDB Attachment Proxy Error"
description: "How to fix CouchDB attachment proxy errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Proxy not forwarding attachment
- Proxy buffer overflow
- Proxy timeout on large attachment

## How to Fix

```bash
curl -s --max-time 60 http://proxy-host:5984/mydb/doc1/file.txt -o file.txt
```

## Examples

```bash
curl -v --max-time 60 http://proxy-host:5984/mydb/doc1/file.txt 2>&1 | head -20
```
