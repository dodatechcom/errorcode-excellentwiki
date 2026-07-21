---
title: "[Solution] Neo4j APOC JSON Error"
description: "How to fix Neo4j APOC JSON processing errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- JSON malformed
- JSON path expression wrong
- Nested depth too deep

## How to Fix

```cypher
RETURN apoc.json.toJson({name: 'Alice', nested: {key: 'value'}})
```

## Examples

```cypher
CALL apoc.json.path('$.store.book[*].author', $jsonString)
```
