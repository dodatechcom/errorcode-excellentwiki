---
title: "[Solution] Neo4j Relationship Not Found Error"
description: "How to fix Neo4j relationship not found errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Relationship was deleted
- Wrong relationship type

## How to Fix

Search relationships:

```cypher
MATCH ()-[r]->() RETURN type(r), count(r);
```

## Examples

```cypher
MATCH (a)-[r:KNOWS]->(b) RETURN a, r, b LIMIT 10;
```
