---
title: "[Solution] Neo4j APOC Schema Error"
description: "How to fix Neo4j APOC schema procedure errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Schema procedure not found
- Index not yet available
- Constraint not applied

## How to Fix

```cypher
CALL apoc.schema.assert({Person: ['name']}, {Friend: ['since']})
```

## Examples

```cypher
CALL db.indexes() YIELD labelsOrTypes, properties
```
