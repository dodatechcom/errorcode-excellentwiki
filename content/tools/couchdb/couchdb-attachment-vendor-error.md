---
title: "[Solution] CouchDB Attachment Vendor Error"
description: "How to fix CouchDB attachment vendor-specific errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CouchDB version vendor extension
- Vendor-specific header not recognized
- Feature not supported in version

## How to Fix

```bash
curl -s http://localhost:5984/ | jq '.version'
```

## Examples

```bash
curl -s http://localhost:5984/_up | jq '.'
```
