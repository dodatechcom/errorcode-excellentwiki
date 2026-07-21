---
title: "[Solution] CouchDB Attachment Streaming Error"
description: "How to fix CouchDB attachment streaming errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Stream interrupted
- Connection reset
- Timeout on large attachment

## How to Fix

```bash
curl -s --max-time 300 http://localhost:5984/mydb/doc1/largefile.bin -o largefile.bin
```

## Examples

```bash
curl -s -o /dev/null -w '%{size_download} %{time_total}' http://localhost:5984/mydb/doc1/largefile.bin
```
