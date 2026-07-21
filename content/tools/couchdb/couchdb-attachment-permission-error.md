---
title: "[Solution] CouchDB Attachment Permission Error"
description: "How to fix CouchDB attachment permission errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- User lacks write permission
- Database security blocks attachment
- Role not authorized

## How to Fix

```bash
curl -s http://localhost:5984/mydb/_security | jq '.'
```

## Examples

```bash
curl -X PUT http://localhost:5984/mydb/_security -H 'Content-Type: application/json' -d '{"admins":{"names":["admin"],"roles":[]},"members":{"names":[],"roles":["user"]}}'
```
