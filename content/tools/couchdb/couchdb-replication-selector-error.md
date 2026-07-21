---
title: "[Solution] CouchDB Replication Selector Error — How to Fix"
description: "Fix CouchDB replication selector errors by resolving Mango selector issues in replication, fixing selector syntax problems, and handling selector-based replication failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Selector Error

CouchDB replication selector errors occur when using Mango selectors in replication fails to filter documents correctly.

## Why It Happens

- Selector syntax is invalid
- Selector references non-existent fields
- Selector is too complex for replication
- Selector does not match any documents
- Selector uses unsupported operators
- Index is missing for selector fields

## Common Error Messages

```
{ "error": "bad_request", "reason": "Invalid selector syntax" }
```

```
{ "error": "internal_server_error", "reason": "Selector evaluation failed" }
```

```
{ "error": "not_found", "reason": "No index for selector" }
```

```
{ "error": "bad_request", "reason": "Unsupported selector operator" }
```

## How to Fix It

### 1. Test Selector

```bash
# Test selector with Mango query
curl -X POST http://localhost:5984/mydb/_find \
  -H "Content-Type: application/json" \
  -d '{
    "selector": {"type": "event", "status": "active"}
  }'
```

### 2. Create Index for Selector

```bash
# Create index for selector fields
curl -X POST http://localhost:5984/mydb/_index \
  -H "Content-Type: application/json" \
  -d '{
    "index": {
      "fields": ["type", "status"]
    },
    "name": "by-type-status",
    "type": "json"
  }'
```

### 3. Use Selector in Replication

```bash
# Replicate with selector filter
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "filter": "_selector",
    "selector": {"type": "event", "status": "active"}
  }'
```

### 4. Fix Selector Syntax

```bash
# Simple selector
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "filter": "_selector",
    "selector": {"type": "event"}
  }'

# Complex selector with $and
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{
    "source": "http://source:5984/db",
    "target": "http://target:5984/db",
    "filter": "_selector",
    "selector": {
      "$and": [
        {"type": {"$eq": "event"}},
        {"status": {"$in": ["active", "pending"]}}
      ]
    }
  }'
```

## Common Scenarios

- **Invalid selector**: Fix Mango selector syntax.
- **No matching documents**: Check selector conditions.
- **No index for selector**: Create index for selector fields.

## Prevent It

- Test selectors with Mango queries first
- Create indexes for selector fields
- Use simple selectors when possible

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Mango Error](/tools/couchdb/couchdb-mango-error)
- [CouchDB Replication Filter Error](/tools/couchdb/couchdb-replication-filter-error)
