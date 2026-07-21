---
title: "[Solution] Neo4j Cardinality Violation Error"
description: "How to fix Neo4j cardinality violation errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Expected single result but got multiple
- Aggregation not used when needed

## How to Fix

Use LIMIT:

```cypher
MATCH (n:Person {name: 'John'}) RETURN n LIMIT 1;
```

## Examples

```cypher
MATCH (n:Person {name: 'John'}) RETURN n LIMIT 1;
```
