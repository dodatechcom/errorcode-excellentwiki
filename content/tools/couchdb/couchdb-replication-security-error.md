---
title: "[Solution] CouchDB Replication Security Error"
description: "How to fix CouchDB replication security errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication blocked by security doc
- Security doc not configured
- User not authorized for replication

## How to Fix

```bash
curl -X PUT http://localhost:5984/mydb/_security -H 'Content-Type: application/json' -d '{"admins":{"names":["admin"],"roles":[]},"members":{"names":[],"roles":[]}}'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/_security | jq '.'
```
