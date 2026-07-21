---
title: "[Solution] CouchDB Conflict Resolution Error"
description: "How to fix CouchDB conflict resolution errors"
tools: ["couchdb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Multiple conflicting revisions
- Auto-merge not working
- Conflict not resolved after update

## How to Fix

```bash
curl -s http://localhost:5984/mydb/doc1?conflicts=true | jq '.["_conflicts"]'
```

## Examples

```bash
curl -s http://localhost:5984/mydb/doc1?conflicts=true | jq '.'
```
